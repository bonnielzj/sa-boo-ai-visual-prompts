# SA&BOO SketchUp Visual Output Standard

Use this reference when a task involves white-model output, camera views, render prompts, material/light studies, or client-facing visual assets.

## Visual chain levels

### Level 0 — No usable visuals

Only text idea exists. Output a structured assumption brief and request/define minimum visual assets:

- plan or rough dimensions,
- one sketch/reference image,
- one target view or focal wall,
- desired mood/material words.

Do not pretend a final design exists. Produce a first-pass visual plan.

### Level 1 — Planning visuals

Inputs include plan/elevation/photo/reference. Produce:

- design brief,
- visual asset list,
- white-model target views,
- plugin/skill routing,
- first modeling steps.

### Level 2 — White model visuals

Inputs include SketchUp model or screenshots. Produce:

- massing critique,
- camera/scene list,
- white-model QA,
- material zoning,
- render prompt draft.

### Level 3 — Material/render visuals

Inputs include model views or draft renders. Produce:

- material/light/camera refinement,
- A/B option critique,
- final image pack plan,
- client-safe narrative.

### Level 4 — Presentation assets

Inputs include final renders/diagrams. Produce:

- selected image sequence,
- before/after pairs,
- proposal layout logic,
- social/case-study crops,
- final QA notes.

## Minimum image pack by stage

### Early concept

- 1 plan/top view or zoning diagram.
- 2 white-model perspective views.
- 1 focal-wall/elevation view.
- 1 mood/material reference chain.

### Design development

- 4 hero camera scenes.
- 2 aligned elevation views.
- 2 material/detail closeups.
- 1 before/after or option A/B comparison.

### Client presentation

- 6-10 curated stills.
- 2 before/after pairs.
- 1 material board.
- 1 annotated design logic page.
- Optional vertical Xiaohongshu crop.

## Camera standards

- Interior eye-level default: about 1200-1500mm unless intentionally lower/higher.
- Avoid extreme wide angle unless documenting small-space layout.
- Keep verticals controlled for architecture/interior views.
- Use one hero shot to explain the spatial concept, not just decoration.
- Create aligned orthographic/elevation views for walls, cabinets, and material divisions.

## Material standards

- Define primary, secondary, and accent materials.
- Material names should be functional: `wall_stone_warm_grey`, `wood_walnut_dark`, `metal_champagne_matte`.
- Check scale before judging beauty: stone veining, wood grain, tile size, fabric weave.
- Luxury effect comes from proportion, texture, edge detail, light control, and restraint.

## Lighting standards

- Start with one lighting story:
  - soft daylight,
  - warm evening residential,
  - gallery accent,
  - commercial bright,
  - cinematic low contrast.
- Separate ambient, task, and accent light.
- Avoid random glowing strips without construction logic.
- Use light to reveal material texture and spatial depth.

## Bilingual design language standard

For SketchUp/render/presentation work, language must be precise enough to guide action. Use bilingual terminology when it improves modeling, prompting, or client communication.

### Required bilingual fields when writing prompts or proposal notes

```text
中文设计表达：
English design expression:
Key terms CN/EN:
Prompt-use English keywords:
Avoid vague words:
```

### Preferred term pairs

```text
体块 massing / volume
轴线 axis
序列 spatial sequence
阈限 threshold
动线 circulation
视线 sightline
比例 proportion
节奏 rhythm
层次 hierarchy
收口 detailing / junction
阴影缝 shadow gap
分缝 reveal / joint
材质层级 material hierarchy
纹理方向 grain direction
洗墙 wall washing
间接光 indirect lighting
线性灯槽 linear light slot
低调奢华 understated luxury
当代东方 contemporary Eastern
克制 restrained
静谧 serene
画廊感 gallery-like
居住感 lived-in
```

Language fails QA if it is generic, literal, over-poetic without design anchors, or unusable by a modeler, renderer, client, supplier, or another agent.

## Three-route output standard

For every render/material/image-output stage, define three executable routes so the project does not depend on one fragile tool path.

### Route A — Model-native rendering from SketchUp / 3ds / 3D files

