#!/usr/bin/env python3
"""Capture source-page images into a local, cited, linked visual asset index."""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, html, json, math, os, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
from typing import Any
import numpy as np
from PIL import Image

UA = "Mozilla/5.0 (SA&BOO Visual Asset Index; private research cache)"
IMG_RE = re.compile(r'<(?:img|source)[^>]+(?:src|data-src|data-original|data-lazy-src|srcset)=["\']([^"\']+)', re.I)
META_RE = re.compile(r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)', re.I)
TITLE_RE = re.compile(r'<title[^>]*>(.*?)</title>', re.I | re.S)
BAD_HINTS = re.compile(r'(logo|icon|flag|sprite|avatar|favicon|loader|spinner|svg-icon|menu-|brandmark)', re.I)


def fetch(url: str, timeout: int = 25) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get("Content-Type", "")


def page_title(markup: str, fallback: str) -> str:
    m = TITLE_RE.search(markup)
    if not m:
        return fallback
    return html.unescape(re.sub(r"\s+", " ", m.group(1)).strip())


def extract_image_urls(markup: str, page_url: str) -> list[str]:
    urls: list[str] = []
    for raw in META_RE.findall(markup) + IMG_RE.findall(markup):
        for part in raw.split(","):
            u = part.strip().split()[0] if part.strip() else ""
            if not u or u.startswith("data:"):
                continue
            u = html.unescape(u)
            if u.startswith("//"):
                u = "https:" + u
            u = urllib.parse.urljoin(page_url, u)
            if BAD_HINTS.search(u):
                continue
            if u not in urls:
                urls.append(u)
    return urls


def ext_from_content_type(content_type: str, url: str) -> str:
    ct = content_type.lower()
    if "jpeg" in ct or "jpg" in ct:
        return ".jpg"
    if "png" in ct:
        return ".png"
    if "webp" in ct:
        return ".webp"
    if "gif" in ct:
        return ".gif"
    path = urllib.parse.urlparse(url).path.lower()
    for e in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
        if path.endswith(e):
            return ".jpg" if e == ".jpeg" else e
    return ".img"


def image_vector(img: Image.Image) -> np.ndarray:
    im = img.convert("RGB").resize((128, 128))
    arr = np.asarray(im).astype("float32") / 255.0
    # color histogram 16 bins per channel
    feats = []
    for c in range(3):
        hist, _ = np.histogram(arr[:, :, c], bins=16, range=(0, 1), density=True)
        feats.extend(hist.tolist())
    mean = arr.reshape(-1, 3).mean(axis=0)
    std = arr.reshape(-1, 3).std(axis=0)
    gray = arr.mean(axis=2)
    gx = np.diff(gray, axis=1, append=gray[:, -1:])
    gy = np.diff(gray, axis=0, append=gray[-1:, :])
    edge = np.sqrt(gx * gx + gy * gy)
    edge_hist, _ = np.histogram(edge, bins=16, range=(0, 1), density=True)
    aspect = img.width / max(img.height, 1)
    brightness = float(gray.mean())
    contrast = float(gray.std())
    feats.extend(mean.tolist() + std.tolist() + edge_hist.tolist() + [aspect, brightness, contrast])
    vec = np.asarray(feats, dtype="float32")
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec


def save_thumbnail(img: Image.Image, path: Path, max_size: int = 360) -> None:
    thumb = img.convert("RGB")
    thumb.thumbnail((max_size, max_size))
    thumb.save(path, "JPEG", quality=82, optimize=True)


