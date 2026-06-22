#!/usr/bin/env python3
import json, subprocess, re, math, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
manifest=[json.loads(l) for l in (ROOT/'visual_assets'/'visual_asset_manifest.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
cache={r['id']:r for r in json.loads((ROOT/'visual_assets'/'cache'/'cache_manifest.json').read_text(encoding='utf-8'))}

def run(cmd): return subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

def image_average_hash(path):
    # Build a simple 8x8 grayscale-ish hash using sips downsample + raw PPM via macOS Python? Use sips to 8x8 png then parse via built-in tkinter not safe.
    # Fallback perceptual-ish hash: use file bytes + dimensions for stability; not semantic but detects exact asset changes.
    data=Path(path).read_bytes()
    return hashlib.sha256(data).hexdigest()[:32]

def tokens(a):
    text=(a.get('embedding_text') or '') + ' ' + ' '.join(a.get('prompt_tags',[])) + ' ' + a.get('trend','') + ' ' + a.get('platform','')
    text=text.lower()
    en=set(re.findall(r'[a-z0-9][a-z0-9\-_/]*', text))
    zh=set(re.findall(r'[\u4e00-\u9fff]{1,3}', text))
    # include Chinese chars from all text
    chars=re.findall(r'[\u4e00-\u9fff]', text)
    zh.update(chars)
    zh.update(''.join(chars[i:i+2]) for i in range(len(chars)-1))
    return en|zh

nodes=[]
for a in manifest:
    c=cache.get(a['id'],{})
    local_thumb=c.get('thumbnail_path') or ''
    local_orig=c.get('original_path') or ''
    node={
        'id':a['id'],
        'type':'visual_asset' if local_thumb else 'trend_reference',
        'platform':a['platform'],
        'trend':a['trend'],
        'source_url':a['source_url'],
        'asset_url':a['asset_url'],
        'local_thumbnail':local_thumb,
        'local_original_cache':local_orig,
        'cached':bool(c.get('cached')),
        'sha256':c.get('sha256',''),
        'perceptual_hash_proxy':image_average_hash(ROOT/local_thumb) if local_thumb else '',
        'pixel_width':c.get('pixel_width'),
        'pixel_height':c.get('pixel_height'),
        'thumbnail_width':c.get('thumbnail_width'),
        'thumbnail_height':c.get('thumbnail_height'),
        'visual_mechanism':a['visual_mechanism'],
        'sa_boo_translation':a['sa_boo_translation'],
        'prompt_tags':a['prompt_tags'],
        'recommended_use':a['recommended_use'],
        'rights_note':a['rights_note']
    }
    nodes.append(node)

# create linked-list style next/prev within platform + semantic edges by token overlap
edges=[]
from collections import defaultdict
by_platform=defaultdict(list)
for n in nodes: by_platform[n['platform']].append(n)
for platform, ns in by_platform.items():
    ns=sorted(ns,key=lambda x:x['id'])
    for i,n in enumerate(ns):
        if i>0: edges.append({'from':n['id'],'to':ns[i-1]['id'],'type':'prev_in_platform','weight':1.0})
        if i<len(ns)-1: edges.append({'from':n['id'],'to':ns[i+1]['id'],'type':'next_in_platform','weight':1.0})

asset_by_id={a['id']:a for a in manifest}
tok={a['id']:tokens(a) for a in manifest}
for i,a in enumerate(manifest):
    sims=[]
    for b in manifest:
        if a['id']==b['id']: continue
        inter=len(tok[a['id']] & tok[b['id']]); union=len(tok[a['id']] | tok[b['id']]) or 1
        score=inter/union
        if score>0.08: sims.append((score,b['id']))
    for score,bid in sorted(sims,reverse=True)[:5]:
        edges.append({'from':a['id'],'to':bid,'type':'semantic_related','weight':round(score,4)})

# link to prompt docs/recipes by rough tags
recipes={
 'liquid-silver':'03_可直接复制风格口令库.md#01液态银色高级kv',
 'texture-check':'03_可直接复制风格口令库.md#02texture-check-触觉材质高级感',
 'opt-out':'03_可直接复制风格口令库.md#03opt-out-era-克制编辑高级感',
 'reality-warp':'03_可直接复制风格口令库.md#04reality-warp-超现实梦核编辑视觉',
 'drama-club':'03_可直接复制风格口令库.md#05drama-club-电影舞台封面',
 'notes-app':'03_可直接复制风格口令库.md#06notes-app-chic-真实拼贴个人ip',
 'prompt-playground':'03_可直接复制风格口令库.md#07prompt-playground-复古ai界面视觉',
 'victorian':'03_可直接复制风格口令库.md#08维多利亚装饰线稿品牌图形',
 'blueprint':'03_可直接复制风格口令库.md#09技术蓝图产品研发线稿',
 'east-west':'03_可直接复制风格口令库.md#10东方低奢空间叙事'
}
for n in nodes:
    low=(n['id']+' '+n['trend']+' '+' '.join(n['prompt_tags'])+' '+n['sa_boo_translation']).lower()
    for key,target in recipes.items():
        if any(part in low for part in key.split('-')):
            edges.append({'from':n['id'],'to':target,'type':'prompt_recipe_reference','weight':0.7})

graph={'version':'1.0','created':'2026-06-22','description':'Linked visual asset graph: local low-res previews + source references + prompt/semantic edges.','nodes':nodes,'edges':edges}
out=ROOT/'visual_assets'/'asset_graph.json'
out.write_text(json.dumps(graph,ensure_ascii=False,indent=2),encoding='utf-8')
# linked list markdown
lines=['# Visual Asset Linked List｜视觉资产链表','','> 每个节点包含：本地缩略图、本地缓存、原始来源、趋势标签、SA&BOO转译、相邻/语义关联。','']
for n in nodes:
    lines.append(f"## {n['id']}｜{n['platform']}｜{n['trend']}")
    lines.append('')
    if n['local_thumbnail']:
        lines.append(f"![{n['id']}]({n['local_thumbnail'].replace(' ','%20')})")
        lines.append('')
    lines += [
        f"- 类型：{n['type']}",
        f"- 本地缩略图：`{n['local_thumbnail'] or '暂无；仅趋势/页面节点'}`",
        f"- 本地缓存：`{n['local_original_cache'] or '暂无'}`",
        f"- 来源页：{n['source_url']}",
        f"- 原资产URL：{n['asset_url']}",
        f"- SHA256：`{n['sha256'] or 'n/a'}`",
        f"- pHash proxy：`{n['perceptual_hash_proxy'] or 'n/a'}`",
        f"- 尺寸：{n['pixel_width']}×{n['pixel_height']} → thumb {n['thumbnail_width']}×{n['thumbnail_height']}",
        f"- 视觉机制：{n['visual_mechanism']}",
        f"- SA&BOO转译：{n['sa_boo_translation']}",
        f"- 标签：{', '.join(n['prompt_tags'])}",
    ]
    related=[e for e in edges if e['from']==n['id'] and e['type'] in ('next_in_platform','prev_in_platform','semantic_related')][:8]
    if related:
        lines.append('- 链接：' + '; '.join([f"{e['type']}→`{e['to']}`({e['weight']})" for e in related]))
    lines += ['','---','']
(ROOT/'visual_assets'/'visual_asset_linked_list.md').write_text('\n'.join(lines),encoding='utf-8')
print('nodes',len(nodes),'edges',len(edges),'cached',sum(1 for n in nodes if n['cached']))