Use this first when geometry, dimensions, openings, material zones, and camera scenes must be preserved. Inputs may be .skp, .3ds, .fbx, .dae, .obj, D5/Enscape/V-Ray/Twinmotion scenes, or exported white-model views. Output should include scene name, camera, render engine, target aspect, and output path.

### Route B — imagegen high-quality image generation/editing

Use when high-quality bitmap concepts, material-light studies, sketch-to-render, white-model-to-render, or visual variants are needed. Prefer source screenshots from validated models. Label every input image role and preserve layout, openings, camera angle, and functional scale unless the brief explicitly allows change.

### Route C — Portable ready-to-run prompt pack

Use when direct rendering/imagegen is blocked or Bonnie wants external iteration. The prompt must be tool-agnostic enough for another agent, Midjourney, 即梦, Stable Diffusion, Runway, D5 AI, Enscape AI, or a human render collaborator.

Required card:

```text
Three output routes:
1. Model-native route:
2. imagegen route:
3. Portable prompt route:
Primary route this round:
Fallback trigger:
```

Portable prompt must include:

```text
Prompt name:
Input image role:
Prompt:
Negative prompt:
Preserve exactly:
May reinterpret:
Camera / aspect ratio:
Output count:
Quality target:
QA checklist:
```

## AI render prompt structure

```text
Subject / space type:
Geometry from source white model:
Style and atmosphere:
Materials:
Lighting:
Camera and composition:
Quality words:
Constraints / do not change:
Negative prompt:
```

Example skeleton:

```text
A refined contemporary living room based on the provided SketchUp white model, preserve the wall openings, ceiling massing, sofa location, and camera angle. Warm grey limestone, dark walnut veneer, matte champagne metal trims, soft ivory fabric sofa, low-key East-West luxury, calm spatial order, layered cove lighting and subtle wall washer, eye-level architectural interior photography, controlled verticals, tactile materials, high-end editorial composition.

Negative: distorted layout, extra windows, wrong openings, excessive decoration, glossy plastic, messy furniture, random neon light, overexposed image, fisheye lens, low resolution, cartoon style.
```

## Rejection criteria

Reject or revise any image/model output with:

- broken scale,
- wrong camera distortion,
- too many unrelated materials,
- generic hotel-style cliché without concept,
- bad texture scale or direction,
- impossible lighting construction,
- poor focal hierarchy,
- messy model geometry,
- low-resolution or blurry output.

## Model-before-render gate

Use this gate before AI Render, D5, Enscape, image generation, or any materialized output based on a SketchUp source image.

Do **not** let prompt quality compensate for weak modeling. If the source model is generic, open, badly composed, or lacks designed hierarchy, stop rendering and improve the model first.

### Source model must pass

- **Closed shell**: no missing ceiling/wall/floor faces, no sky leaks, no visible outside void unless intentionally modeled.
- **Camera proof**: camera is inside/valid, not blocked by walls, not excessively wide, and the main focal idea is readable.
- **Spatial hierarchy**: one clear primary move, such as portal, frame, curve, wall thickness, ceiling raft, focal wall, furniture island, or light slot.
- **Proportion rhythm**: panels, slabs, trims, furniture, and ceiling lines have believable scale and spacing.
- **Material zones**: even in white model, wall/floor/ceiling/wood/stone/metal/fabric zones are named or visually separated.
- **Light logic**: cove, washer, task, or ambient light has a plausible construction position; no random glow strips.
- **Furniture credibility**: major furniture has real scale, cushion/edge logic, and does not read as only crude placeholder boxes.
- **Clean source**: no guide labels, helper lines, default blue/back faces, material leaks, or unrelated clutter in render views.

### If the gate fails

Return this decision before generating:

```text
本轮不进入渲染，原因：<source-model failure>
先做模型 V_next：
1.
2.
3.
下一视觉检查点：<source PNG/contact sheet path or scene name>
```

### Minimum pass package

Before rendering, produce or request:

- 1 source contact sheet,
- 1 hero source view,
- 1 focal-wall/elevation source view,
- 1 spatial proof/top/high-angle source view,
- 1 short QA note naming what still fails.


