# Using Visual Asset Index in Other SA&BOO Skills

## Mandatory citation pattern

When output depends on visual references, include:

```text
Asset ID:
Thumbnail:
Original local path:
Source page URL:
Original image URL:
Rights/usage:
How to use it:
```

## Search commands

Default project index:

```bash
INDEX="/Users/bonnie/Documents/学习项目/SA_BOO_Visual_Asset_Index/visual_assets.jsonl"
python /Users/bonnie/.codex/skills/sa-boo-visual-asset-index/scripts/search_visual_assets.py --index "$INDEX" --query "D5 interior warm lighting material" --top 8 --format markdown
```

Image similarity:

```bash
python /Users/bonnie/.codex/skills/sa-boo-visual-asset-index/scripts/search_visual_assets.py --index "$INDEX" --image /path/to/reference.jpg --top 8 --format markdown
```

Rebuild vectors and Markdown report:

```bash
python /Users/bonnie/.codex/skills/sa-boo-visual-asset-index/scripts/rebuild_visual_index.py --out "/Users/bonnie/Documents/学习项目/SA_BOO_Visual_Asset_Index"
```

## Rights reminders

- `reference-only`: internal learning only; do not paste into client/public deliverables.
- `user-provided`: follow project confidentiality and user permission.
- `owned`: can be used according to SA&BOO policy.
- `open-license`: cite license URL.

## Skill routing examples

- Render proposal: search `D5 interior lighting material`, `Enscape walkthrough`, `Twinmotion phasing`.
- Figma Brand Kit: search `Figma brand kit visual system`, `template system`, `brand guidelines`.
- Xiaohongshu cover: search by desired material/style, then use only as composition reference.
- Material database: ingest supplier/product images as `user-provided` or `supplier-reference`.
