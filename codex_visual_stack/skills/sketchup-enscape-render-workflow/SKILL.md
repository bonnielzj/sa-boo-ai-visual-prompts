---
name: sketchup-enscape-render-workflow
description: SketchUp Enscape 4.16+/4.18 Mac workflow for SketchUp 2025 interior rendering. Use when Codex needs to plan, prepare, audit, or guide Enscape real-time rendering from SketchUp 2025 on Bonnie's Mac Studio, including white-model-to-material render passes, camera/lighting/material setup, Asset Library/Cosmos usage, renderer QA, export packs, troubleshooting, and integration with SA&BOO visual-first image output.
---

# SketchUp Enscape Render Workflow

Use this skill when Enscape is the main render engine for SketchUp 2025 interior projects. Keep `sa-boo-visual-first-core` and `sa-boo-realtime-render-presentation` as governing standards: output decisions must lead to strong images, not only render settings.

## Installed environment

- Machine: Mac Studio, Apple M1 Max, 64 GB RAM, Metal 3.
- SketchUp: 2025.
- Enscape installer found: `/Users/bonnie/Downloads/Enscape-4.18.1.1579.dmg`.
- SketchUp extension registered at:
  - `/Library/Application Support/SketchUp 2025/SketchUp/Plugins/enscape.rb`
  - `/Library/Application Support/SketchUp 2025/SketchUp/Plugins/enscape/`
- Extension metadata reports: `Enscape For SketchUp`, version `4.16`, Chaos Software, 2026.
- Runtime path:
  - `/Library/Chaos/Enscape/Enscape.Sketchup.Plugin.Host-net10.0/`
  - includes `Enscape.Sketchup.Plugin.2025.runtimeconfig.json`.
- RendererHost path:
  - `/Library/Chaos/Enscape/RendererHost/Enscape.RendererHost`
- A running `Enscape.RendererHost --port ...` process means SketchUp has launched Enscape successfully.

## Safety note

A failed temporary Enscape 4.1 user-level bridge was disabled at:
`/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/_codex_disabled_enscape_2025_20260623_210853`.
Do not restore it unless intentionally debugging old versions.

## Integrated loop pairing

Pair with `sa-boo-sketchup-interior-director` and read its `references/integrated-production-loop.md` when Enscape is part of a broader CAD→SU→render workflow. Enscape must not start until visual evidence, CAD/model scale, extents, camera, and material zones pass the model-before-render gate. Save accepted Enscape previews into the project visual asset index.

## Core output logic

For interior design, use Enscape as the controlled render proof after white-model approval:

```text
SketchUp white model → camera lock → base material zones → Enscape lighting/material proof → hero/detail exports → QA → optional AI/post-production
```

Do not use Enscape to hide bad modeling. If scale, camera, or material zoning is weak, return to SketchUp first.

## Default Enscape image pack

For Bonnie's visual-first workflow, default to:

```text
1. 人视角 hero view
2. 入口/转场 view
3. 使用者坐姿/站姿 view
4. 关键立面 45° view
5. 特殊造型 close-up
6. 材质/灯光 detail close-up
```

Top views are internal checks only unless the user asks.

## Scene preparation

1. Lock SketchUp camera scenes before rendering.
2. Use human-eye camera height: usually 1300-1600 mm standing, 950-1200 mm seated.
3. Use two-point perspective / vertical correction for hero and elevation-like views.
4. Keep geometry clean: no duplicate faces, hidden junk, excessive components, or broken imports.
5. Name tags/materials clearly by role: `WALL_main`, `FLOOR_wood`, `STONE_feature`, `LIGHT_cove`, etc.
6. Assign simple material zones before detailed Enscape materials.

## Lighting strategy

Choose one coherent story per pass:

- Daylight soft: natural window light, low contrast, material readability.
- Warm evening: cove light + task light + restrained accent, no over-glow.
- Gallery accent: wall-wash / artwork / sculptural focal lighting.
- Commercial bright: more even illumination, less drama, clear client decision images.

Avoid random glow strips everywhere. Every visible light must have a reason.

## Material strategy

- Use Enscape/PBR materials only after spatial proof is approved.
- Prioritize correct scale, roughness, reflection, bump/normal, and texture direction.
- For luxury interiors, avoid high-gloss presets everywhere; use controlled reflection and tactile contrast.
- Use Architextures / texture positioning / material replacer before Enscape if material zoning or UVs are messy.

## Export QA

Before accepting Enscape output:

1. Camera: verticals controlled, no fisheye, composition has hierarchy.
2. Scale: furniture, openings, ceiling, cabinets, circulation feel real.
3. Lighting: source is plausible; no uncontrolled blown-out strips.
4. Materials: wood/stone scale and direction are believable.
5. Detail: special forms have close-up proof.
6. Anti-AI feeling: not generic luxury, not random props, not soulless showroom.
7. Deliverable: each image answers a design question.

## Standard response pattern

```text
Enscape 渲染任务：
- 本轮要证明：
- 目标图片：

SketchUp 准备：
- 模型：
- 材质分区：
- 相机：

Enscape 设置：
- 灯光故事：
- 材质重点：
- 输出规格：

出图清单：
1.
2.
3.

QA：
- 通过：
- 风险：
- 下一张图：
```
