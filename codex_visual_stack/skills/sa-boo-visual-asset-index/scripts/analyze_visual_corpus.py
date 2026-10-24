#!/usr/bin/env python3
"""Measure deterministic visual patterns in an existing image corpus.

This script does not score taste. It produces pixel/metadata evidence and coarse
cluster representatives for later full-image review by a designer.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def load_catalog(path: Path | None) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    if not path or not path.exists():
        return {}, {}
    text = path.read_text(encoding="utf-8")
    try:
        raw = json.loads(text)
        rows = raw if isinstance(raw, list) else raw.get("items", [])
    except json.JSONDecodeError:
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    by_id: dict[str, dict[str, Any]] = {}
    by_name: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        asset_id = str(row.get("asset_id", ""))
        if asset_id:
            by_id[asset_id] = row
        for key in ("art_study_path", "local_image_path", "filename"):
            value = row.get(key)
            if value:
                by_name[Path(str(value)).name] = row
    return by_id, by_name


def asset_id_for(path: Path, row: dict[str, Any] | None) -> str:
    if row and row.get("asset_id"):
        return str(row["asset_id"])
    return path.stem.split("_")[0]


def srgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    xyz = linear @ np.array(
        [[0.4124564, 0.3575761, 0.1804375],
         [0.2126729, 0.7151522, 0.0721750],
         [0.0193339, 0.1191920, 0.9503041]],
        dtype="float32",
    ).T
    xyz /= np.array([0.95047, 1.0, 1.08883], dtype="float32")
    delta = 6 / 29
    f = np.where(xyz > delta ** 3, np.cbrt(xyz), xyz / (3 * delta ** 2) + 4 / 29)
    return np.stack(
        [116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])],
        axis=-1,
    )


def palette(img: Image.Image, colors: int = 5) -> list[dict[str, Any]]:
    sample = img.convert("RGB").resize((96, 96))
    q = sample.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    counts = q.getcolors(96 * 96) or []
    pal = q.getpalette() or []
    total = sum(count for count, _ in counts) or 1
    result = []
    for count, idx in sorted(counts, reverse=True):
        rgb = tuple(pal[idx * 3:idx * 3 + 3])
        result.append({"hex": "#%02X%02X%02X" % rgb, "share": round(count / total, 4)})
    return result


def ocr_metrics(ocr_dir: Path | None, asset_id: str) -> dict[str, Any]:
    if not ocr_dir or not ocr_dir.exists():
        return {"ocr_available": False, "ocr_line_count": None, "ocr_text_area": None,
                "ocr_center_x": None, "ocr_center_y": None}
    matches = sorted(ocr_dir.glob(f"{asset_id}_*.json")) or sorted(ocr_dir.glob(f"{asset_id}.json"))
    if not matches:
        return {"ocr_available": False, "ocr_line_count": None, "ocr_text_area": None,
                "ocr_center_x": None, "ocr_center_y": None}
    data = json.loads(matches[0].read_text(encoding="utf-8"))
    boxes = [line.get("bbox") for line in data.get("lines", []) if line.get("bbox")]
    mask = np.zeros((200, 200), dtype=bool)
    weighted_x = 0.0
    weighted_y = 0.0
    weight = 0.0
    for box in boxes:
        if len(box) != 4:
            continue
        x, y, w, h = [float(v) for v in box]
        x0 = max(0, min(199, int(math.floor(x * 200))))
        x1 = max(x0 + 1, min(200, int(math.ceil((x + w) * 200))))
        # Apple Vision records a bottom-left origin; convert to top-left for centroid.
        top = 1.0 - y - h
        y0 = max(0, min(199, int(math.floor(top * 200))))
        y1 = max(y0 + 1, min(200, int(math.ceil((top + h) * 200))))
        mask[y0:y1, x0:x1] = True
        area = max(w * h, 0.0)
        weighted_x += (x + w / 2) * area
        weighted_y += (top + h / 2) * area
        weight += area
    return {
        "ocr_available": True,
        "ocr_line_count": len(boxes),
        "ocr_text_area": round(float(mask.mean()), 6),
        "ocr_center_x": round(weighted_x / weight, 6) if weight else None,
        "ocr_center_y": round(weighted_y / weight, 6) if weight else None,
    }


def spatial_metrics(saliency: np.ndarray) -> dict[str, Any]:
    h, w = saliency.shape
    total = float(saliency.sum())
    if total <= 1e-12:
        return {"saliency_center_x": 0.5, "saliency_center_y": 0.5,
                "saliency_center_share": 0.0, "saliency_entropy": 0.0,
                "saliency_grid": [0.0] * 9}
    ys, xs = np.mgrid[0:h, 0:w]
    cx = float((saliency * (xs + 0.5)).sum() / total / w)
    cy = float((saliency * (ys + 0.5)).sum() / total / h)
    grid = []
    for gy in range(3):
        for gx in range(3):
            y0, y1 = gy * h // 3, (gy + 1) * h // 3
            x0, x1 = gx * w // 3, (gx + 1) * w // 3
            grid.append(float(saliency[y0:y1, x0:x1].sum() / total))
    probs = np.asarray(grid, dtype="float64")
    entropy = float(-(probs[probs > 0] * np.log(probs[probs > 0])).sum() / math.log(9))
    return {
        "saliency_center_x": round(cx, 6),
        "saliency_center_y": round(cy, 6),
        "saliency_center_share": round(grid[4], 6),
        "saliency_entropy": round(entropy, 6),
        "saliency_grid": [round(x, 6) for x in grid],
    }


def image_metrics(path: Path) -> tuple[dict[str, Any], Image.Image]:
    with Image.open(path) as raw:
        img = ImageOps.exif_transpose(raw).convert("RGB")
        width, height = img.size
        work = img.copy()
    work.thumbnail((320, 320))
    rgb = np.asarray(work, dtype="float32") / 255.0
    lab = srgb_to_lab(rgb)
    linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    lum = 0.2126 * linear[..., 0] + 0.7152 * linear[..., 1] + 0.0722 * linear[..., 2]
    mx = rgb.max(axis=2)
    mn = rgb.min(axis=2)
    saturation = np.divide(mx - mn, mx, out=np.zeros_like(mx), where=mx > 1e-8)
    gx = np.diff(lum, axis=1, append=lum[:, -1:])
    gy = np.diff(lum, axis=0, append=lum[-1:, :])
    grad = np.sqrt(gx * gx + gy * gy)
    local_deviation = np.abs(lab[..., 0] - np.median(lab[..., 0])) / 100.0
    saliency = grad + 0.35 * local_deviation
    rg = rgb[..., 0] - rgb[..., 1]
    yb = 0.5 * (rgb[..., 0] + rgb[..., 1]) - rgb[..., 2]
    colorfulness = math.sqrt(float(rg.std()) ** 2 + float(yb.std()) ** 2) + 0.3 * math.sqrt(float(rg.mean()) ** 2 + float(yb.mean()) ** 2)
    result = {
        "width": width,
        "height": height,
        "aspect_ratio": round(width / max(height, 1), 6),
        "lab_mean_l": round(float(lab[..., 0].mean()), 6),
        "lab_mean_a": round(float(lab[..., 1].mean()), 6),
        "lab_mean_b": round(float(lab[..., 2].mean()), 6),
        "lab_std_l": round(float(lab[..., 0].std()), 6),
        "saturation_mean": round(float(saturation.mean()), 6),
        "saturation_p75": round(float(np.percentile(saturation, 75)), 6),
        "low_saturation_share": round(float((saturation < 0.12).mean()), 6),
        "luminance_mean": round(float(lum.mean()), 6),
        "luminance_contrast_p95_p05": round(float(np.percentile(lum, 95) - np.percentile(lum, 5)), 6),
        "colorfulness": round(float(colorfulness), 6),
        "edge_strength": round(float(grad.mean()), 6),
        "edge_density": round(float((grad > 0.06).mean()), 6),
        "palette": palette(work),
    }
    result.update(spatial_metrics(saliency))
    return result, work


def feature_matrix(rows: list[dict[str, Any]]) -> np.ndarray:
    keys = [
        "lab_mean_l", "lab_mean_a", "lab_mean_b", "lab_std_l",
        "saturation_mean", "luminance_contrast_p95_p05", "colorfulness",
        "edge_strength", "edge_density", "saliency_center_x", "saliency_center_y",
        "saliency_center_share", "saliency_entropy", "ocr_text_area",
    ]
    matrix = []
    for row in rows:
        values = [float(row.get(key) or 0.0) for key in keys]
        values.append(math.log(max(float(row["aspect_ratio"]), 1e-6)))
        matrix.append(values)
    return np.asarray(matrix, dtype="float32")


def kmeans(x: np.ndarray, k: int, iterations: int = 80) -> tuple[np.ndarray, np.ndarray]:
    k = max(1, min(k, len(x)))
    mean = x.mean(axis=0)
    first = int(np.argmax(((x - mean) ** 2).sum(axis=1)))
    centers = [x[first].copy()]
    while len(centers) < k:
        dist = np.min(np.stack([((x - c) ** 2).sum(axis=1) for c in centers]), axis=0)
        centers.append(x[int(np.argmax(dist))].copy())
    cmat = np.stack(centers)
    labels = np.zeros(len(x), dtype=int)
    for _ in range(iterations):
        new_labels = np.argmin(((x[:, None, :] - cmat[None, :, :]) ** 2).sum(axis=2), axis=1)
        if np.array_equal(labels, new_labels):
            labels = new_labels
            break
        labels = new_labels
        for idx in range(k):
            members = x[labels == idx]
            if len(members):
                cmat[idx] = members.mean(axis=0)
    return labels, cmat


def representatives(x: np.ndarray, labels: np.ndarray, centers: np.ndarray, per_cluster: int = 4) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for cluster_id in range(len(centers)):
        idxs = np.flatnonzero(labels == cluster_id)
        order = sorted(idxs, key=lambda i: float(((x[i] - centers[cluster_id]) ** 2).sum()))
        result[cluster_id] = [int(i) for i in order[:per_cluster]]
    return result


def contact_sheet(rows: list[dict[str, Any]], reps: dict[int, list[int]], out: Path) -> None:
    cell_w, cell_h = 260, 210
    cols = max((len(v) for v in reps.values()), default=1)
    sheet = Image.new("RGB", (cols * cell_w, len(reps) * cell_h), "#F2F0EA")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for cluster_id, idxs in sorted(reps.items()):
        for col, idx in enumerate(idxs):
            row = rows[idx]
            with Image.open(row["path"]) as raw:
                img = ImageOps.exif_transpose(raw).convert("RGB")
            img.thumbnail((cell_w - 16, cell_h - 40))
            x = col * cell_w + (cell_w - img.width) // 2
            y = cluster_id * cell_h + 8
            sheet.paste(img, (x, y))
            label = f"C{cluster_id + 1} {row['asset_id']}  sat {row['saturation_mean']:.2f}  text {row.get('ocr_text_area') or 0:.2f}"
            draw.text((col * cell_w + 8, cluster_id * cell_h + cell_h - 24), label, fill="#171717", font=font)
    sheet.save(out, "JPEG", quality=88, optimize=True)


def round_median(rows: list[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return round(float(np.median(values)), 6) if values else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", required=True, help="Canonical image directory")
    ap.add_argument("--out", required=True, help="Independent output directory")
    ap.add_argument("--catalog", help="Optional JSON array or JSONL asset catalog")
    ap.add_argument("--ocr-dir", help="Optional OCR JSON directory with normalized bounding boxes")
    ap.add_argument("--clusters", type=int, default=6)
    args = ap.parse_args()

    image_dir = Path(args.images).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    catalog_path = Path(args.catalog).expanduser().resolve() if args.catalog else None
    ocr_dir = Path(args.ocr_dir).expanduser().resolve() if args.ocr_dir else None
    by_id, by_name = load_catalog(catalog_path)

    paths = sorted(
        (p for p in image_dir.rglob("*") if p.is_file() and p.suffix.lower() in EXTS),
        key=lambda p: p.name,
    )
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for path in paths:
        hinted_id = path.stem.split("_")[0]
        catalog_row = by_name.get(path.name) or by_id.get(hinted_id)
        asset_id = asset_id_for(path, catalog_row)
        try:
            metrics, _ = image_metrics(path)
        except Exception as exc:
            errors.append({"path": str(path), "error": str(exc)})
            continue
        row: dict[str, Any] = {
            "asset_id": asset_id,
            "path": str(path),
            "title": (catalog_row or {}).get("title", path.stem),
            "tags": (catalog_row or {}).get("tags", []),
            "review_status": (catalog_row or {}).get("review_status"),
            "feedback_status": (catalog_row or {}).get("feedback_status"),
            "transfer_rule": (catalog_row or {}).get("transfer_rule") or (catalog_row or {}).get("quality_notes"),
        }
        row.update(metrics)
        row.update(ocr_metrics(ocr_dir, asset_id))
        rows.append(row)

    if not rows:
        raise SystemExit("No readable images found")

    raw_features = feature_matrix(rows)
    mean = raw_features.mean(axis=0)
    std = raw_features.std(axis=0)
    standardized = (raw_features - mean) / np.where(std < 1e-8, 1.0, std)
    labels, centers = kmeans(standardized, args.clusters)
    reps = representatives(standardized, labels, centers)
    for idx, label in enumerate(labels):
        rows[idx]["cluster_id"] = f"C{int(label) + 1}"

    metrics_path = out / "corpus_metrics.jsonl"
    metrics_path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")

    summary_clusters = []
    for cluster_id in range(len(centers)):
        members = [rows[i] for i in range(len(rows)) if labels[i] == cluster_id]
        palette_counts = Counter(color["hex"] for row in members for color in row["palette"][:2])
        tag_counts = Counter(
            str(tag) for row in members for tag in row.get("tags", [])
            if str(tag).strip()
        )
        summary_clusters.append({
            "cluster_id": f"C{cluster_id + 1}",
            "count": len(members),
            "representative_ids": [rows[i]["asset_id"] for i in reps[cluster_id]],
            "median_lab_l": round_median(members, "lab_mean_l"),
            "median_saturation": round_median(members, "saturation_mean"),
            "median_luminance_contrast": round_median(members, "luminance_contrast_p95_p05"),
            "median_edge_density": round_median(members, "edge_density"),
            "median_text_area": round_median(members, "ocr_text_area"),
            "median_saliency_center_share": round_median(members, "saliency_center_share"),
            "frequent_palette_hex": [x for x, _ in palette_counts.most_common(5)],
            "frequent_tags": [x for x, _ in tag_counts.most_common(8)],
        })

    summary = {
        "image_dir": str(image_dir),
        "count": len(rows),
        "error_count": len(errors),
        "measurement_scope": [
            "Lab color and luminance", "saturation and colorfulness", "coarse palette",
            "luminance contrast", "edge/detail density", "aspect ratio",
            "saliency concentration proxy", "OCR text area and centroid when boxes exist",
        ],
        "limitations": [
            "Clusters describe measured similarity, not aesthetic quality or approval.",
            "Saliency is a deterministic edge and lightness-deviation proxy, not eye tracking.",
            "OCR area depends on available detected boxes and may miss stylized lettering.",
            "Screenshots or UI chrome in source images influence measurements unless cropped beforehand.",
        ],
        "overall_medians": {
            "lab_l": round_median(rows, "lab_mean_l"),
            "saturation": round_median(rows, "saturation_mean"),
            "luminance_contrast": round_median(rows, "luminance_contrast_p95_p05"),
            "edge_density": round_median(rows, "edge_density"),
            "text_area": round_median(rows, "ocr_text_area"),
        },
        "clusters": summary_clusters,
        "errors": errors,
    }
    (out / "corpus_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    contact_sheet(rows, reps, out / "cluster_representatives.jpg")

    lines = [
        "# Visual corpus measurement report",
        "",
        f"Images measured: **{len(rows)}**  ",
        f"Read errors: **{len(errors)}**",
        "",
        "> Evidence only: clusters and pixel statistics do not score taste, originality, cultural fit, or user approval.",
        "",
        "## Overall medians",
        "",
        f"- Lab L*: `{summary['overall_medians']['lab_l']}`",
        f"- Saturation: `{summary['overall_medians']['saturation']}`",
        f"- Luminance contrast p95-p05: `{summary['overall_medians']['luminance_contrast']}`",
        f"- Edge density: `{summary['overall_medians']['edge_density']}`",
        f"- OCR text area: `{summary['overall_medians']['text_area']}`",
        "",
        "## Coarse clusters for visual review",
        "",
    ]
    for item in summary_clusters:
        lines += [
            f"### {item['cluster_id']} — {item['count']} images",
            "",
            f"Representatives: {', '.join(item['representative_ids'])}",
            f"Median saturation `{item['median_saturation']}`, contrast `{item['median_luminance_contrast']}`, edge density `{item['median_edge_density']}`, OCR text area `{item['median_text_area']}`.",
            f"Frequent quantized colors: {', '.join(item['frequent_palette_hex'])}",
            f"Frequent explicit tags: {', '.join(item['frequent_tags'])}",
            "",
        ]
    lines += [
        "## Required interpretation step",
        "",
        "Inspect the representative full images and at least one counterexample per candidate mechanism. Cross-check catalog tags, transfer rules, and exact user feedback before updating a method ledger or design skill.",
        "",
        "See `corpus_summary.json` for machine-readable metrics and `cluster_representatives.jpg` for the compact review sheet.",
    ]
    (out / "corpus_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Measured {len(rows)} images into {out}")
    print(f"Metrics: {metrics_path}")
    print(f"Representatives: {out / 'cluster_representatives.jpg'}")


if __name__ == "__main__":
    main()
