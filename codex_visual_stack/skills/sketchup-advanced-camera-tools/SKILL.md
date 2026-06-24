---
name: sketchup-advanced-camera-tools
description: SketchUp Advanced Camera Tools 1.3.4 workflow for SketchUp 2025 physical camera planning, cinematographic composition, focal length/aspect-ratio control, safe zones, camera frustums, camera locking, look-through views, interior render shot lists, white-model-to-AI-render source cameras, and consistent proposal/D5/Enscape/Twinmotion export scenes. Use when Codex needs to plan, prepare, audit, or guide camera setup and scene composition in SketchUp interior-design models.
---

# SketchUp Advanced Camera Tools

Use this skill to plan real-world camera views in SketchUp before rendering, AI Render, D5/Enscape/Twinmotion export, screenshots, or proposal plates. Advanced Camera Tools (ACT) is best for repeatable named physical cameras with controlled focal length, aspect ratio, safe zones, and frustum visibility.

Codex usually cannot click the ACT toolbar directly; prepare model/camera requirements, create scene/camera naming plans, suggest manual ACT steps, and use SketchUp MCP for read-only checks or camera/scene support where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/su_advancedcameratools-1.3.4.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_advancedcameratools.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_advancedcameratools/`
- Installed version from loader: `1.3.4`.
- Creator: SketchUp / Trimble.
- Package contents: Ruby loader, encrypted `.rbe` files, camera preset `.skp` assets, `cameradata/cameras.csv`, icons, localized strings, and `.susig`; no `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If `matching_extensions` is empty, SketchUp was not restarted after file install.

Read `references/advanced-camera-tools-workflow.md` for detailed install checks, camera recipes, and QA.

## Core workflow

1. **Define the deliverable**
   - Spatial mood render: perspective camera with controlled focal length.
   - True front/elevation: use Curic Align View or native parallel projection instead; ACT is for physical camera/render framing.
   - AI Render source: clear clay/white-model image with strong geometry and prompt-friendly composition.
   - Proposal set: repeatable scenes with same aspect ratio, camera height, and focal-length logic.

2. **Choose camera language**
   - Interior overview: 24–28 mm equivalent, but avoid over-wide distortion.
   - Human-eye/client view: 30–35 mm equivalent, camera height around 1.3–1.6 m.
   - Detail/material shot: 50–85 mm equivalent, tighter crop, less distortion.
   - Hero/commercial shot: 35–50 mm equivalent, deliberate foreground/midground/background layering.

3. **Create ACT camera manually in SketchUp**
   - Open ACT from `Tools > Advanced Camera Tools` or its toolbar.
   - Use `Create Camera` and choose a suitable camera/format preset.
   - Place the camera, use `Look Through Camera`, then adjust pan/tilt/roll, focal length, and framing.
   - Show safe zones/frustum only when useful for setup; hide them before final export unless intentionally documenting camera setup.
   - Lock camera after approval to prevent accidental drift.

4. **Save and name scenes deliberately**
   - `CAM_ACT_Living_Hero_35mm_16x9_01`
   - `CAM_ACT_Kitchen_Dining_28mm_16x9_01`
   - `CAM_ACT_Bedroom_Detail_55mm_4x5_01`
   - `CAM_AIRender_WhiteModel_Living_35mm_01`

5. **Integrate with render/prompt workflows**
   - Pair the scene name with material/light prompts for AI Render.
   - Keep camera locked while iterating material, lighting, and furniture options.
   - Duplicate scenes for option A/B rather than moving the camera.

6. **QA before export**
   - Vertical lines are not unintentionally tilted.
   - No excessive wide-angle stretching at frame edges.
   - Main furniture is not clipped awkwardly.
   - Door/window openings and ceiling/floor planes clarify space volume.
   - Aspect ratio matches final destination: 16:9, 4:5, 1:1, A3 landscape, etc.

## Output pattern

```text
镜头目标：
空间/对象：
ACT 相机类型/画幅：
焦距建议：
相机高度/视线：
安全框/构图：
场景命名：
后续用途：AI Render / D5 / Enscape / Twinmotion / 提案PDF
QA 检查：
```
