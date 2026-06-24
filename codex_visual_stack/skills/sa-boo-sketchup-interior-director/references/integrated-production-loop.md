# SA&BOO Integrated Interior Production Loop

Use this reference when a project spans co-design, layout/CAD accuracy, SketchUp modeling, organic/detail modeling, Enscape, AI Render/imagegen, visual asset indexing, and proposal output. The goal is to prevent plugin fragmentation and turn many skills into one self-correcting design workflow.

## Prime rule

```text
co-design alignment → visual evidence → CAD/layout truth → SketchUp model proof → detail/model QA → material-light-camera proof → three-route output → image QA → asset index → next decision
```

Do not start from tools. Start from the design question and the next visual proof.

## Skill ownership matrix

| Gate | Design question | Primary skill | Support skills | Required visual/evidence |
|---|---|---|---|---|
| B00 原始基准 | What is the measured source of truth? | `sa-boo-co-design-interior-partner` | `interior-layout-optimizer`, `cadq`, `sa-boo-cad-sketchup-bridge` | CAD/PDF/SU top view, known dimension check, source preserved |
| A01 科学平面 | Does the plan work in real use? | `interior-layout-optimizer` | `cadq`, AutoCAD MCP, SC071 retrieval | measurable layout diagnosis, circulation/storage/wet-area checks |
| SU01 准确白模 | Does SketchUp match CAD and scale? | `sa-boo-cad-sketchup-bridge` | edge cleanup, solid inspector, SketchUp MCP | clean top view, 2 perspectives, 1 elevation/section, scale QA |
| SU02 重点节点 | Which nodes decide the scheme? | `sa-boo-sketchup-interior-director` | `sketchup-artisan-organic-modeling`, profile/panel/curve skills | key-node white model, detail view, buildability note |
| M01 材质/灯光 | Does material/light support the concept? | `sketchup-enscape-render-workflow` | material/texture/color/light skills | material zones, lighting story, Enscape/source previews |
| R01 汇报图 | Which images are client-safe? | `sa-boo-sketchup-interior-director` | Enscape, AI Render, imagegen, proposal deck, visual asset index | contact sheet, selected hero/detail images, QA note |

## Three output routes

Keep all three routes available, but choose one primary route per round:

```text
Route A — Model-native render
SketchUp / 3ds / D5 / Enscape / V-Ray / Twinmotion. Use when geometry, scale, and buildability must be protected.

Route B — imagegen / AI image output
Use for controlled concept variants, white-model-to-render, material-light studies, or render polish. Requires source readiness and anti-drift constraints.

Route C — portable prompt pack
Use when direct rendering/generation is blocked or Bonnie wants external iteration in another agent/tool. Must include preserve/may-change/negative/QA fields.
```

## Self-looping protocol

Use this loop after every significant action:

```text
1. Read triggered skill(s).
2. Identify current gate and design question.
3. Define the visual key image or measurable proof.
4. Execute the smallest useful action.
5. Run QA: scale, geometry, material, light, camera, anti-AI, buildability.
6. Reject weak output internally.
7. Save/cite accepted visual evidence through the visual asset index.
8. Feed the lesson back into the next model/render/prompt step.
9. Ask Bonnie only for subjective or identity-defining decisions.
```

Stop the loop when it becomes mechanical, produces files without better decisions, or hides a weak model behind rendering.

## Model-before-render hard gate

Do not enter Enscape, AI Render, imagegen, or final prompt generation unless the source model passes:

```text
- CAD/layout scale confirmed or uncertainty stated.
- No oversized hidden CAD reference or far-away geometry corrupting extents.
- Clean source view/contact sheet exists.
- Camera is readable and not blocked.
- Main spatial hierarchy is clear.
- Material zones or white-model zones are distinguishable.
- Lighting story is plausible.
- No obvious duplicate geometry, wrong overlaps, broken faces, or render helpers polluting deliverables.
```

If the gate fails, output:

```text
本轮不进入渲染，先做模型 V_next。
失败原因：
下一视觉检查点：
```

## Visual asset index requirement

For every important checkpoint, record:

```text
asset_id
local_original_path
thumbnail_path
source_model_path / source_cad_path / source_url
capture_date
category / tags
rights_status
quality_notes
prev_id / next_id / related_ids
decision_supported
```

Use this especially for CAD/SU QA images, Enscape previews, AI Render variants, material boards, and client-facing contact sheets.

## Bilingual method requirement

Chinese is used for design judgment, local construction thinking, and Bonnie-facing critique. English is used for image prompts, international renderer collaboration, and concise professional design expressions. Do not translate literally; convert intent into professional design language.

Required bilingual block when useful:

```text
中文设计判断：
English design expression:
Key terms CN/EN:
Prompt-use English keywords:
```

## Standard integrated response

```text
本轮判断 / Current gate:
- Gate:
- Design question:
- Decision mode: Discuss / Recommend / Execute

视觉证据链 / Visual evidence:
- Current assets:
- Missing proof:
- Next visual key image:

准确性与模型 QA / Accuracy + model QA:
- CAD/layout:
- SketchUp scale/extents:
- Geometry overlaps/junk:
- Pass / fail:

生产路线 / Production routes:
1. Model-native route:
2. imagegen / AI route:
3. Portable prompt route:
- Primary route:
- Fallback trigger:

执行 / Next action:
- What I will do:
- What Bonnie must decide, if any:
- Output path(s):

质量检查 / QA:
- Keep:
- Reject:
- Next checkpoint:
```

## Calibration from Logicat R16 QA

Recent real-project lesson:

- Active model: `LOGICAT_popup_ASTRONAUT_CAT_UFO_R15_white_bg_ceiling_enscape.skp`.
- CAD basis: `popup_ufo_layout_8x9m_v2_ascii.dxf`, interpreted as 8000 × 9000 mm despite DXF unit-header ambiguity.
- Issue found: hidden locked group `LOCKED_IMPORTED_CAD_REF_PLAN_DXF` scaled about 1000× too large, corrupting model extents.
- Correct evidence: `VISIBLE_CAD_TRACE_FROM_PREVIOUS_DXF`, `CAD_SCALE_GRID_1000MM`, and `8m x 9m field from CAD - R08` align to 8000 × 9000 mm.
- Workflow lesson: never enter Enscape/AI Render before scale/extents QA; archive visual proof in `assets/visual_cache`.
