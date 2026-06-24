---
name: sa-boo-visual-asset-index
description: SA&BOO visual asset citation and local image cache workflow for design learning, trend research, material references, render references, brand kit references, and vector-like search. Use when the user asks to preserve original visual assets, avoid dead URLs, create image/reference libraries, cite source images, build moodboard/reference indexes, capture D5/Enscape/Twinmotion/Figma/brand/material visuals, or create searchable/linked visual asset chains for skills and project knowledge. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Visual Asset Index

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Use this skill whenever learning/research needs **actual visual references**, not only text. Every visual learning item should have a locally cached image, source attribution, rights status, tags, and a searchable index.

## Core rule

Do not rely only on live URLs. For each visual reference, store:

- local cached image path
- local thumbnail path
- source page URL
- original image URL
- capture date
- title / description / tags
- copyright/license status
- hash/checksum
- `prev_id` / `next_id` for chain browsing
- vector-like features for retrieval

## Workflow

1. **Create or update asset index**
   - Use `scripts/capture_visual_assets.py` with a seed JSON of source pages.
   - Store outputs in `assets/visual_cache/` or a project-specific folder.

2. **Use legal/ethical cache policy**
   - Treat cached third-party images as private study/reference material unless license permits reuse.
   - Do not use cached images as client deliverables or public marketing without permission.
   - Keep source attribution and rights notes next to every cached image.

3. **Build the linked list**
   - Each asset gets `prev_id` and `next_id` by source order.
   - Use `asset_chain.json` to browse references in sequence.
   - Use tags and `related_ids` for cross-topic relationships.

4. **Build vector-like retrieval**
   - The script stores `vectors.npy` and `vector_index.json` using image color/contrast/edge/aspect features.
   - Use `scripts/search_visual_assets.py` to search by text tags or by visual similarity to another image.

5. **Use with other SA&BOO skills**
   - For render standards: attach source render references to lighting/material/camera notes.
   - For material/supplier DB: attach material sample photos, catalog covers, and supplier images.
   - For Figma Brand Kit: attach original brand system references and local thumbnails.
   - For trend radar: every trend signal should have at least one visual asset record.

## Output pattern

```text
视觉资产库：
缓存位置：
索引文件：
已捕获数量：
链表入口：
可检索字段：
版权/使用限制：
下一步：
```

## Quality bar

- Prefer source pages with stable attribution: official galleries, product docs, vendor catalogs, design media pages.
- Store metadata even if image download fails.
- Avoid private/social scraping unless the user provides screenshots or exports.
- Use thumbnails in previews; keep original cache for internal reference.
