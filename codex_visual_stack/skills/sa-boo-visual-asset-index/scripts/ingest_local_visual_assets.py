#!/usr/bin/env python3
"""Ingest user-owned/local visual files into the SA&BOO visual asset index."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, shutil
from pathlib import Path
import numpy as np
from PIL import Image

EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.tif', '.tiff'}

def image_vector(img: Image.Image) -> np.ndarray:
    im = img.convert('RGB').resize((128, 128))
    arr = np.asarray(im).astype('float32') / 255.0
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
    feats.extend(mean.tolist() + std.tolist() + edge_hist.tolist() + [aspect, float(gray.mean()), float(gray.std())])
    vec = np.asarray(feats, dtype='float32')
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec

def save_thumb(img: Image.Image, path: Path) -> None:
    t = img.convert('RGB')
    t.thumbnail((360, 360))
    t.save(path, 'JPEG', quality=82, optimize=True)

def load_existing(out: Path):
    idx = out / 'visual_assets.jsonl'
    if not idx.exists():
        return []
    return [json.loads(x) for x in idx.read_text(encoding='utf-8').splitlines() if x.strip()]

def write_all(out: Path, records, vectors):
    if records:
        for i, r in enumerate(records):
            r['prev_id'] = records[i-1]['asset_id'] if i else None
            r['next_id'] = records[i+1]['asset_id'] if i < len(records)-1 else None
            r['vector_row'] = i
            r['vector_file'] = 'vectors.npy'
        mat = np.vstack(vectors).astype('float32')
        sim = mat @ mat.T
        for i, r in enumerate(records):
            order = np.argsort(-sim[i])
            r['related_ids'] = [records[j]['asset_id'] for j in order if j != i][:5]
        np.save(out / 'vectors.npy', mat)
        (out / 'vector_index.json').write_text(json.dumps([r['asset_id'] for r in records], ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'visual_assets.jsonl').write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in records) + ('\n' if records else ''), encoding='utf-8')
    chain = {'head': records[0]['asset_id'] if records else None, 'tail': records[-1]['asset_id'] if records else None, 'count': len(records), 'items': [{'asset_id': r['asset_id'], 'prev_id': r.get('prev_id'), 'next_id': r.get('next_id')} for r in records]}
    (out / 'asset_chain.json').write_text(json.dumps(chain, ensure_ascii=False, indent=2), encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--local-dir', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--category', default='user-provided')
    ap.add_argument('--tags', default='user-provided,SA&BOO')
    ap.add_argument('--rights-status', default='user-provided')
    ap.add_argument('--usage-allowed', default='private-study,project-reference')
    args = ap.parse_args()
    src = Path(args.local_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    originals = out / 'originals'; thumbs = out / 'thumbs'
    originals.mkdir(parents=True, exist_ok=True); thumbs.mkdir(parents=True, exist_ok=True)
    records = load_existing(out)
    existing_ids = {r['asset_id'] for r in records}
    vectors = []
    # Rebuild existing vectors from current records to keep row order simple.
    for r in records:
        with Image.open(out / r['local_image_path']) as img:
            vectors.append(image_vector(img))
    captured_at = dt.datetime.now(dt.timezone.utc).isoformat()
    tags = [t.strip() for t in args.tags.split(',') if t.strip()]
    added = 0
    for file in sorted(src.rglob('*')):
        if file.suffix.lower() not in EXTS or not file.is_file():
            continue
        data = file.read_bytes()
        sha = hashlib.sha256(data).hexdigest()
        asset_id = 'VA-' + sha[:12]
        if asset_id in existing_ids:
            continue
        with Image.open(file) as img:
            img.load(); width, height = img.size
            ext = '.jpg' if file.suffix.lower() == '.jpeg' else file.suffix.lower()
            dst = originals / f'{asset_id}{ext}'
            if not dst.exists(): shutil.copy2(file, dst)
            thumb = thumbs / f'{asset_id}.jpg'
            save_thumb(img, thumb)
            vec = image_vector(img)
        rec = {
            'asset_id': asset_id,
            'title': file.stem,
            'source_name': 'local-user-provided',
            'source_page_url': '',
            'original_image_url': '',
            'local_image_path': str(dst.relative_to(out)),
            'local_thumbnail_path': str(thumb.relative_to(out)),
            'width': width,
            'height': height,
            'file_ext': ext,
            'sha256': sha,
            'captured_at': captured_at,
            'tags': tags,
            'category': args.category,
            'visual_notes': 'User-provided/local visual asset ingested for SA&BOO private indexed reference.',
            'rights_status': args.rights_status,
            'usage_allowed': args.usage_allowed,
            'prev_id': None,
            'next_id': None,
            'source_prev_id': None,
            'source_next_id': None,
            'related_ids': [],
            'vector_file': 'vectors.npy',
            'vector_row': None,
        }
        records.append(rec); vectors.append(vec); existing_ids.add(asset_id); added += 1
    write_all(out, records, vectors)
    print(f'Ingested {added} local assets. Total: {len(records)}. Index: {out / "visual_assets.jsonl"}')

if __name__ == '__main__':
    main()
