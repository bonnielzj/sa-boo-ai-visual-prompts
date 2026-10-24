#!/usr/bin/env python3
"""Audit a SA&BOO reference image library for count, metadata, suspicious sources, and baseline QA.
Usage: python audit_reference_library.py /path/to/<theme参考图>
"""
from __future__ import annotations
import json, sys, csv, collections, re
from pathlib import Path

SUSPICIOUS_HOST_PATTERNS = [
    r'pinterest', r'pinimg', r'craiyon', r'freepik', r'shutterstock', r'istock', r'depositphotos', r'dreamstime',
    r'amazon', r'alibaba', r'1688', r'made-in-china', r'temu', r'etsy', r'ebay', r'walmart'
]
SUSPICIOUS_TEXT_PATTERNS = [
    r'supplier', r'factory', r'wholesale', r'for sale', r'posm', r'planogram', r'supermarket', r'warehouse',
    r'grocery', r'trade show booth', r'exhibition booth', r'3d model', r'mockup', r'AI generated', r'普通货架',
    r'厂家', r'供应商', r'批发', r'超市', r'仓储'
]
REQUIRED_FIELDS = [
    'asset_id','title','source_page_url','original_image_url','local_image_path','local_thumbnail_path',
    'captured_at','tags','category','quality_notes','rights_status'
]
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.tif', '.tiff'}


def image_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS]

def load_rows(base: Path):
    p = base / 'index' / 'visual_assets.jsonl'
    if not p.exists():
        p = base / 'index' / 'visual_assets.json'
    if not p.exists():
        raise SystemExit(f'Missing visual asset index under {base}/index')
    if p.suffix == '.jsonl':
        return [json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]
    return json.loads(p.read_text(encoding='utf-8'))

def host(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url or '').netloc.lower()

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: audit_reference_library.py /path/to/reference-library')
    base = Path(sys.argv[1]).expanduser().resolve()
    rows = load_rows(base)
    images = image_files(base / 'images')
    thumbs = image_files(base / 'thumbs')
    missing = []
    suspicious = []
    rights_bad = []
    for r in rows:
        miss = [f for f in REQUIRED_FIELDS if f not in r or r.get(f) in (None, '')]
        # prev_id/next_id may be null at chain endpoints, but fields should exist.
        for f in ['prev_id','next_id']:
            if f not in r:
                miss.append(f)
        if miss:
            missing.append({'asset_id': r.get('asset_id'), 'missing': sorted(set(miss))})
        h = host(r.get('source_page_url') or r.get('original_image_url'))
        text = ' '.join(str(r.get(k,'')) for k in ['title','source_page_url','original_image_url','quality_notes']).lower()
        if any(re.search(p, h, re.I) for p in SUSPICIOUS_HOST_PATTERNS) or any(re.search(p, text, re.I) for p in SUSPICIOUS_TEXT_PATTERNS):
            suspicious.append({'asset_id': r.get('asset_id'), 'source': h, 'title': r.get('title','')[:120]})
        if r.get('rights_status') != 'reference-only':
            rights_bad.append({'asset_id': r.get('asset_id'), 'rights_status': r.get('rights_status')})
    counts = collections.Counter(host(r.get('source_page_url') or r.get('original_image_url')) for r in rows)
    report = {
        'library': str(base),
        'rows': len(rows),
        'images': len(images),
        'thumbs': len(thumbs),
        'host_counts': counts.most_common(30),
        'missing_metadata_count': len(missing),
        'suspicious_count': len(suspicious),
        'rights_bad_count': len(rights_bad),
        'missing_metadata_sample': missing[:20],
        'suspicious_sample': suspicious[:30],
        'rights_bad_sample': rights_bad[:20],
    }
    out = base / 'index' / 'qa_audit_report.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if len(rows) != len(images) or len(rows) != len(thumbs):
        sys.exit(2)
    if missing or rights_bad:
        sys.exit(3)

if __name__ == '__main__':
    main()
