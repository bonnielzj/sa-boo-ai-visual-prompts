---
name: sa-boo-furniture-textile-softdecor
description: SA&BOO furniture, textile, soft-decoration, FF&E, styling, and interior object knowledge system. Use when Codex needs to learn, research, specify, compare, audit, source, model, tag, draw, render, or present furniture, upholstery, curtains, rugs, bedding, cushions, lighting/decor objects, system furniture, full-home custom cabinetry, wardrobes, walk-in closets, kitchens, wall panels, modular storage, textile materials, furniture history/styles, official high-end furniture brand websites and downloads such as Baxter, Cassina, Minotti, Vitra, Artek, B&B Italia, Poliform, CAD/SKP/DWG/Revit/BIM/3D product assets, supplier/product data, museum/open-source/GitHub references, local visual assets, CAD blocks, SketchUp components, FF&E schedules, procurement notes, or Bonnie's evolving aesthetic logic. Must apply SA&BOO visual-first doctrine and connect furniture knowledge to CAD, SketchUp, materials, budgets, renders, and client-facing proposals.
---

# SA&BOO Furniture / Textile / Soft Decor Knowledge

Use this skill to turn furniture, textile, and soft-decoration work into a **visual-first, reusable co-design system** rather than generic prose. The output should help SA&BOO choose, critique, model, draw, render, price, and present FF&E with taste, construction awareness, and source traceability.

## Co-design, not copywriting

Act as Bonnie's design partner, not a text generator. The purpose of skills, MCP tools, warehouse resources, official brand sources, GitHub/open assets, CAD/SU files, and visual indexes is to produce better design decisions and visual/technical artifacts. Text is only the record of evidence, reasoning, decisions, and next actions.

For substantial design tasks, push toward tangible outputs: visual asset chains, moodboards, product/source cards, CAD blocks/layers, SketchUp component plans, material boards, FF&E schedules, render prompts, camera lists, annotated QA, or proposal pages. Do not stop at generic paragraphs when an asset, model, drawing, table, or visual checkpoint can move the design forward.


## Proactive database invocation rule

Do not wait for Bonnie to explicitly ask to use the furniture/textile/soft-decor database. Whenever a task involves furniture, textile, upholstery, curtain, rug, bedding, styling objects, system furniture, FF&E, sourcing, CAD furniture blocks, SketchUp components, render styling, material boards, proposal selections, or procurement/spec decisions, proactively consult and update the local database when useful:

```text
/Users/bonnie/Documents/学习项目/sa-boo-design-knowledge-base/03-databases/furniture-textile-softdecor/
```

Minimum active lookup order:

1. `sources.csv` — official brand/source/download/rights intelligence.
2. `objects.csv` — known furniture/object cards, dimensions, materials, CAD/SU/render notes.
3. `textiles.csv` — textile fibers, performance, cleaning, certifications, tactile notes.
4. `cad_su_assets.csv` — downloaded/model asset paths, units, scale, LOD, tags/layers, quality notes.
5. `aesthetic_notes.csv` — Bonnie/SA&BOO aesthetic memory, what worked, what to avoid.

Use the database in three ways:

- **Read before deciding**: cite existing records when a decision can reuse prior knowledge.
- **Write after learning**: when a new official source, product family, textile, CAD/SU asset, or aesthetic rule is discovered, add or propose a row instead of leaving it in chat only.
- **Flag gaps**: if the database lacks the needed object/source/textile/model, state the missing row and the next capture/search action.

For quick tasks, mention only the relevant database fact. For substantial design work, include a short `数据库调用` section with file(s) consulted, matching records, missing records, and proposed updates.

## Governing rule

Follow `sa-boo-visual-first-core` before long explanation:

- Build or cite a high-quality visual asset chain for furniture/textile/soft decor judgment.
- Use `sa-boo-visual-asset-index` when collecting, caching, tagging, or searching visual references.
- Treat third-party images/models as private study/reference unless a license explicitly allows reuse.
- Text must interpret visible evidence: proportion, material, construction, tactility, style lineage, placement, scale, maintenance, procurement risk.
- Do not accept empty “高级感” language. Name what creates quality.
- Buildability is equal to visual quality: verify CAD/SU scale, dimensions, clearances, layers/tags, model hygiene, and construction/spec boundaries whenever a design is meant to land.

## Rapid skill/tool dispatch

When a task can benefit from better design taste, standards, CAD/SU quality, materials, or proposal polish, read `references/rapid-skill-router.md` and use the smallest effective combination that still preserves quality: **1 primary skill + necessary support skills + required QA**. Do not wait for Bonnie to name every tool; do not omit a needed skill just to look efficient.


## Quality over speed rule

Efficiency is a coordination method, not a quality permission slip. Lightweight routing means fewer unnecessary tools, not lower standards. Never use speed, token economy, or “minimum skill set” as a reason to skip visual evidence, official source checks, dimension verification, material logic, CAD/SU hygiene, aesthetic critique, or delivery QA.

If the fast path cannot preserve quality, slow down and state which additional evidence, skill, source, drawing, model, or QA gate is required.

## Quick routing

Read only the reference file that matches the task:

