#!/usr/bin/env python3
"""Cache source-linked visual assets as low-resolution local research previews.

Copyright note:
- By default this script does NOT persist high-resolution third-party originals.
- It stores low-resolution thumbnails for internal research/indexing only.
- Do not treat third-party cached images as owned commercial assets.
"""
import json, urllib.request, urllib.parse, subprocess, re, tempfile, hashlib, argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'visual_assets'/'visual_asset_manifest.jsonl'
CACHE=ROOT/'visual_assets'/'cache'
THUMBS=CACHE/'thumbs'
ORIG=CACHE/'original'
THUMBS.mkdir(parents=True, exist_ok=True)

def safe_ext(url, content_type=''):
    path=urllib.parse.urlparse(url).path.lower()
    for ext in ['.png','.jpg','.jpeg','.webp','.gif']:
        if path.endswith(ext): return ext
    if 'png' in content_type: return '.png'
    if 'jpeg' in content_type or 'jpg' in content_type: return '.jpg'
    if 'webp' in content_type: return '.webp'
    return '.img'

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--keep-original', action='store_true', help='Persist full downloaded originals locally. Avoid committing them unless licensed.')
    args=ap.parse_args()
    if args.keep_original:
        ORIG.mkdir(parents=True, exist_ok=True)
    records=[]
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        a=json.loads(line)
        rec={'id':a['id'],'asset_url':a['asset_url'],'cached':False,'reason':'','original_path':'','thumbnail_path':'','sha256':'','md5':'','pixel_width':None,'pixel_height':None,'thumbnail_width':None,'thumbnail_height':None,'cache_policy':'thumbnail_only_low_res_research_preview'}
        if a.get('asset_kind')!='remote_image_reference':
            rec['reason']='not_remote_image_reference'
            records.append(rec); continue
        url=a['asset_url']
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; SA-BOO research thumbnail cache)','Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'})
            with urllib.request.urlopen(req, timeout=35) as r:
                data=r.read(20_000_000)
                ctype=r.headers.get('content-type','')
            ext=safe_ext(url, ctype)
            if ext=='.img':
                if data[:8].startswith(b'\x89PNG'): ext='.png'
                elif data[:3]==b'\xff\xd8\xff': ext='.jpg'
                elif data[:4]==b'RIFF' and b'WEBP' in data[:20]: ext='.webp'
            rec['sha256']=hashlib.sha256(data).hexdigest()
            rec['md5']=hashlib.md5(data).hexdigest()
            with tempfile.TemporaryDirectory() as td:
                op=Path(td)/f"{a['id']}{ext}"
                op.write_bytes(data)
                info=run(['sips','-g','pixelWidth','-g','pixelHeight',str(op)])
                if info.returncode!=0:
                    rec['reason']='downloaded_but_sips_unreadable: '+info.stderr.strip()[:200]
                    records.append(rec); continue
                m_w=re.search(r'pixelWidth:\s*(\d+)', info.stdout)
                m_h=re.search(r'pixelHeight:\s*(\d+)', info.stdout)
                rec['pixel_width']=int(m_w.group(1)) if m_w else None
                rec['pixel_height']=int(m_h.group(1)) if m_h else None
                tp=THUMBS/f"{a['id']}.jpg"
                conv=run(['sips','-Z','512','-s','format','jpeg',str(op),'--out',str(tp)])
                if conv.returncode!=0:
                    rec['reason']='thumbnail_failed: '+conv.stderr.strip()[:200]
                else:
                    tinfo=run(['sips','-g','pixelWidth','-g','pixelHeight',str(tp)])
                    tw=re.search(r'pixelWidth:\s*(\d+)', tinfo.stdout)
                    th=re.search(r'pixelHeight:\s*(\d+)', tinfo.stdout)
                    rec['thumbnail_width']=int(tw.group(1)) if tw else None
                    rec['thumbnail_height']=int(th.group(1)) if th else None
                    rec['thumbnail_path']=str(tp.relative_to(ROOT))
                    rec['cached']=True
                    rec['reason']='cached_low_res_research_thumbnail'
                if args.keep_original:
                    full=ORIG/f"{a['id']}{ext}"
                    full.write_bytes(data)
                    rec['original_path']=str(full.relative_to(ROOT))
                    rec['cache_policy']='thumbnail_plus_local_original_not_for_redistribution'
        except Exception as e:
            rec['reason']=type(e).__name__+': '+str(e)[:250]
        records.append(rec)
    (CACHE/'cache_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    with open(CACHE/'cache_manifest.jsonl','w',encoding='utf-8') as f:
        for r in records: f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print('cached',sum(1 for r in records if r['cached']),'of',len(records))
    for r in records:
        if r['cached']:
            print('OK',r['id'],r['thumbnail_path'])
        elif r['reason']!='not_remote_image_reference':
            print('SKIP/ERR',r['id'],r['reason'])
if __name__=='__main__': main()
