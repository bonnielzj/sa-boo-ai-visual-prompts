---
name: sa-boo-autocad-construction-standard
description: SA&BOO AutoCAD construction drawing standard for interior design and renovation drawings, including CAD layer naming, colors/lineweights, annotation and dimension styles, title blocks, sheet/file naming, issue versions, revision clouds, change logs, redlines, QA/QC checks, and AutoCAD MCP drafting setup. Use when the user asks to learn, create, audit, standardize, or automate AutoCAD施工图, 室内施工图, 图层, 标注, 出图, 版本, 变更, 竣工图, DWG/DXF review, or SA&BOO CAD office standards. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO AutoCAD Construction Standard

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Use this skill to create or audit SA&BOO interior construction drawings with consistent layers, annotations, versions, and change control. It complements `autocad-drafting`; load `autocad-drafting` whenever calling AutoCAD MCP tools.

## Operating principle

- Draft in **model space at 1:1, millimeters**.
- Plot from layout sheets with controlled title blocks, viewports, scales, CTB/STB, and revision table.
- Keep drawings clean enough that another designer, site contractor, supplier, or future Bonnie can understand them without asking.
- Treat issued drawings as legal/business records: never overwrite issued DWG/PDF packages.

## Reference workflow

1. **Set up project standard**
   - Read `references/layer-standard.md` for layer names and plotting weights.
   - Run `scripts/generate_cad_assets.py` to create the latest CSV/LISP/SCR assets when needed.
   - In AutoCAD, load `assets/create_samboo_layers.lsp` or execute its code via AutoCAD MCP.

2. **Set up annotation**
   - Read `references/annotation-standard.md` before drawing dimensions, tags, leaders, and notes.
   - Use paper heights: 2.5mm body/dims, 3.5mm subtitle, 5mm drawing title, 7mm sheet title.
   - Use annotative styles when possible; otherwise model text height = paper height × scale.

3. **Manage files and versions**
   - Read `references/version-revision-standard.md` before issuing or revising drawings.
   - Keep WIP and issued folders separate.
   - Use R00/R01/R02 for issued revisions; use v0.x only for internal working versions.

4. **Handle changes**
   - Put revision clouds and delta triangles on revision layers.
   - Update title block revision table and `assets/change_log_template.csv`.
   - Cloud only current issued revision unless the client/contract requires cumulative clouds.

5. **QA before issue**
   - Read `references/qaqc-checklist.md`.
   - Check layers, lineweights, dimensions, viewport scales, Xrefs, title block, revision table, and plot output.

## AutoCAD MCP use

When automating drawings:

- First load `autocad-drafting`.
- Do not call AutoCAD MCP tools in parallel.
- For layer setup, prefer one LISP batch using `system.execute_lisp` with code from `assets/create_samboo_layers.lsp`.
- After drawing, use screenshots/PDF plot QA before saving/issuing.

## Output format

```text
施工图标准判断：
图层/线宽问题：
标注/尺寸问题：
版本/变更问题：
建议修正步骤：
可执行 AutoCAD/LISP：
出图前 QA：
```

## Quick defaults

- Layer prefix: `I` interiors, `A` architecture, `E` electrical, `P` plumbing, `M` mechanical/HVAC, `X` xref/reference, `NPLT` non-plot.
- Layer pattern: `{discipline}-{major}-{minor}-{status}` where useful, e.g. `I-WALL-FULL-N`.
- Status codes: `N` new, `E` existing, `D` demolish, `F` future, `T` temporary, `R` revision.
- Key layers: walls, doors, fixed furniture, ceiling, floor finish, lighting, power, plumbing, dimensions, text, tags, revision clouds, title block, non-plot construction.
