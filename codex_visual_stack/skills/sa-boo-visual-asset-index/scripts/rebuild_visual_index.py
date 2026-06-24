#!/usr/bin/env python3
"""Rebuild SA&BOO visual asset hybrid vectors and reports.

Hybrid vector = image features + hashed text/tag metadata features.
No cloud API required. This is intentionally lightweight and portable.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, re
from pathlib import Path
from typing import Iterable
import numpy as np
from PIL import Image

TOKEN_RE = re.compile(r"[a-zA-Z0-9\u4e00-\u9fff]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def image_vector(img: Image.Image) -> np.ndarray:
    im = img.convert("RGB").resize((128, 128))
    arr = np.asarray(im).astype("float32") / 255.0
    feats: list[float] = []
    # RGB histograms: color distribution
    for c in range(3):
        hist, _ = np.histogram(arr[:, :, c], bins=16, range=(0, 1), density=True)
        feats.extend(hist.tolist())
    # mean/std: palette and saturation/contrast hint
    mean = arr.reshape(-1, 3).mean(axis=0)
    std = arr.reshape(-1, 3).std(axis=0)
    gray = arr.mean(axis=2)
    # edge histogram: composition/detail density hint
    gx = np.diff(gray, axis=1, append=gray[:, -1:])
    gy = np.diff(gray, axis=0, append=gray[-1:, :])
    edge = np.sqrt(gx * gx + gy * gy)
    edge_hist, _ = np.histogram(edge, bins=16, range=(0, 1), density=True)
    aspect = img.width / max(img.height, 1)
    feats.extend(mean.tolist() + std.tolist() + edge_hist.tolist() + [aspect, float(gray.mean()), float(gray.std())])
    vec = np.asarray(feats, dtype="float32")
    n = np.linalg.norm(vec)
    return vec / n if n else vec


def text_vector(text: str, dims: int = 256) -> np.ndarray:
    v = np.zeros(dims, dtype="float32")
    toks = tokenize(text)
    if not toks:
        return v
    for tok in toks:
        h = int(hashlib.sha256(tok.encode("utf-8")).hexdigest()[:8], 16)
        idx = h % dims
        sign = 1.0 if ((h >> 8) & 1) else -1.0
        v[idx] += sign
    n = np.linalg.norm(v)
    return v / n if n else v


def record_text(r: dict) -> str:
    tags = r.get("tags", [])
    if isinstance(tags, str):
        tags_s = tags
    else:
        tags_s = " ".join(map(str, tags))
    return " ".join([
        str(r.get("asset_id", "")),
        str(r.get("title", "")),
        str(r.get("source_name", "")),
        str(r.get("category", "")),
        tags_s,
        str(r.get("visual_notes", "")),
    ])


def load_records(index: Path) -> list[dict]:
    return [json.loads(x) for x in index.read_text(encoding="utf-8").splitlines() if x.strip()]


def write_csv(path: Path, records: list[dict]) -> None:
    if not records:
        return
    keys = list(records[0].keys())
    for r in records:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader(); w.writerows(records)


def write_report(out: Path, records: list[dict], limit: int = 80) -> Path:
    lines = [
        "# SA&BOO Visual Asset Index — Original Asset Reference Report",
        "",
        f"Asset library: `{out}`",
        f"Count: **{len(records)}**",
        "",
        "> Third-party cached images are for private study/reference unless `rights_status` explicitly says otherwise.",
        "",
        "## How to cite an asset in future outputs",
        "",
        "```text",
        "Asset ID: VA-...",
        "Original: /absolute/path/to/original",
        "Thumbnail: /absolute/path/to/thumb",
        "Source: https://...",
        "Rights: reference-only / owned / user-provided / open-license",
        "What this visual teaches: ...",
        "```",
        "",
        "## Indexed assets",
        "",
    ]
    for r in records[:limit]:
        original = out / r.get("local_image_path", "")
        thumb = out / r.get("local_thumbnail_path", "")
        tags = r.get("tags", [])
        if not isinstance(tags, str):
            tags = ", ".join(map(str, tags))
        lines += [
            f"### {r.get('asset_id')} — {r.get('source_name','')}",
            "",
            f"![{r.get('asset_id')}]({thumb})",
            "",
            f"- **Original:** `{original}`",
            f"- **Source page:** {r.get('source_page_url','')}",
            f"- **Original image URL:** {r.get('original_image_url','')}",
            f"- **Category:** `{r.get('category','')}`",
            f"- **Tags:** {tags}",
            f"- **Rights / usage:** `{r.get('rights_status','')}` / `{r.get('usage_allowed','')}`",
            f"- **Size:** {r.get('width')}×{r.get('height')}",
            f"- **Chain:** prev `{r.get('prev_id')}` → next `{r.get('next_id')}`",
            f"- **Related:** {', '.join(map(str, r.get('related_ids', [])[:5]))}",
            "",
        ]
    p = out / "VISUAL_ASSET_INDEX.md"
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Visual asset index directory containing visual_assets.jsonl")
    ap.add_argument("--text-weight", type=float, default=0.45)
    ap.add_argument("--image-weight", type=float, default=0.55)
    ap.add_argument("--report-limit", type=int, default=120)
    args = ap.parse_args()
    out = Path(args.out).expanduser().resolve()
    records = load_records(out / "visual_assets.jsonl")
    vectors = []
    image_vectors = []
    text_vectors = []
    for i, r in enumerate(records):
        img_path = out / r.get("local_image_path", "")
        with Image.open(img_path) as img:
            iv = image_vector(img)
        tv = text_vector(record_text(r))
        hv = np.concatenate([iv * args.image_weight, tv * args.text_weight]).astype("float32")
        n = np.linalg.norm(hv)
        hv = hv / n if n else hv
        r["vector_row"] = i
        r["vector_file"] = "vectors.npy"
        image_vectors.append(iv)
        text_vectors.append(tv)
        vectors.append(hv)
    if vectors:
        mat = np.vstack(vectors).astype("float32")
        sim = mat @ mat.T
        for i, r in enumerate(records):
            order = np.argsort(-sim[i])
            r["related_ids"] = [records[j]["asset_id"] for j in order if j != i][:8]
        np.save(out / "vectors.npy", mat)
        np.save(out / "image_vectors.npy", np.vstack(image_vectors).astype("float32"))
        np.save(out / "text_vectors.npy", np.vstack(text_vectors).astype("float32"))
    (out / "vector_index.json").write_text(json.dumps([r["asset_id"] for r in records], ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "visual_assets.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n", encoding="utf-8")
    write_csv(out / "visual_assets.csv", records)
    chain = {"head": records[0]["asset_id"] if records else None, "tail": records[-1]["asset_id"] if records else None, "count": len(records), "items": [{"asset_id": r["asset_id"], "prev_id": r.get("prev_id"), "next_id": r.get("next_id")} for r in records]}
    (out / "asset_chain.json").write_text(json.dumps(chain, ensure_ascii=False, indent=2), encoding="utf-8")
    report = write_report(out, records, args.report_limit)
    print(f"Rebuilt hybrid vector index: {out / 'vectors.npy'} shape={np.load(out / 'vectors.npy').shape if vectors else (0,0)}")
    print(f"Report: {report}")

if __name__ == "__main__":
    main()
