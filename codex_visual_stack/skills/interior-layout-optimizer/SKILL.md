---
name: interior-layout-optimizer
description: >-
  Residential interior floor-plan layout optimization with CAD/MCP accuracy gates and SABOO SC071 asset-library vector retrieval. Use when Codex needs to critique, optimize, redraw, compare, or propose apartment/flat/duplex/villa layouts; audit DWG/DXF/PDF/image plans; use cadq, AutoCAD MCP, CAD↔SketchUp bridge, dimensions, layers, walls, doors, windows, wet areas, storage, circulation, clearances, public/private zoning, kitchen/bath/core relations, suites, +1 rooms, and source cases. Must not make random changes from blurry images; CAD/DWG/DXF/PDF dimensions and non-movable constraints are the source of truth. Must follow SA&BOO visual-first rule with measurable plan evidence, not vague diagrams.
---

# Interior Layout Optimizer

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

## CAD / MCP accuracy-first doctrine

Use this skill to optimize residential interior floor plans with **CAD/MCP-backed accuracy** and source-backed reasoning from the SABOO SC071 asset library. The optimizer must not behave like a loose concept generator.

Hard rules:

- **CAD or measured baseline is the source of truth.** Prefer DWG/DXF/PDF with known dimensions. If only an image exists, mark all dimensions as uncertain and ask for at least one known dimension before precise optimization.
- **Do not make random redlines from blurry images.** A blurred plan can support discussion only, not accurate wall moves, cabinet depths, door swings, or construction decisions.
- **Use CAD-related tools when accuracy matters.** Pair with `cadq` for DWG/DXF semantic/spatial queries, `autocad-drafting` for AutoCAD MCP drawing/editing/dimensions, and `sa-boo-cad-sketchup-bridge` when the plan must proceed into SketchUp white modeling.
- **Separate facts from proposals.** Facts include dimensions, walls, shafts, beams, columns, windows, doors, plumbing/wet zones, load-bearing constraints, and existing furniture/client requirements. Proposals include layout moves and design options.
- **SC071 cases are precedents, not permission.** Retrieved cases can inspire strategies or warn against pitfalls, but they cannot override actual CAD constraints.
- **Every layout option must pass a practical checklist**: circulation width, door conflicts, furniture scale, storage depth, wet-area feasibility, structural boundaries, daylight/ventilation, privacy, and maintenance.

If precision is required and no usable CAD/PDF/known dimension exists, stop at **conceptual strategy** and label it clearly:

```text
准确性状态：概念级，未到施工/建模级
缺少：DWG/DXF/PDF 或至少一个已知尺寸
下一视觉检查点：可量测平面 / CAD top view / DXF ingest report
```

## Mandatory CAD accuracy workflow

Before proposing layout changes, choose the correct evidence route:

```text
Route 1 — DWG/DXF available
- Use `cadq` to ingest/query semantic or spatial facts when needed.
- Use AutoCAD MCP via `autocad-drafting` to open, inspect, dimension, annotate, redraw, or export when drawing edits are required.
- Record units, extents, known dimensions, layers, walls, doors/windows, fixed cores, wet areas, shafts, and structural constraints.

Route 2 — PDF available
- Use PDF as measured/visual baseline; extract or verify scale where possible.
- If precision is needed, convert/trace to CAD or request DWG/DXF.
- Do not overclaim exact dimensions from an unscaled screenshot.

Route 3 — image/screenshot only
- Use only for early diagnosis and concept discussion.
- Require one known dimension before clearances, furniture fit, or wall moves become precise.
- Mark uncertain zones and avoid construction-level claims.

Route 4 — no plan visual
- Ask for plan/CAD/PDF/screenshot or produce only an input checklist.
```

Minimum baseline facts to extract before serious optimization:

```text
- Units / scale / known dimension
- External wall boundary and usable area
- Structural walls / columns / beams / shafts
- Wet areas and plumbing constraints
- Door and window openings + swing directions
- Existing kitchen/bath/core locations
- Ceiling/beam constraints if relevant
- Household structure and storage/lifestyle priorities
```

## Tool routing for accurate plans

```text
Need to ask “what exists in this DWG/DXF?” → use cadq.
Need to create/edit/dimension CAD geometry → use autocad-drafting / AutoCAD MCP.
Need to move from CAD to SketchUp white model → use sa-boo-cad-sketchup-bridge.
Need residential layout reasoning/SC071 precedents → use interior-layout-optimizer.
Need visual proposal/render after plan is verified → use sa-boo-sketchup-interior-director.
```

