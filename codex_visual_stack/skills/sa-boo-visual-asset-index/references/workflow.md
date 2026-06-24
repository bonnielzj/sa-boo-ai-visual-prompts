# Visual Asset Index Workflow

## Capture sources

Use seed JSON:

```json
[
  {
    "source_name": "D5 Interior Solution",
    "source_page_url": "https://www.d5render.com/solutions/interior",
    "category": "render/interior",
    "tags": ["D5", "interior", "lighting", "material"],
    "rights_status": "reference-only"
  }
]
```

Run:

```bash
python scripts/capture_visual_assets.py --seeds assets/seed_sources.json --out assets/visual_cache --max-total 40
```

## Search

Text/tag search:

```bash
python scripts/search_visual_assets.py --index assets/visual_cache/visual_assets.jsonl --query "warm stone interior lighting before after"
```

Image similarity search:

```bash
python scripts/search_visual_assets.py --index assets/visual_cache/visual_assets.jsonl --image path/to/reference.jpg
```

## Use in deliverables

For research reports, include:

```text
Asset ID:
Thumbnail/local path:
Source page:
Original image URL at capture:
Rights:
What this teaches:
```

For public/client work, do not paste third-party cached images unless licensed. Use them to guide original design, AI prompts, or internal analysis.
