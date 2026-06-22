#!/usr/bin/env python3
import json, re, math, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'visual_assets'/'visual_asset_manifest.jsonl'
INDEX=ROOT/'vector_index'/'visual_asset_vectors.json'
DIM=512

def tokens(text):
    text=text.lower()
    words=re.findall(r'[a-z0-9][a-z0-9\-_/]*', text)
    zh=re.findall(r'[\u4e00-\u9fff]', text)
    zh_bigrams=[''.join(zh[i:i+2]) for i in range(len(zh)-1)]
    zh_trigrams=[''.join(zh[i:i+3]) for i in range(len(zh)-2)]
    return words+zh+zh_bigrams+zh_trigrams

def vectorize(text):
    counts={}
    for t in tokens(text): counts[t]=counts.get(t,0)+1
    dense={}
    for t,c in counts.items():
        idx=int(hashlib.sha256(t.encode()).hexdigest(),16)%DIM
        dense[idx]=dense.get(idx,0.0)+(1+math.log(c))
    norm=math.sqrt(sum(v*v for v in dense.values())) or 1
    return {i:v/norm for i,v in dense.items()}

def dot(q, sparse):
    return sum(q.get(i,0.0)*v for i,v in sparse)

def main():
    if len(sys.argv)<2:
        print('Usage: python3 scripts/search_visual_assets.py "query" [top_k]')
        raise SystemExit(2)
    query=sys.argv[1]
    top=int(sys.argv[2]) if len(sys.argv)>2 else 8
    assets={a['id']:a for a in [json.loads(line) for line in MANIFEST.read_text(encoding='utf-8').splitlines() if line.strip()]}
    idx=json.loads(INDEX.read_text(encoding='utf-8'))
    q=vectorize(query)
    rows=[]
    for d in idx['documents']:
        score=dot(q, d['vector'])
        if score>0:
            rows.append((score, assets[d['id']]))
    rows.sort(reverse=True, key=lambda x:x[0])
    for score,a in rows[:top]:
        print(f"{score:.4f}\t{a['id']}\t{a['platform']}\t{a['trend']}")
        print(f"  {a['caption']}")
        print(f"  tags: {', '.join(a.get('prompt_tags',[]))}")
        print(f"  asset: {a['asset_url']}")
        print(f"  source: {a['source_url']}")
if __name__=='__main__': main()