## Real design / anti-AI feeling standard

Use this standard whenever AI rendering, white-model interpretation, or style generation risks becoming generic.

### What “AI感” usually looks like

Reject or revise outputs that show:

- generic luxury hotel clichés without a site/client reason,
- random marble, metal, arches, sculptural furniture, or glowing strips added only for visual noise,
- impossible joints, floating panels, unbuildable ceilings, or material transitions with no thickness,
- over-perfect showroom staging with no life, memory, use, or human scale,
- inconsistent style mashups that look trendy but not authored,
- fake depth, fake window views, wrong openings, changed floor plan, or ignored white-model constraints,
- excessive smoothness, plastic textures, glossy everything, or meaningless cinematic haze,
- objects that do not support function, circulation, storage, ritual, brand, or emotion.

### What “real design” must show

Approve only when the work shows:

1. **Use logic** — the design supports how people enter, sit, cook, gather, work, display, rest, store, or move.
2. **Spatial authorship** — there is a clear idea: axis, threshold, frame, compression/release, focal wall, sequence, or ritual.
3. **Material truth** — materials have scale, thickness, edge logic, maintenance awareness, and tactile contrast.
4. **Light with purpose** — lighting reveals space and use; it is not decoration-only glow.
5. **Human trace** — the space feels inhabitable, with restraint, memory, and small intentional details.
6. **Construction imagination** — even if conceptual, it suggests how it could become real.
7. **Project specificity** — it belongs to this client/site/brief, not a generic prompt trend.

### Prompt anti-AI guardrail

When writing AI render prompts, include preservation constraints and project specificity:

```text
Preserve the exact SketchUp white-model geometry, wall openings, ceiling massing, camera angle, and functional layout. Make the design feel authored, buildable, and lived-in, not generic AI luxury. Use restrained materials, believable joints, real furniture scale, controlled lighting, and quiet human details specific to this project.
```

Add negative prompt terms:

```text
generic AI interior, random luxury, impossible construction, fake openings, changed layout, overdecorated, glossy plastic, excessive glow, meaningless arches, incoherent style mix, lifeless showroom, distorted furniture, fake depth, over-smoothed surfaces
```

### Real-design QA question

Before calling an output final, answer in one sentence:

```text
这个设计的灵魂在哪里？它为什么不是一张漂亮但空洞的 AI 图？
```


## No-image-no-finish production rule

For Bonnie's interior workflow, text is allowed for planning but not accepted as a final design deliverable. Every production round must end with one of these:

1. **Actual image asset** — screenshot, render, generated image, diagram, material board, or exported view with a local path or inline display.
2. **Capture instruction** — exact view/camera/scene to capture from SketchUp, CAD, 3ds/3ds Max, D5, Enscape, LightUp, V-Ray, Twinmotion, or AI Render.
3. **Generation prompt pack** — ready-to-run prompt plus negative prompt, input image role, preservation constraints, aspect ratio, and target output count.
4. **Three-route output card** — model-native route, imagegen route, and portable prompt route with primary route and fallback trigger.
5. **Asset gap request** — if blocked, state the missing image/file needed and why it is the next visual checkpoint.

### Minimum visual loop

```text
idea → visual target list → white-model screenshot → critique → material/light test → critique → final image pack
```

### Output status labels

Use one of these labels at the end of design responses:

```text
视觉状态：已产出图片资产
视觉状态：等待你截图/导出
视觉状态：可立即进入 AI Render / image generation
视觉状态：缺少关键输入图，无法负责任出图
```

### Image prompt pack requirements

When actual generation is the next step, include:

```text
Input image role:
Prompt:
Negative prompt:
Preserve:
May change:
Aspect ratio:
Output count:
QA focus:
```

### First-test image package

For a new space idea with no model yet, the first usable output package should be:

- one rough plan/diagram or CAD/SU reference request,
- one white-model camera list,
- two draft perspective prompt directions,
- one focal-wall/elevation direction,
- one negative prompt preventing AI drift.
