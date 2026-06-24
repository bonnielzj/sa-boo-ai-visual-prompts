#!/usr/bin/env python3
"""Search SA&BOO visual asset index by text, image similarity, or hybrid query."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
import numpy as np
from PIL import Image

TOKEN_RE = re.compile(r"[a-zA-Z0-9\u4e00-\u9fff]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def image_vector(img: Image.Image) -> np.ndarray:
    im = img.convert("RGB").resize((128, 128))
    arr = np.asarray(im).astype("float32") / 255.0
    feats: list[float] = []
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
    feats.extend(mean.tolist() + std.tolist() + edge_hist.tolist() + [aspect, float(gray.mean()), float(gray.std())])
    vec = np.asarray(feats, dtype="float32")
    n = np.linalg.norm(vec)
    return vec / n if n else vec


def text_vector(text: str, dims: int = 256) -> np.ndarray:
    v = np.zeros(dims, dtype="float32")
    for tok in tokenize(text):
        h = int(hashlib.sha256(tok.encode("utf-8")).hexdigest()[:8], 16)
        v[h % dims] += 1.0 if ((h >> 8) & 1) else -1.0
    n = np.linalg.norm(v)
    return v / n if n else v


def load_records(index: Path) -> list[dict]:
    return [json.loads(line) for line in index.read_text(encoding="utf-8").splitlines() if line.strip()]


def result_obj(rank: int, score: float, r: dict, base: Path) -> dict:
    return {
        "rank": rank,
        "score": round(float(score), 6),
        "asset_id": r.get("asset_id"),
        "title": r.get("title"),
        "source_name": r.get("source_name"),
        "source_page_url": r.get("source_page_url"),
        "original_image_url": r.get("original_image_url"),
        "image": str(base / r.get("local_image_path", "")),
        "thumbnail": str(base / r.get("local_thumbnail_path", "")),
        "category": r.get("category"),
        "tags": r.get("tags", []),
        "rights_status": r.get("rights_status"),
        "usage_allowed": r.get("usage_allowed"),
        "prev_id": r.get("prev_id"),
        "next_id": r.get("next_id"),
        "related_ids": r.get("related_ids", [])[:5],
        "visual_notes": r.get("visual_notes", ""),
    }


def print_markdown(results: list[dict]) -> None:
    for x in results:
        print(f"### {x['rank']}. {x['asset_id']} — score {x['score']}")
        print(f"![{x['asset_id']}]({x['thumbnail']})")
        print(f"- Original: `{x['image']}`")
        print(f"- Source: {x['source_page_url']}")
        print(f"- Original image URL: {x['original_image_url']}")
        print(f"- Category: `{x['category']}`")
        print(f"- Tags: {', '.join(map(str, x['tags'])) if isinstance(x['tags'], list) else x['tags']}")
        print(f"- Rights / usage: `{x['rights_status']}` / `{x['usage_allowed']}`")
        print(f"- Chain: prev `{x['prev_id']}` → next `{x['next_id']}`")
        print(f"- Related: {', '.join(map(str, x['related_ids']))}")
        print("")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--query", default="")
    ap.add_argument("--image", default="")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--format", choices=["jsonl", "markdown"], default="jsonl")
    ap.add_argument("--text-weight", type=float, default=0.45)
    ap.add_argument("--image-weight", type=float, default=0.55)
    args = ap.parse_args()
    index = Path(args.index).expanduser().resolve()
    base = index.parent
    records = load_records(index)
    if not records:
        return
    scores = np.zeros(len(records), dtype="float32")
    if args.query:
        tvs = np.load(base / "text_vectors.npy") if (base / "text_vectors.npy").exists() else None
        qv = text_vector(args.query)
        if tvs is not None and tvs.shape[1] == qv.shape[0]:
            scores += args.text_weight * (tvs @ qv)
        # exact token overlap bonus keeps tag search crisp
        qtok = set(tokenize(args.query))
        for i, r in enumerate(records):
            hay = " ".join(map(str, [r.get("asset_id", ""), r.get("title", ""), r.get("source_name", ""), r.get("category", ""), r.get("tags", ""), r.get("visual_notes", "")]))
            rtok = set(tokenize(hay))
            if qtok:
                scores[i] += 0.35 * len(qtok & rtok) / max(len(qtok), 1)
    if args.image:
        ivs = np.load(base / "image_vectors.npy") if (base / "image_vectors.npy").exists() else np.load(base / "vectors.npy")
        with Image.open(args.image) as img:
            qiv = image_vector(img)
        if ivs.shape[1] == qiv.shape[0]:
            scores += args.image_weight * (ivs @ qiv)
    if not args.query and not args.image:
        scores += 1
    order = np.argsort(-scores)[:args.top]
    results = [result_obj(rank, float(scores[int(i)]), records[int(i)], base) for rank, i in enumerate(order, 1)]
    if args.format == "markdown":
        print_markdown(results)
    else:
        for x in results:
            print(json.dumps(x, ensure_ascii=False))

if __name__ == "__main__":
    main()
