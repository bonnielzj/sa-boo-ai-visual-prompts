# Rapid Skill Router for Furniture / Textile / Soft Decor / System Furniture

Use this to quickly and efficiently mobilize the skill/tool set that raises SA&BOO design taste, standards, and delivery quality. Efficiency must never reduce quality. Choose the smallest set that can pass the required quality gates; if quality needs more support or QA, add it.

## Maximal useful resource mobilization

- Mobilize all relevant available resources when they improve design quality: SA&BOO skills, CAD/SketchUp skills, MCP tools, warehouse/local assets, official brand downloads, open GitHub repositories, open datasets, supplier pages, standards, and visual indexes.
- "Relevant" means the resource can improve an actual design decision, visual output, model/drawing quality, material/spec accuracy, or delivery standard.
- Do not hoard resources passively. If a warehouse asset, official CAD/SU file, GitHub model/dataset, material texture, or brand scene can sharpen the work, surface it, cite it, and convert it into design action.
- The goal is co-design: options, comparisons, sketches, model/CAD actions, material boards, FF&E schedules, render prompts, and QA — not long-form prose as an end in itself.

## Non-negotiable: efficiency cannot lower quality

- Lightweight routing organizes complexity; it does **not** lower standards.
- Speed is valuable only when it preserves or improves visual evidence, source traceability, dimensions, material logic, CAD/SU hygiene, and delivery QA.
- Do not skip official-source checks, dimensions, material/finish verification, model import hygiene, rights review, aesthetic critique, or client/施工图 quality gates for the sake of being fast.
- If a task cannot be done quickly at SA&BOO quality, say so and name the missing evidence or additional skill/tool needed.
- A "minimal" workflow is only acceptable when it still produces a beautiful, accurate, technically defensible result.

## Buildability / CAD / SketchUp precision gate

For any design that may be implemented, do not stop at visual taste. Add precision checks:

```text
Units confirmed?
Known dimensions verified?
Clearances checked?
CAD layer/block/tag logic defined?
SketchUp component naming/tag/LOD/material slots clean?
Official model/source rights recorded?
Construction vs concept boundary clear?
Site-measure / tolerance / installation risks named?
```

If any answer is unknown, mark it as a risk and define the next CAD/SU verification action.

## Default stance

- Visual-first: use or request visual evidence before long explanations.
- Official-source-first: for furniture/system products, prefer official brand/product/download pages before generic websites.
- Production-aware: every aesthetic decision should connect to CAD, SketchUp, material, FF&E, render, supplier, proposal, and buildability output.
- Fast but not shallow: route quickly, then inspect proportion, materials, dimensions, rights, file quality, buildability, and presentation quality.

## Quick recipes

### 1. Furniture / soft decor selection or critique

```text
Primary: sa-boo-furniture-textile-softdecor
Support: sa-boo-visual-asset-index + sa-boo-material-supplier-budget-db
Optional: sa-boo-proposal-deck-director if client-facing
Read: aesthetic-logic.md + furniture-taxonomy.md
```

Use when selecting sofa/chair/rug/curtain/bedding/decor, comparing brands, or writing FF&E logic.

### 2. Official brand learning cycle

```text
Primary: sa-boo-furniture-textile-softdecor
Support: sa-boo-visual-asset-index + sa-boo-design-research-radar
Optional: sa-boo-material-supplier-budget-db
Read: official-brand-cycle.md + source-map.md
```

Use for Baxter, Cassina, Minotti, Vitra, Artek, B&B Italia, Poliform, and similar brands.

### 3. 全屋定制 / system furniture / kitchens / wardrobes

```text
Primary: sa-boo-furniture-textile-softdecor
Support: sa-boo-cad-sketchup-bridge + sa-boo-material-supplier-budget-db
QA: sa-boo-autocad-construction-standard or sketchup-sketchup-interior-director depending output
Read: system-furniture-custom-cabinetry.md + cad-sketchup-bridge.md
```

Use for Poliform, USM, Molteni&C/Dada, Alias, SieMatic, Bulthaup, Boffi, Valcucine, Rimadesio, Porro, Lema, Modulnova, Cesar, Poggenpohl.

### 4. SketchUp furniture/CAD/SKP/DWG/Revit/BIM asset use

```text
Primary: sa-boo-sketchup-interior-director
Support: sa-boo-furniture-textile-softdecor + sa-boo-cad-sketchup-bridge
QA: sketchup-edge-tools-cleanup or sketchup-solid-inspector-repair if imported geometry is messy/heavy
Read: cad-sketchup-bridge.md + system-furniture-custom-cabinetry.md if cabinetry/system
```

