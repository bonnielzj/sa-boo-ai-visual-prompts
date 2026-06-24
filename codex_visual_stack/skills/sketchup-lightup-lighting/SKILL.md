---
name: sketchup-lightup-lighting
description: SketchUp LightUp Demo 7.5.f workflow for SketchUp 2025 realtime lighting, soft lighting previews, daylight and sky-factor checks, IES light testing, point lights, light meters, illumination diagnostics, realtime flythroughs, and render-prep QA for interior design. Use when Codex needs to plan, prepare, audit, or guide lighting studies in SketchUp before AI Render, D5, Enscape, Twinmotion, proposal screenshots, or client lighting discussions.
---

# SketchUp LightUp Lighting

Use this skill to guide LightUp lighting studies inside SketchUp: daylight/sky checks, artificial light previews, IES tests, light meter grids, quick realtime render feedback, and lighting QA before final rendering in AI Render, D5, Enscape, or Twinmotion.

Codex usually cannot click the LightUp toolbar directly; prepare the model, light plan, settings, test scenes, and QA checklist, then guide manual LightUp operations. Use SketchUp MCP for read-only plugin checks, scene/camera planning, and model organization where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/LightUp_Demo.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/lightup.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/lightup/`
- Extension name: `Lightup Tools`.
- Loader version: `7.x`; internal version: `7.5.f`.
- Creator: Adam Billyard / LightUp.
- Package contents include Ruby files, IES libraries, LightUp components, HTML/JS UI, and native render modules. Ruby 3.2 macOS universal/arm64 bundle is present.
- Demo/license limitation: treat as trial/demo until the user confirms license status; do not promise commercial output without checking license terms.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files and Ruby 3.2 macOS bundle present. If extension list is empty, restart SketchUp after file install.

Read `references/lightup-workflow.md` for installation checks, lighting recipes, and QA.

## Core workflow

1. **Define lighting question**
   - Daylight: is the room too dark/bright; where does light reach?
   - Artificial light: are downlights, linear lights, wall washers, and decorative fixtures balanced?
   - Mood preview: does the scene support the intended atmosphere before final renderer setup?
   - Technical check: use light meters/IES to validate illuminance patterns.

2. **Prepare the model**
   - Clean heavy geometry and hide unrelated tags.
   - Assign basic material reflectance logic: white plaster, wood, stone, fabric, glass.
   - Ensure openings, glazing, ceilings, and major furniture are present.
   - Save a separate test scene/model version before running heavy illumination.

3. **Set camera and scene states**
   - Use `sketchup-advanced-camera-tools` for locked perspective render views.
   - Use `sketchup-curic-align-view` for elevation or analysis views.
   - Name scenes: `LU_Daylight_Living_01`, `LU_Night_Downlights_01`, `LU_IES_WallWash_01`.

4. **Run LightUp manually**
   - Enable LightUp tools from SketchUp after restart.
   - Place point lights / IES fixtures / light meter grids as needed.
   - Run illumination preview; adjust light power, color, and fixture spacing.
   - Use daylight/sky-factor style checks when analyzing openings and natural light.

5. **Translate findings to render workflow**
   - Record fixture type, approximate intensity/color temperature, and problem areas.
   - Use findings to set D5/Enscape/Twinmotion lights or AI Render prompts.
   - Export quick screenshots for internal comparison, not final if demo limitations/watermarks apply.

6. **QA**
   - Avoid overexposed ceilings and dead dark corners unless intentional.
   - Check task lighting at kitchen counters, desks, vanities, reading zones.
   - Check wall grazing/washing direction and scallop spacing.
   - Confirm material reflectance does not fake unrealistic brightness.
   - Keep one daylight and one night scene for client explanation.

## Output pattern

```text
灯光目标：日光 / 夜景 / 灯具布点 / IES / 照度检查
空间/镜头：
模型准备：
LightUp 操作：
灯具参数建议：色温 / 强度 / 间距 / 高度
分析输出：截图 / 照度网格 / 问题清单
后续转译：AI Render / D5 / Enscape / Twinmotion
QA 检查：
```
