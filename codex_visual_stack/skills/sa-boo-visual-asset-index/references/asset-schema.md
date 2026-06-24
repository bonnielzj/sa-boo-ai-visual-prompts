# Visual Asset Schema

Each JSONL row should include:

| Field | Meaning |
|---|---|
| asset_id | stable hash/id |
| title | source/page title or assigned title |
| source_name | source label |
| source_page_url | page URL where image was found |
| original_image_url | original image URL at capture time |
| local_image_path | local cached original/reference copy |
| local_thumbnail_path | local thumbnail |
| width / height | pixel dimensions |
| file_ext | extension/content type |
| sha256 | checksum of cached image bytes |
| captured_at | ISO date/time |
| tags | searchable tags |
| category | render, material, brand, interior, lighting... |
| visual_notes | what to learn from this asset |
| rights_status | reference-only, open-license, owned, user-provided, unknown |
| usage_allowed | private-study, client-presentation, public-marketing, etc. |
| prev_id / next_id | linked-list chain |
| related_ids | cross-links for mood/style/material similarity |
| vector_file | where vector data is stored |
| vector_row | row number in vector array |

## Rights status rules

- `reference-only`: third-party copyrighted or unclear license; internal study only.
- `owned`: SA&BOO/user owns or created it.
- `user-provided`: user supplied; follow project confidentiality.
- `open-license`: explicitly licensed; record license URL.
- `public-domain`: only when verified.

## Chain rules

Use two chains when helpful:

1. `source_prev/source_next`: order in source page capture.
2. `curated_prev/curated_next`: SA&BOO curated learning path.
