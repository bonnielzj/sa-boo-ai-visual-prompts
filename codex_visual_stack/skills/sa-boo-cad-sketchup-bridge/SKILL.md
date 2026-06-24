---
name: sa-boo-cad-sketchup-bridge
description: SA&BOO CAD↔SketchUp bridge workflow for interior design, renovation, and visual-first project delivery. Use when Codex needs to connect AutoCAD/DWG/DXF drawings with SketchUp 2025 modeling, clean CAD plans for SketchUp import, query or audit CAD files, create SU-ready reference drawings, build white models from CAD, export SketchUp visual decisions back to CAD construction drawings, manage CAD/SU file versions, or maintain a closed loop between accurate 2D construction information and high-quality SketchUp visual output. Must prioritize visual asset chain, white-model screenshots, camera views, render outputs, and CAD accuracy together.
---

# SA&BOO CAD SketchUp Bridge

Use this skill to make CAD and SketchUp work as one controlled interior-design pipeline. CAD provides **accurate 2D geometry, dimensions, layers, and construction language**. SketchUp provides **space, massing, material, lighting, camera, and visual output**. The bridge prevents messy imports, broken models, duplicate revisions, and unclear handoffs.

## Governing principles

- Follow `sa-boo-visual-first-core`: final value must include visual assets, not only text.
- Pair with `sa-boo-sketchup-interior-director` for SketchUp modeling/rendering and visual QA.
- Pair with `sa-boo-autocad-construction-standard` for CAD layers, annotations, revisions, and issue standards.
- Pair with `sa-boo-furniture-textile-softdecor` whenever CAD/SU work includes loose furniture, system furniture, textiles, FF&E, official brand downloads, SketchUp components, or furniture blocks; consult its database before creating/importing assets.
- Pair with `cadq` when querying DWG/DXF semantics or extracting numeric/spatial facts from CAD.
- Pair with `autocad-drafting` whenever AutoCAD MCP tools are invoked.
- Never treat raw CAD as directly model-ready. Create a clean SU import drawing first.
- Never treat SketchUp render geometry as construction truth. Bring confirmed decisions back to CAD with controlled layers, dimensions, and revision notes.


## B00/A01/SU01 gate discipline

For residential design, CAD↔SketchUp bridge is not complete just because files converted. It must preserve design trust:

- **B00**: create a baseline package from source PDF/CAD/DXF/SU: original/crop, clean CAD preview, top-view comparison, and known dimension check.
- **A01**: produce a scientifically justified optimized plan: circulation, clearances, furniture scale, storage capacity, door conflicts, wet-area/service constraints, and client use pattern.
- **SU01**: build a clean white model from the verified plan; imported CAD is locked reference, not messy modeling geometry.

Do not create abstract redlines or decorative SU work before these gates are readable. If DWG cannot be directly read by the current backend, use PDF as visual reference while converting/obtaining DXF; do not let conversion friction replace design progress.

When a project folder provides QA scripts such as `scripts/qa_visual_outputs.py`, run them on exported CAD/SU image folders and keep the resulting contact sheet/report with the revision notes.

## Core bridge loop

```text
Raw CAD / PDF / site info
→ CAD audit and cleanup
→ SU_IMPORT_CLEAN DWG/DXF
→ SketchUp locked reference
→ white model and visual output
→ design decisions / dimensions / elevations
→ CAD construction drawing update
→ issue package / revision log
→ next design iteration
```

## File structure

Use this folder logic for new projects:

```text
00_原始资料
01_CAD_Original
02_CAD_Clean_For_SU
03_SketchUp_Model
04_SU_Exports_View
05_Render_Assets
06_CAD_Construction
07_Client_Presentation
08_Revision_Log
```

Use versioned filenames:

```text
项目名_PLAN_ORIGINAL_R00.dwg
项目名_SU_IMPORT_CLEAN_R00.dwg
项目名_DESIGN_MODEL_R00.skp
项目名_WHITE_MODEL_VIEW_R00.png
项目名_RENDER_CONCEPT_R00.png
项目名_CONSTRUCTION_R00.dwg
项目名_REVISION_LOG_R00.csv
```

## CAD → SketchUp workflow

1. **Audit source CAD**
   - Confirm units, model-space geometry, extents, scale, origin distance, xrefs, blocks, hatch density, layers, and text/dimension clutter.
   - If spatial/numeric facts are needed from DWG/DXF, use `cadq` and do not invent numbers.