Do not call CAD tools for superficial decoration. Call them when they improve measurement, constraints, drawing truth, or downstream modeling accuracy.

## Mandatory source-backed workflow

1. **Read the task inputs first**: area, household, room target, lifestyle priorities, non-movable constraints, and any uploaded plan/image/PDF/CAD file. Classify the evidence as DWG/DXF, PDF, image-only, or no-plan.
2. **Run CAD accuracy checks before design options** when precision matters: units/scale, known dimensions, structural walls/columns, wet zones, shafts, windows/doors, door swings, and furniture clearance. Use `cadq`, AutoCAD MCP, or CAD↔SketchUp bridge when available and relevant.
3. **Retrieve source references before proposing**. Run `scripts/query_index.rb` against the vectorized index and cite the returned source paths.
   - Similar cases: `scripts/query_index.rb --query "<area + type + goals>" --scope both -n 8`
   - Positive references: add `--quality positive`.
   - Pitfall references: add `--quality negative`.
   - Filter when known: `--typology 平层|复式|别墅|大平层|异型平层`, `--area-min`, `--area-max`, `--rooms`.
4. **Load the appropriate references**:
   - Read `references/cad-accuracy-workflow.md` when a DWG/DXF/PDF/image plan must be measured, audited, redrawn, or routed through CAD/MCP tools.
   - Read `references/layout-optimization-logic.md` for design heuristics, pattern language, and evaluation rubric.
   - Read `references/source-index.md` when you need index schema, source statistics, high-signal study sets, or citation rules.
5. **Use retrieved assets as evidence**, not decoration. In final/design notes, cite at least 3 source cases/assets when the user asks for optimization ideas, and separate positive precedents from反例/避坑.
6. **Do not claim the vector index is the original drawing**. It is a retrieval layer over the source assets. If precise dimensions are needed, inspect the original image/DWG/PDF path returned by the query.

## Output structure for layout optimization

Prefer this structure unless the user requests another format:

1. **准确性状态 / CAD baseline**: evidence type, units/scale, known dimensions, fixed constraints, uncertain zones, and whether the plan is concept-level or modeling/construction-level.
2. **现状诊断**: immutable constraints, wasted area, bad adjacencies, circulation conflicts, daylight/ventilation, storage, privacy, wet-area/core issues, door conflicts, furniture clearance.
3. **CAD/MCP证据**: cadq/AutoCAD/PDF/image findings, dimensions or handles/layers when available, and what cannot be inferred.
4. **源资产召回**: list comparable SC071 cases/assets with local paths or SMB URLs and why each is relevant; separate positive precedents from pitfalls.
5. **优化策略**: 2-4 concept options, each with measurable layout moves, pros/cons, risk points, and what not to move.
6. **推荐方案**: one preferred option with implementation sequence and required CAD/SU next action.
7. **校验清单**: circulation width, furniture scale, storage depth, wet-area feasibility, door swings, public/private boundary, daylight/ventilation, structure/plumbing risk, buildability.

## Bad-layout-output firewall

Reject or downgrade outputs that show:

- random wall/furniture moves without scale or constraint evidence;
- redlines drawn over unreadable screenshots;
- missing door swings, cabinet depth, toilet/shower clearance, or circulation width;
- moving wet areas, shafts, structural walls, or exterior openings without evidence;
- using SC071 precedents as if they were this project's actual CAD;
- proceeding to SketchUp/rendering before A01 plan checks pass.

If blocked by missing data, produce a precise request instead of inventing:

```text
缺少用于准确优化的资料：
1. DWG/DXF or scaled PDF
2. one known dimension if only image is available
3. non-movable walls/shafts/wet zones
4. household and storage requirements
下一步：先做 B00 原始基准 / CAD top-view proof
```


## Index maintenance

- Current source root: `/Volumes/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+`.
- If the SMB library changes or is remounted elsewhere, rebuild: `ruby -EUTF-8:UTF-8 scripts/build_index.rb --source "<mounted source path>" --out assets/index`.
- Main index files: `assets/index/cases.jsonl`, `assets/index/assets.jsonl`, `assets/index/manifest.json`.
- Contact sheets for quick visual orientation live in `assets/index/contact_sheets/`.