- **Knowledge architecture / study plan / taxonomy** → `references/knowledge-map.md`
- **Sofas, chairs, tables, storage, beds, casegoods, lighting/decor** → `references/furniture-taxonomy.md`
- **Ergonomics / golden ratio / classical proportion / human-scale QA** → `references/ergonomics-proportion-classics.md`
- **System furniture / 全屋定制 / 厨柜衣柜系统** → `references/system-furniture-custom-cabinetry.md`
- **Upholstery, curtain, rug, bedding, leather, fiber, weave, performance** → `references/textile-softdecor-materials.md`
- **Aesthetic critique, style logic, Bonnie/SA&BOO taste calibration** → `references/aesthetic-logic.md`
- **CAD blocks, SketchUp components, render assets, model hygiene** → `references/cad-sketchup-bridge.md`
- **P0 official furniture brands / open-source / museum / GitHub / supplier / standards sources** → `references/source-map.md`
- **Official brand study cycle / Baxter-Cassina-Minotti etc.** → `references/official-brand-cycle.md`
- **Fast skill/tool routing for design quality** → `references/rapid-skill-router.md`
- **Co-design operating protocol / not copywriting** → `references/co-design-operating-protocol.md`
- **FF&E schedules, procurement, pricing, certification, maintenance** → pair with `sa-boo-material-supplier-budget-db`; use `assets/ffe_knowledge_schema.csv` as a starter schema.


## Residential furniture and storage modeling gate

For small residential CAD/SU schemes, do not place generic boxes and call them furniture. Before modeling or rendering major furniture/storage, check:

- human scale and clearances: sofa depth, coffee-table reach, dining pull-out, bed-side passage, wardrobe door/drawer use, desk chair movement;
- function: daily two-person living, occasional guest/work mode, laundry/service pressure, storage categories;
- silhouette and taste: use curated local/official references rather than arbitrary primitives;
- CAD/SU expression level: footprint and clearance first, then simplified component/proxy, then detailed model only if it affects the decision;
- material truth: fabric/wood/stone/metal texture scale and maintenance, not just color.

For Bonnie's local libraries, first make a shortlist/contact sheet and translate references into decisions. Private study references are not automatically client/public assets.

## Core workflow

```text
1. Define use case
   → learning / specification / sourcing / model library / CAD block / SketchUp render / proposal / procurement.

2. Build visual evidence
   → local assets, official product pages, museum archives, open-license libraries, user screenshots, CAD/SU screenshots.
   → record source URL, license/rights, local path, quality notes, and what the asset teaches.

3. Classify object and material
   → furniture type + room + function + dimensions + construction + material + style + supplier/source.

4. Analyze design quality
   → proportion, silhouette, ergonomics, material truth, detail, texture scale, placement, relationship to architecture, longevity.

5. Translate into production
   → CAD layer/block/tag, SketchUp component/tag/material, render prompt, FF&E line item, budget/procurement risk, client wording.

6. Store reusable knowledge
   → update an index, schema, source map, official-brand product/source log, asset chain, or project FF&E schedule instead of leaving knowledge only in chat.
```

## What “learn furniture” means here

Always learn across five linked layers:

1. **Object intelligence** — type, dimensions, ergonomics, proportion systems, construction, joinery, cushion logic, hardware, durability.
2. **Material intelligence** — fiber, weave, finish, texture scale, cleaning, abrasion, flammability, colorfastness, emissions, sustainability.
3. **Aesthetic intelligence** — silhouette, era/style lineage, proportion, restraint, tension, rhythm, narrative, anti-generic taste.
4. **Spatial intelligence** — placement, clearance, sightline, adjacency, lighting relationship, scale in CAD/SU.
5. **Delivery intelligence** — source, license, CAD/SU asset quality, lead time, supplier, budget, maintenance, replacement risk.

## Minimum output pattern

```text
视觉主线：
- 输入/引用资产：asset IDs, paths, URLs, rights
- 缺失视觉：what must be captured next

知识判断：
- 类型 / 空间 / 功能：
- 形体比例 / 轮廓：
- 材料 / textile / tactile logic：
- 施工与耐用性：
- 风格谱系与审美判断：

CAD / SketchUp 联动：
- CAD 表达：layer/block/tag/尺寸/符号
- SketchUp 表达：component/tag/material/proxy/detail level
- 渲染表达：texture scale/camera/light/prompt notes

FF&E / 采购：
- source / supplier / license：
- budget / lead time / maintenance / risk：

下一步：
- add to local visual index / source map / FF&E schedule / model library
```

## Quality gates

Reject or mark as weak when:

- the visual is blurry, unattributed, low-resolution, watermarked beyond study usefulness, or irrelevant;
- the furniture scale would break circulation or human use;
- the textile choice ignores cleaning, abrasion, sunlight, pets/children, flame code, or moisture;
- the SketchUp model is too heavy, untagged, wrongly scaled, or uses low-quality textures;
- the CAD block is decorative only and lacks clear footprint, clearance, or tag logic;
- the proposal language praises “luxury” without visible evidence;
- the style is a cliché collage rather than a coherent spatial/material story.

## Tool and skill pairings

- `sa-boo-visual-asset-index`: cache/cite/search visual references.
- `sa-boo-material-supplier-budget-db`: FF&E schedule, supplier scoring, pricing, procurement, certifications.
- `sa-boo-cad-sketchup-bridge`: CAD↔SketchUp handoff and version loop.
- `sa-boo-sketchup-interior-director`: visual-first model, material, camera, render workflow.
- `sa-boo-autocad-construction-standard` + `autocad-drafting`: CAD layer/block/drawing standards.
- `sa-boo-proposal-deck-director`: client-facing furniture/material story and image packs.
- `sa-boo-design-research-radar`: current style/trend scans; always save visual evidence.

## Starter scripts and assets

- `scripts/create_ffe_knowledge_base.py` creates CSV tables for furniture, textile, source, CAD/SU, and aesthetic notes.
- `assets/ffe_knowledge_schema.csv` defines recommended fields for an FF&E knowledge item.
- `assets/source_seeds.json` lists vetted initial sources for visual/source learning; use with visual-asset-index capture tools only when rights are acceptable for private study.
