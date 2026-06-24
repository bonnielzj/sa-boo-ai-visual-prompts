---
name: sa-boo-realtime-render-presentation
description: SA&BOO real-time rendering presentation workflow for D5 Render, Enscape, Twinmotion, and similar interior visualization tools, covering quick client presentations, lighting setup, material standards, camera composition, scene states, before/after comparisons, export packs, QA, and social/proposal reuse. Use when the user asks to learn, standardize, create, audit, or plan D5/Enscape/Twinmotion renders, real-time walkthroughs, interior render briefing, lighting/material/camera settings, before-after views, proposal render packs, or rendering-to-Figma/PDF/Xiaohongshu workflows. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Realtime Render Presentation

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Use this skill to turn 3D models into fast, controlled client-facing visuals with D5 / Enscape / Twinmotion. The goal is not maximal photorealism every time; it is **clear design decision communication**: space, light, material, mood, and before/after value.

## Default strategy

- **Early concept**: quick model + AI/mood references + 4-6 stills. Do not over-polish.
- **Client decision meeting**: before/after, option A/B, material closeups, lighting scenes.
- **Final proposal**: refined stills + short walkthrough + annotated comparison pages.
- **Social/case study**: export clean before/after pairs and vertical crops.

## Tool positioning

Read `references/tool-comparison.md` when choosing a tool.

- **D5 Render**: best SA&BOO default for high-speed interior mood, asset/material richness, cinematic stills/video.
- **Enscape**: best for live design review inside SketchUp/Revit/Rhino and quick client walkthroughs.
- **Twinmotion**: best for large scenes, landscape/context, phasing, presentation/media packs, Unreal ecosystem.

## Workflow

1. **Brief the render pack**
   - Project type, design stage, target audience, deliverable, time budget.
   - Read `references/render-pack-scope.md` for 30-minute / 2-hour / half-day pack choices.

2. **Prepare the model**
   - Clean geometry, correct scale, meaningful layers/tags, no duplicate surfaces.
   - Assign base materials before import; name objects by function/material.

3. **Set light**
   - Read `references/lighting-standard.md`.
   - Use one coherent lighting story: natural soft morning, warm evening, gallery accent, or commercial bright.
   - Always separate ambient light, key task light, and decorative/accent light.

4. **Set materials**
   - Read `references/material-standard.md`.
   - Prioritize scale, roughness, reflection, bump/normal, and edge detail.
   - Do not use glossy presets everywhere; luxury = controlled reflection and tactile contrast.

5. **Set cameras**
   - Read `references/camera-standard.md`.
   - Build a shot list before rendering. Use consistent height, focal length, vertical correction, and naming.

6. **Create before/after and options**
   - Read `references/before-after-standard.md`.
   - Use locked camera pairs; only design content changes.
   - Use matching exposure, focal length, crop, and time of day.

7. **Export and QA**
   - Read `references/export-qaqc.md`.
   - Export stills, short video/walkthrough if needed, panorama/presentation when useful, and Figma/PDF-ready image packs.

## Output pattern

```text
汇报目标：
推荐工具：D5 / Enscape / Twinmotion / 混合
交付包：
镜头清单：
灯光策略：
材质策略：
Before/After策略：
导出规格：
QA检查：
下一步：
```

## Risk rules

- Mark early renders as “概念效果，以施工图和材料实样为准”.
- Do not show impossible lighting, wrong material scale, or unbuildable details as final commitment.
- Avoid over-beautified images that hide design decisions; every image should answer a client question.

## Visual asset reference requirement

For any render standard, mood direction, lighting/material/camera recommendation, or before/after plan, first use `sa-boo-visual-asset-index` when available. Return at least 3 cited visual assets with:

```text
Asset ID:
Thumbnail:
Original local path:
Source page URL:
Original image URL:
Rights/usage:
What this asset teaches for the current render:
```

Do not give pure text standards when the user asks for learning, inspiration, or visual direction. If no project-owned assets exist, use reference-only indexed assets for private study and clearly mark them as not for public/client reuse.

