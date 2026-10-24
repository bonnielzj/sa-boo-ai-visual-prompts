# Premium reference baseline and source map

## Project-specific reference baselines

Use the current user's designated library and scoped acceptance/rejection labels.
Record its actual location in the private project, not in a public skill package.
Choose props, retail, signage, product, or brand sources according to the brief;
this package includes neither a private corpus nor inherited aesthetic approval.

## Source priority

P0 final sources:
- brand official: Prada Group, Gentle Monster, Jacquemus, Dior, Louis Vuitton, Loewe, Bottega Veneta, Burberry, etc.
- studios/designers: Random Studio, Crosby Studios, Snarkitecture, OMA/AMO, Masquespacio, Yinka Ilori, India Mahdavi.
- design media: Frame, Superfuture, Dezeen, Designboom, Retail Design Blog, Yellowtrace, Wallpaper, gooood, ArchDaily, Design Milk, The Spaces, Interior Design Magazine, Hypebeast/Hypebae/WWD when they show actual spaces.

P1 good if filtered:
- Behance project pages with authorship, multiple high-resolution images, real spatial/project thinking, and no generic AI/render dump.

P2 discovery leads:
- Pinterest, Instagram, DINZD, Designwire, 公众号, 小红书 screenshots/exports. Use to find project names and source trails; avoid making them the majority of final sources unless no better source exists.

## Hard rejection taxonomy

Reject or quarantine:
- supplier, factory, wholesale, e-commerce, Amazon, Alibaba, 1688, Made-in-China;
- POSM, planogram, supermarket/grocery/warehouse shelving, generic retail racks;
- trade-show booths and ordinary exhibition systems;
- low-resolution, blurry, heavy watermark, compressed, blank, pure text boards;
- stock/mockup/AI-looking images, low-grade 3D renders;
- restaurants/cafes/offices/residential images when not requested;
- runway/showspace images unless the spatial set has clear commercial/interior inspiration value.

## Minimum file contract

Every approved collection should contain:

```text
images/
thumbs/
index/visual_assets.jsonl
index/visual_assets.json
index/sources.csv
index/asset_chain.json
_contact_sheet_01.jpg ...
_<主题>_总览.jpg
README.md
_scripts/  # optional, preserve useful gather/download scripts
```

Every asset record should preserve:

```text
asset_id
seq
title
source_name
source_page_url
original_image_url
local_image_path
local_thumbnail_path
width / height
sha256
captured_at
tags
category
visual_notes
quality_notes
rights_status = reference-only
usage_allowed = private-study/internal-reference only
prev_id / next_id
```

## Design MCP contract

Future design MCP/retrieval tools should not return only vague text inspiration. They should expose:
- `asset_id`
- `thumbnail_path`
- `local_original_path`
- `source_page_url`
- `original_image_url`
- `category/tags`
- `rights_status`
- `quality_notes`
- similarity/search score when relevant

For design generation/modeling tools, selected references must be translated into: form language, material, color, scale, lighting, circulation, construction feasibility, and render/CAD/SU instructions.

## All-design-domain extension

Apply source-backed reference selection to **product design and brand design**, as well as interiors/furniture. For every domain, preserve the same chain:

```text
brief/sample → source hierarchy → aesthetic rejection → local cache/index → contact-sheet QA → design translation
```

### Product design searches

Prioritize official/design-media/project sources for:
- product form, CMF, material research, packaging structure, accessories, jewelry, devices, furniture-object crossover, line-art/blueprint references;
- source anchors: Dezeen, Designboom, Wallpaper, Core77, Yanko Design, Design Milk, Behance curated product projects, brand official launch pages, studio portfolios, museum/archive pages when useful;
- reject generic Amazon/Alibaba product photos, supplier catalogs unless sourcing is explicitly requested, low-grade 3D renders, patent-looking junk diagrams without aesthetic value.

### Brand / visual identity searches

Prioritize project depth and system thinking:
- visual identity, logo/core-symbol, typography, grid, art direction, packaging, campaign/KV, social templates, environmental graphics, motion identity;
- source anchors: Behance curated projects, BP&O, Brand New/UnderConsideration, It’s Nice That, The Brand Identity, Mindsparkle Mag, Design Week, Dieline, Packaging of the World, studio portfolios, brand guideline PDFs where publicly available;
- reject logo-template dumps, AI-logo sites, generic Canva templates, low-grade mockup-only projects, untraceable Pinterest-only images, fake brand boards with no system quality.

### Translation requirements

- Product: convert references into silhouette, part breakdown, CMF, material/process, ergonomics, scale, exploded/blueprint view, prototype or render prompt.
- Brand: convert references into visual mother motif, symbol construction, typography/grid, color/material/image style, packaging/KV/social/deck applications.
- Space: convert references into circulation, thresholds, display hierarchy, focal nodes, material/lighting, CAD/SU/render actions.
