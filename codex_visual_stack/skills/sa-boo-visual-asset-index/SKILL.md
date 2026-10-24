---
name: sa-boo-visual-asset-index
description: SA&BOO visual asset citation and local image-cache workflow. Use only when the user asks to preserve or cite source visuals, avoid dead URLs, create a reusable image/reference library, build a moodboard index, or create a searchable visual asset chain. Do not use for a supplied reference, a clear visual edit, ordinary design approval, or a one-off shortlist that does not need persistent indexing.
---

# SA&BOO Visual Asset Index

## Scope boundary

- Activate this workflow only when visuals must persist as cached, cited, tagged,
  linked, or searchable assets. It is infrastructure for a requested library, not
  a prerequisite for ordinary SA&BOO design work.
- When this skill is properly triggered, let actual visuals lead the indexed
  evidence and use text to summarize, compare, decide, and translate.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not turn a quick shortlist or accepted design result
  into a database. For a formal indexed output, include only the metadata needed
  for retrieval, provenance, rights, and the stated handoff.

Do not infer a persistent-library request merely because a task includes images,
design learning, research, style, a proposal, a prompt, rendering, or review.

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
- lightweight local features for coarse retrieval; name the actual feature method
  and never imply semantic embeddings when only color/edge/aspect statistics exist
- evidence role: `PROJECT_EVIDENCE`, `PUBLISHED_CLAIM`, `SPATIAL_PROOF`,
  `OPERATING_PROOF`, `AESTHETIC_REFERENCE`, or `GENERATED_HYPOTHESIS`
- project stage and the decision the asset can or cannot support

Do not mix these evidence roles in one undifferentiated moodboard. A generated
image must never be indexed as operating proof, and a published project image
must record what it cannot prove.

## Runtime and layout preflight

Use an interpreter whose NumPy and Pillow imports have been verified; do not assume macOS `/usr/bin/python3` is compatible with Hermes packages.

```bash
HERMES_ROOT="${HERMES_HOME:-$HOME/.hermes}"
PY="$HERMES_ROOT/hermes-agent/venv/bin/python"
if [ ! -x "$PY" ]; then PY="$(command -v python3.11)"; fi
"$PY" -c 'import numpy, PIL'
```

The bundled capture/ingest/rebuild scripts use a **staging index layout**: `originals/`, `thumbs/`, and index/vector files at the output root. This is valid for local retrieval, but it is not the final Premium Curator library contract. When handing accepted references to `sa-boo-premium-reference-curator`, normalize selected assets into `images/`, `thumbs/`, and `index/`; preserve source fields and rights status; add a human curatorial `quality_notes`; then build and inspect the contact sheet and run the Curator audit. Never overwrite an approved reference library in place.

## Workflow

1. **Create or update asset index**
   - Use `scripts/capture_visual_assets.py` with a seed JSON of source pages.
   - Store outputs in a project-owned cache such as `<project>/assets/visual_cache/`, or in the designated reference-library root. This directory is created per project; it is not a bundled skill asset.

2. **Use legal/ethical cache policy**
   - Treat cached third-party images as private study/reference material unless license permits reuse.
   - Do not use cached images as client deliverables or public marketing without permission.
   - Keep source attribution and rights notes next to every cached image.

3. **Build the linked list**
   - Each asset gets `prev_id` and `next_id` by source order.
   - Use `asset_chain.json` to browse references in sequence.
   - Use tags and `related_ids` for cross-topic relationships.

4. **Build lightweight retrieval**
   - The bundled scripts currently use RGB histograms, channel statistics, a simple
     gradient histogram, luminance/contrast, aspect ratio, and hashed metadata tokens.
     They are useful for coarse candidate retrieval, not semantic image understanding.
   - Use `scripts/search_visual_assets.py` to search by explicit tags/text overlap or
     coarse visual similarity. Do not call these vectors CLIP, embeddings, or proof of
     shared design logic.

5. **Use with other SA&BOO skills**
   - For render standards: attach source render references to lighting/material/camera notes.
   - For material/supplier DB: attach material sample photos, catalog covers, and supplier images.
   - For Figma Brand Kit: attach original brand system references and local thumbnails.
   - For trend radar: every trend signal should have at least one visual asset record.

6. **Measure corpus patterns when the task is aesthetic accumulation**
   - Read the Premium Curator's
     `references/corpus-pattern-synthesis.md` before interpreting a collection.
   - Run `scripts/analyze_visual_corpus.py` on the canonical image folder, optionally
     passing its catalog and OCR directory. It writes bounded deterministic metrics,
     cluster representatives, and a compact report without modifying source images.
   - Measurements may cover Lab color, saturation, luminance/contrast, palette,
     edge/detail density, aspect ratio, spatial concentration, and OCR text area when
     bounding boxes are available. Record unavailable fields as unavailable; do not
     estimate them from prose.
   - Cluster output is a review aid. The Premium Curator must inspect representative
     full images and combine measurements with visible mechanism labels and Bonnie's
     acceptance/rejection state before deriving a reusable design method.
   - Re-run only after a meaningful new batch or when a current design question needs
     comparison. Do not append a corpus report to every local edit or daily poster.


## Premium curation standard

When the asset library is for Bonnie's design inspiration or 审美积累, use `sa-boo-premium-reference-curator` as the quality layer above this indexing workflow. It applies across product design, brand/VI/packaging/KV, interiors, furniture, props, retail, signage, and rendering references.

When the current task actually stores or retrieves aesthetic feedback, read
[aesthetic-learning-loop.md](../sa-boo-premium-reference-curator/references/aesthetic-learning-loop.md).
Do not load this indexing skill merely because Bonnie approved a result; keep the
result in its existing project record unless a reusable library is requested.
Keep the existing asset schema: reference the project decision record from
`quality_notes`, and retain the original asset ID/path and rights status. Store
the scoped lesson in that decision record, not a parallel asset database. Verify
that any ingest/export script preserves the note/link before claiming it saved.
Similarity features can retrieve candidates; they cannot infer taste approval.
Rejected images may remain as review evidence but must be excluded from active
masters and positive generation-reference selections. Read-only review remains
read-only; no automatic global-memory writes or background collection.

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