Check: source URL, rights, units, scale, exact dimensions, clearances, component naming, tags, LOD, material slots, polygon weight, proxy strategy, and construction-vs-concept boundary.

### 5. CAD drawing / construction expression

```text
Primary: sa-boo-autocad-construction-standard
Support: sa-boo-furniture-textile-softdecor + sa-boo-cad-sketchup-bridge
Tool: autocad-drafting if drawing creation/editing is requested
Read: cad-sketchup-bridge.md; system-furniture-custom-cabinetry.md for fixed systems
```

Use for blocks, layers, FF&E tags, built-in furniture elevations, module schedules, details, issue standards.

### 6. Material / supplier / budget / FF&E schedule

```text
Primary: sa-boo-material-supplier-budget-db
Support: sa-boo-furniture-textile-softdecor + sa-boo-visual-asset-index
Read: textile-softdecor-materials.md + source-map.md
```

Use for pricing, suppliers, product schedules, maintenance, substitutions, approvals, certificates.

### 7. Client-facing proposal / moodboard / image pack

```text
Primary: sa-boo-proposal-deck-director
Support: sa-boo-furniture-textile-softdecor + sa-boo-visual-asset-index
Optional: sa-boo-east-west-luxury-interior for bilingual premium narrative
```

Use only visually approved/cited assets. Third-party brand imagery stays private/reference unless permission exists.

### 8. Trend scan / aesthetic upgrade

```text
Primary: sa-boo-design-research-radar
Support: sa-boo-furniture-textile-softdecor + sa-boo-visual-asset-index
Read: aesthetic-logic.md + source-map.md
```

Use for current design direction, brand trend, material trend, official brand scene analysis.

### 9. Ergonomics / proportion / classical design common sense

```text
Primary: sa-boo-furniture-textile-softdecor
Support: sa-boo-cad-sketchup-bridge + sa-boo-sketchup-interior-director when dimensions/models matter
Optional: cadq / autocad-drafting for drawing verification
Read: ergonomics-proportion-classics.md + furniture-taxonomy.md
```

Use for human dimensions, clearances, seating/table/desk/kitchen/wardrobe checks, golden ratio, rule of thirds, Modulor, classical order/proportion, grids, and CAD/SU ergonomic QA.

## Decision tree

```text
Is the task about selecting/critiquing furniture or textile?
→ furniture-textile-softdecor primary.

Is it about official brand products/downloads?
→ official-brand-cycle + source-map; record rights and formats.

Is it about kitchens/wardrobes/wall systems/custom cabinetry?
→ system-furniture-custom-cabinetry + cad-sketchup-bridge.

Is it about human dimensions, golden ratio, proportion, or classic design basics?
→ read ergonomics-proportion-classics and translate into CAD/SU checks.

Is there CAD/DWG/DXF or construction drawing output?
→ add autocad-construction-standard; use autocad-drafting when editing/creating CAD.

Is there SketchUp/SKP/3D model/render output?
→ add sketchup-interior-director; run model hygiene checks.

Is there budget/supplier/procurement output?
→ add material-supplier-budget-db.

Is there client presentation output?
→ add proposal-deck-director after visual/source QA.
```

## Speed rules

- If the task is a quick opinion: use 1 primary skill + aesthetic gate only, but still state uncertainty and needed evidence if the visual/source basis is weak.
- If the task touches a real project file: add CAD/SU/material QA.
- If the task uses brand assets: record rights immediately.
- If a model/download is involved: verify units and source before design judgment.
- If visuals are missing: state the next visual checkpoint rather than writing generic advice.
- If quality conflicts with speed: quality wins; add the missing skill, source check, drawing/model QA, or visual checkpoint.

## Design action outputs

Prefer outputs that move design forward:

```text
- visual reference chain / asset IDs / source links
- option comparison matrix
- furniture or system product card
- CAD layer/block/tag plan
- SketchUp component/LOD/material plan
- material and finish board
- FF&E schedule row(s)
- render prompt + camera list
- QA rejection/fix list
- next concrete modeling/drawing/capture step
```

If the response is mostly text, it must explain which visual/model/drawing/table artifact should be produced next.

## Standard output for routed tasks

```text
本轮主 skill：
辅助 skill：
暂不调用：原因

视觉依据：
审美/标准判断：
CAD/SU/材料/FF&E 影响：
风险：
下一步最小动作：
```
