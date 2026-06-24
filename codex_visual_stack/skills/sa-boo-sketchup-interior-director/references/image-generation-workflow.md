# Image Generation Workflow for SA&BOO SketchUp Interior Director

Use this reference when the task involves AI image generation, white-model-to-render, sketch-to-render, material/light variants, prompt packs, or image polishing. The goal is not simply to generate attractive pictures; the goal is to create images that advance a real interior design decision.

## Prime rule

```text
source visual → readiness score → generation route → prompt matrix → output QA → design feedback → next visual checkpoint
```

Do not let prompt writing compensate for weak spatial authorship. If the source model or brief is not strong enough, return to SketchUp/modeling or concept definition first.

## 1. Source asset readiness gate

Before generating, score the input asset or brief:

```text
Source asset readiness:
- Geometry clarity: pass / weak / fail
- Camera clarity: pass / weak / fail
- Spatial hierarchy: pass / weak / fail
- Material zoning: pass / weak / fail
- Lighting logic: pass / weak / fail
- Resolution/readability: pass / weak / fail
- Design specificity: pass / weak / fail
Decision: ready for imagegen / needs SketchUp capture / needs concept route / needs external prompt only
```

Minimum source package for reliable interior generation:

- one hero white-model screenshot or render-view capture;
- one plan/top/high-angle proof if layout matters;
- one focal-wall/elevation view if a wall/detail is the subject;
- a short preservation list: openings, walls, ceiling, circulation, camera angle, main furniture;
- a short creative variable list: material tone, light temperature, styling, atmosphere.

If more than two categories fail, do not generate final-looking images. Produce a model/camera fix plan or a portable exploratory prompt instead.

## 2. Image generation modes

Choose the mode before writing prompts:

| Mode | Use when | Output |
|---|---|---|
| Faithful white-model-to-render | geometry must remain accurate | 1-3 realistic renders preserving model/camera |
| Concept atmosphere exploration | mood/material direction is not chosen | 3-6 controlled variants |
| Material/light swap | form is approved but palette/light needs testing | A/B material-light comparison |
| Detail/focal-wall study | a wall, cabinet, ceiling, or feature needs development | aligned elevation + detail crops |
| Render polish | existing render is close but lacks quality | improved image preserving composition |
| Portable external prompt | direct generation/rendering is blocked | ready-to-run prompt pack |

## 3. Prompt matrix method

Avoid a single overstuffed prompt. Build a small matrix:

```text
Base invariant lock:
- Preserve exactly:
- Do not change:
- Camera / aspect:
- Functional layout:

Variant axis A — material:
A1 restrained stone + warm wood
A2 pale plaster + dark walnut
A3 mineral grey + bronze detail

Variant axis B — lighting/mood:
B1 soft daylight
B2 warm evening residential
B3 gallery accent / low contrast

Generation set:
- V1 faithful baseline: A1+B1
- V2 warmer emotional route: A2+B2
- V3 sharper editorial route: A3+B3
```

For serious design work, produce at least:

1. **Faithful baseline** — closest to the SketchUp model and current design.
2. **Creative upgrade** — stronger atmosphere while preserving layout.
3. **Risk route** — more memorable but clearly marked as experimental.

## 4. Prompt structure for imagegen

Use this structure for `imagegen` or portable prompt packs:

```text
Use case: sketch-to-render / photorealistic interior / material-light study
Input image role: source SketchUp white-model screenshot / focal-wall elevation / reference mood image
Design thesis: <one sentence>
Primary request: <what to generate or edit>
Preserve exactly: <geometry, openings, camera, layout, circulation, major furniture>
May reinterpret: <material tone, light mood, accessories, texture richness>
Spatial hierarchy: <main volume, axis, focal wall, threshold, ceiling move>
Materials: <primary / secondary / accent with scale and finish>
Lighting: <ambient / task / accent; color temperature; construction logic>
Camera/composition: <lens feel, verticals, crop, viewpoint>
Human/lived-in detail: <subtle, functional, non-random detail>
Quality target: high-end editorial interior photography, sharp, refined, buildable
Negative prompt: <AI drift, changed layout, fake openings, excessive glow, random luxury, impossible joints, distorted furniture, glossy plastic, low resolution>
```

## 5. Anti-drift constraints

Always include preservation constraints when a SketchUp/CAD source exists:

```text
Preserve the exact source geometry, wall openings, ceiling massing, camera angle, circulation, and main furniture positions. Do not add windows, remove walls, change door locations, alter ceiling height, distort furniture scale, or invent impossible construction.
```

Use stronger negative prompts for interiors:

```text
generic AI interior, random luxury, changed floor plan, fake openings, impossible construction, excessive glowing strips, meaningless arches, incoherent style mix, glossy plastic, distorted furniture, fisheye lens, over-smoothed surfaces, lifeless showroom, low resolution, blurry, watermark
```

## 6. Output count and aspect ratios

Default suggestions:

- Early concept: 3 outputs, 16:9 or 4:3.
- Focal wall / elevation: 2-3 outputs, 3:2 or 4:3; use aligned/orthographic source when possible.
- Social / Xiaohongshu crop: 2 outputs, 3:4 or 9:16.
- Client hero still: 3-4 outputs, 16:9 or 3:2.
- Detail/material crop: 2 outputs, 1:1 or 4:5.

Do not request too many variants before the source concept is sharp. More images do not fix a vague design.

## 7. Generated image QA

After generation, score each image:

```text
Image QA:
- Geometry preservation: 0-3
- Spatial hierarchy: 0-3
- Material discipline: 0-3
- Lighting logic: 0-3
- Camera quality: 0-3
- Buildability: 0-3
- Anti-AI realness: 0-3
- Emotional/design memory: 0-3
Decision: keep / revise prompt / return to SketchUp / reject
```

Reject images even if beautiful when they:

- change the plan or openings;
- fake the ceiling/wall condition;
- hide bad scale with haze or darkness;
- add random luxury decoration;
- destroy the intended focal hierarchy;
- look like generic AI portfolio images rather than this project.

## 8. Feedback loop back to SketchUp

Every accepted generated image must become one of these:

```text
- SketchUp modeling instruction: what geometry/detail/material to build next.
- Material palette update: what finishes and texture directions to test.
- Camera/light update: what scene, lens, crop, or lighting story to recreate.
- Proposal asset: selected render/contact sheet with QA note.
- Prompt revision: what to lock, remove, or strengthen in the next round.
```

Do not finish with “nice image.” Finish with the next design action.

## 9. Standard response block

```text
Image generation plan:
- Source readiness:
- Generation mode:
- Primary route:
- Variant matrix:
- Prompt set:
- Expected output count/aspect:
- QA criteria:
- If generation fails:
- Feedback back to SketchUp:
```