def rel(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except Exception:
        return str(path)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", required=True, help="JSON file with source pages")
    ap.add_argument("--out", required=True, help="Output visual cache directory")
    ap.add_argument("--max-total", type=int, default=40)
    ap.add_argument("--max-per-source", type=int, default=8)
    ap.add_argument("--min-width", type=int, default=360)
    ap.add_argument("--min-height", type=int, default=240)
    args = ap.parse_args()

    seeds = json.loads(Path(args.seeds).read_text(encoding="utf-8"))
    out = Path(args.out).expanduser().resolve()
    originals = out / "originals"
    thumbs = out / "thumbs"
    originals.mkdir(parents=True, exist_ok=True)
    thumbs.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    vectors: list[np.ndarray] = []
    captured_at = dt.datetime.now(dt.timezone.utc).isoformat()

    for seed in seeds:
        if len(records) >= args.max_total:
            break
        page_url = seed["source_page_url"]
        try:
            page_bytes, _ct = fetch(page_url)
            markup = page_bytes.decode("utf-8", "ignore")
        except Exception as e:
            print(f"WARN page failed {page_url}: {e}", file=sys.stderr)
            continue
        title = page_title(markup, seed.get("source_name", page_url))
        image_urls = extract_image_urls(markup, page_url)
        source_count = 0
        last_in_source: str | None = None
        for img_url in image_urls:
            if len(records) >= args.max_total or source_count >= args.max_per_source:
                break
            try:
                data, ct = fetch(img_url, timeout=20)
                ext = ext_from_content_type(ct, img_url)
                if ext in {".svg", ".img"} and "image" not in ct.lower():
                    continue
                sha = hashlib.sha256(data).hexdigest()
                asset_id = "VA-" + sha[:12]
                img_path = originals / f"{asset_id}{ext}"
                # Verify image bytes before committing to cache, so failed SVG/HTML/403 bodies do not become orphan assets.
                import io
                with Image.open(io.BytesIO(data)) as img:
                    img.load()
                    width, height = img.size
                    if width < args.min_width or height < args.min_height:
                        continue
                    if not img_path.exists():
                        img_path.write_bytes(data)
                    thumb_path = thumbs / f"{asset_id}.jpg"
                    save_thumbnail(img, thumb_path)
                    vec = image_vector(img)
            except Exception as e:
                print(f"WARN image failed {img_url}: {e}", file=sys.stderr)
                continue
            rec = {
                "asset_id": asset_id,
                "title": title,
                "source_name": seed.get("source_name", ""),
                "source_page_url": page_url,
                "original_image_url": img_url,
                "local_image_path": rel(img_path, out),
                "local_thumbnail_path": rel(thumb_path, out),
                "width": width,
                "height": height,
                "file_ext": ext,
                "sha256": sha,
                "captured_at": captured_at,
                "tags": seed.get("tags", []),
                "category": seed.get("category", "visual-reference"),
                "visual_notes": seed.get("visual_notes", "Captured original visual reference for private SA&BOO study and indexing."),
                "rights_status": seed.get("rights_status", "reference-only"),
                "usage_allowed": seed.get("usage_allowed", "private-study"),
                "prev_id": records[-1]["asset_id"] if records else None,
                "next_id": None,
                "source_prev_id": last_in_source,
                "source_next_id": None,
                "related_ids": [],
                "vector_file": "vectors.npy",
                "vector_row": len(vectors),
            }
            if records:
                records[-1]["next_id"] = asset_id
            if last_in_source:
                for r in reversed(records):
                    if r["asset_id"] == last_in_source:
                        r["source_next_id"] = asset_id
                        break
            records.append(rec)
            vectors.append(vec)
            last_in_source = asset_id
            source_count += 1
            time.sleep(0.05)

    # Add simple related links by visual cosine within same/different categories.
    if vectors:
        mat = np.vstack(vectors)
        sim = mat @ mat.T
        for i, rec in enumerate(records):
            order = np.argsort(-sim[i])
            rec["related_ids"] = [records[j]["asset_id"] for j in order if j != i][:5]
        np.save(out / "vectors.npy", mat)
        (out / "vector_index.json").write_text(json.dumps([r["asset_id"] for r in records], ensure_ascii=False, indent=2), encoding="utf-8")

    jsonl = out / "visual_assets.jsonl"
    with jsonl.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    csv_path = out / "visual_assets.csv"
    if records:
        with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(records[0].keys()))
            w.writeheader(); w.writerows(records)
    chain = {"head": records[0]["asset_id"] if records else None, "tail": records[-1]["asset_id"] if records else None, "count": len(records), "items": [{"asset_id": r["asset_id"], "prev_id": r["prev_id"], "next_id": r["next_id"]} for r in records]}
    (out / "asset_chain.json").write_text(json.dumps(chain, ensure_ascii=False, indent=2), encoding="utf-8")

    # HTML contact sheet with local thumbnails and source links.
    cards = []
    for r in records:
        tags = ", ".join(r.get("tags", []))
        cards.append(f'''<article class="card"><a href="{r['local_image_path']}"><img src="{r['local_thumbnail_path']}"/></a><h3>{html.escape(r['asset_id'])}</h3><p>{html.escape(r['source_name'])}</p><p>{html.escape(tags)}</p><p>{r['width']}×{r['height']} · {html.escape(r['rights_status'])}</p><p><a href="{html.escape(r['source_page_url'])}">source page</a></p></article>''')
    html_doc = f'''<!doctype html><meta charset="utf-8"><title>SA&BOO Visual Asset Index</title><style>body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;background:#111;color:#eee;margin:24px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:18px}}.card{{background:#1c1c1c;border:1px solid #333;border-radius:14px;padding:12px}}img{{width:100%;height:180px;object-fit:cover;border-radius:10px}}a{{color:#c8aa73}}p{{font-size:12px;color:#bbb}}h3{{font-size:14px}}</style><h1>SA&BOO Visual Asset Index</h1><p>Count: {len(records)} · Cached: {captured_at} · Third-party images are reference-only unless rights say otherwise.</p><div class="grid">{''.join(cards)}</div>'''
    (out / "preview.html").write_text(html_doc, encoding="utf-8")
    print(f"Captured {len(records)} assets into {out}")
    print(f"Index: {jsonl}")
    print(f"Preview: {out / 'preview.html'}")

if __name__ == "__main__":
    main()