2. **Create SU clean drawing**
   - Save a separate `SU_IMPORT_CLEAN` file. Do not overwrite original CAD.
   - Keep only geometry needed for modeling: walls, openings, fixed furniture, key ceiling/ground/lighting control lines, main elevation datum, and critical reference dimensions.
   - Delete or isolate hatches, text, dimensions, title blocks, viewports, repeated symbols, heavy blocks, and remote geometry.
   - Place reference-only items on clear layers/tags such as `X-SU-REF-PLAN`, `X-SU-REF-CEILING`, `X-SU-REF-ELEV`, `X-SU-REF-FURN`.

3. **Import to SketchUp**
   - Import at millimeters unless project evidence says otherwise.
   - Keep imported CAD as a locked reference group/component.
   - Assign it to a reference tag such as `CAD_REF_PLAN` and do not model directly on messy imported edges.
   - Check a known dimension immediately.
   - Check origin and model extents. Move a copied working reference near SketchUp origin if needed, while keeping a note of alignment.

4. **Build clean SU model**
   - Trace/rebuild walls, openings, ceiling, floors, and fixed elements using clean SketchUp geometry.
   - Use CAD as reference, not as final model geometry.
   - Route to SketchUp skills: Edge Tools for line cleanup, 1001bit for architectural basics, Profile Builder for trims/panels, Floor Panel Grid for divisions, Curic Align View for elevations, Advanced Camera Tools for views.

5. **Output visual assets**
   - Produce plan-like top view, white-model perspectives, key elevation views, section/cutaway views, and camera list.
   - Continue into material/light/render pipeline only after white-model scale and focal walls pass QA.

Read `references/cad-to-sketchup.md` for detailed cleanup and import checklist.

## SketchUp → CAD workflow

1. **Identify confirmed design decisions**
   - Only export/translate confirmed geometry: wall changes, built-in furniture outlines, ceiling levels, lighting positions, material divisions, panel seams, section cuts, and key elevations.
   - Keep speculative/AI-only render details out of construction CAD unless confirmed.

2. **Export from SketchUp intentionally**
   - Export aligned elevations, section slices, plan views, and reference linework rather than full heavy textured models.
   - Use `sketchup-curic-align-view` for wall/cabinet/elevation views.
   - Use `sketchup-s4u-slice-section-cuts` for cut geometry and sections.
   - Use `sketchup-flatten-faces-cleanup` when panel layouts or curved surface unwrapping need 2D reference.

3. **Rebuild/standardize in CAD**
   - Put imported SU-derived linework on reference layers first.
   - Redraw/clean construction entities on SA&BOO CAD layers.
   - Add dimensions, tags, material codes, notes, and revision marks in CAD.
   - Plot PDF or screenshot for QA before issue.

Read `references/sketchup-to-cad.md` for return-to-CAD rules and deliverables.

## Decision ownership rules

```text
Precise dimensions / construction issue → CAD is source of truth.
Spatial composition / client visual approval → SketchUp is source of truth.
Material mood / lighting / camera / render → SketchUp/render asset is source of truth.
Issued construction drawings → CAD/PDF issue package is source of truth.
```

If CAD and SketchUp conflict, stop and report the conflict before continuing.

## Bridge QA gate

Before moving from CAD to SU:

- Units confirmed.
- Source file preserved.
- Clean import file created.
- Hatches/text/title blocks removed or isolated.
- Far-away geometry checked.
- Known dimension verified after import.
- CAD reference locked in SketchUp.

Before moving from SU to CAD:

- Design decision confirmed.
- View/cut exported intentionally.
- Scale and alignment checked.
- SU linework treated as reference first.
- CAD layers/dimensions/notes standardized.
- Revision log updated.

Before client or construction issue:

- Visual assets show the design clearly.
- CAD dimensions and annotations support the visual decisions.
- File names and revision status are clear.
- No unverified AI/render-only detail is presented as construction fact.

## Default response format

```text
桥接目标：CAD→SU / SU→CAD / 双向迭代
当前输入资产：
- CAD/DXF/PDF/SU/图片：
- 版本：
- 单位/比例状态：

视觉主线：
- 本轮必须产出的图像资产：
- 参考/白模/渲染/施工图之间的关系：

CAD 处理：
1.
2.
3.

SketchUp 处理：
1.
2.
3.

需要调用的 skills / MCP：
1.
2.
3.

风险与冲突：
- 尺寸：
- 图层/导入：
- 模型：
- 施工表达：

交付物：
- SU_IMPORT_CLEAN：
- SketchUp 模型/视图：
- 白模/渲染图：
- CAD 回传/施工图：
- 版本记录：
```

## Short trigger phrases

Bonnie can say:

- “把这个 CAD 接到 SketchUp workflow。”
- “先帮我清一个 SU 导入版 CAD。”
- “从这个 CAD 建白模。”
- “把这个 SU 立面逻辑回传到 CAD。”
- “检查 CAD 和 SU 有没有对不上。”
- “启动 CAD↔SketchUp 桥接流程。”
