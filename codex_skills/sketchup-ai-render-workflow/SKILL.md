---
name: sketchup-ai-render-workflow
description: SketchUp AI Render / SketchUp Diffusion workflow for SketchUp 2025 interior design. Use when Codex needs to plan, prepare, prompt, audit, or guide AI Render outputs from SketchUp scenes, including white-model-to-material concept renders, prompt/negative-prompt writing, geometry-vs-prompt influence strategy, material and lighting descriptions, inpainting/regeneration guidance, render pass planning, client-safe privacy cautions, and integration with SketchUp MCP scene/camera/model preparation.
---

# SketchUp AI Render Workflow

Use this skill to turn a SketchUp 2025 model or white model into controlled AI Render concept images for SA&BOO interior design work. This skill does not assume Codex can press AI Render's UI buttons directly; Codex prepares the SketchUp scene, camera/material intent, prompt pack, QA checklist, and manual operation steps. If SketchUp MCP is running, use it only for model/scene preparation, viewport export, and verification—not for uploading confidential design data without user approval.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS / Apple Silicon.
- AI Render plugin installed from `/Users/bonnie/Downloads/ai_render_2026-06-03.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_diffusion.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_diffusion/`
- Plugin version from loader: `1.2026.06.03`; creator: Trimble; SketchUp requirement: 2024.0 or higher.
- The RBZ contains macOS universal `SketchUpDiffusion.bundle` files and Windows `.so` files. Treat the macOS `.bundle` as the relevant runtime.

Read `references/ai-render-2026-06-03.md` when working on concrete AI Render prompts, scene prep, privacy, or troubleshooting.

## Integrated loop pairing

Pair with `sa-boo-sketchup-interior-director` and read its `references/integrated-production-loop.md` when AI Render is part of a broader production chain. AI Render must use the same source-readiness, model-before-render, anti-drift, QA, and visual-asset-index rules as imagegen/Enscape. If a model has scale/extents errors, output a prompt plan only and block final generation.

## Core workflow

1. **Confirm project stage and image role**
   - White model massing study: prioritize spatial blocks, depth, light, and silhouette.
   - Material exploration: preserve core geometry but let AI develop wall/floor/ceiling/furniture finish.
   - Client-facing concept: lock camera and write more conservative, buildable material prompts.
   - Social/mood visual: allow more stylization but label as concept, not final construction promise.

2. **Prepare SketchUp before AI Render**
   - Clean model scale, visible camera composition, tags/layers, and object names.
   - Hide messy construction guides, redundant geometry, and irrelevant background assets.
   - Set a clear camera: 2-point perspective, vertical correction, human eye height, readable focal length.
   - Add simple base materials to guide zones: walls, floor, ceiling, built-ins, furniture, metal, glass, textile.
   - For white model passes, keep geometry white/off-white but use shadows, section depth, and material labels in prompt.

3. **Run the model-before-render gate**
   - Do not render a weak or generic model just because the prompt is strong. A bad source image becomes a bad AI render with nicer materials.
   - Block rendering and return to SketchUp modeling if the room shell is open, the camera is outside/blocked, default/back-face materials leak, scale is unbelievable, the focal wall has no hierarchy, the ceiling/floor are unresolved, furniture is only crude boxes, or the light source has no construction logic.
   - Require a source PNG/contact sheet before AI Render. Judge the source image first: closed shell, spatial hierarchy, proportion rhythm, material zones, lighting story, camera composition, and one clear design idea.
   - If the source fails, state: `本轮不进入渲染，先做模型 V_next` and name the exact model fixes.

4. **Write prompt in structured blocks**
   - Scene: room type, camera view, spatial relationship.
   - Design language: restrained luxury / East-West / gallery / warm minimal / etc.
   - Materials: floor, wall, ceiling, built-ins, furniture, metal, textile, stone/wood.
   - Lighting: daylight direction, ambient fill, task light, accent light, mood.
   - Control: preserve SketchUp geometry, keep built proportions, avoid changing layout.
   - Output: photorealistic interior render, clean composition, no people unless requested.

5. **Set influence strategy**
   - Early style exploration: lower geometry influence, higher prompt influence.
   - Accurate client review: higher geometry influence, moderate prompt influence.
   - Material iteration on fixed layout: high geometry influence, specific material prompt.
   - Inpainting/regeneration: isolate one area and keep the rest unchanged.

6. **Use negative prompt**
   - Block common failures: distorted furniture, extra windows/doors, wrong layout, warped ceiling, messy clutter, cartoon style, over-glossy surfaces, people, text/logo/watermark, unrealistic lighting.

7. **QA and iterate**
   - Check geometry fidelity, scale, door/window positions, ceiling height, circulation, buildability, material logic, light source plausibility, and client risk.
   - Save outputs with prompt, date, scene name, and iteration notes.

## Output pattern

```text
AI Render 任务：
SketchUp 场景准备：
推荐相机：
Prompt：
Negative Prompt：
Influence 建议：
需要手动点击：
输出命名：
QA 检查：
下一轮迭代：
```

## Safety rules

- Treat AI Render as a cloud/generative workflow. Do not upload confidential client drawings, private addresses, faces, or unpublished commercial assets unless the user explicitly approves.
- Mark generated images as “AI concept render / 非施工承诺”.
- Never let AI output override construction feasibility; verify with drawings, dimensions, and material samples.
- If the MCP server is offline, provide manual SketchUp steps and ask the user to start MCP only if live model edits are required.
