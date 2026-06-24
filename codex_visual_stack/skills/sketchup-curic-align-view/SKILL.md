---
name: sketchup-curic-align-view
description: SketchUp Curic Align View 1.2.1 workflow for SketchUp 2025 camera, elevation, section, and presentation view alignment. Use when Codex needs to plan, prepare, audit, or guide aligned views from faces/edges/objects, orthographic elevation-like scenes, interior wall elevations, cabinet/front views, material detail views, camera locking, FOV consistency, spin/rotation view corrections, render-ready SketchUp scenes, AI Render source views, before-after camera matching, and proposal screenshot/export composition.
---

# SketchUp Curic Align View

Use this skill to create clean, repeatable SketchUp views aligned to faces, walls, cabinetry, elevations, detail planes, or selected geometry. Curic Align View helps make model views presentation-ready before screenshots, AI Render, D5/Enscape export, Figma/PDF proposal pages, or construction/elevation review.

Codex usually cannot click the Curic toolbar directly; prepare the model, name target planes/scenes, suggest manual Curic steps, and use SketchUp MCP for camera/scene creation, viewport exports, and verification where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Curic Align View source package: `/Users/bonnie/Downloads/su插件/curic_align_view_v1.2.1.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/curic_align_view.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/curic_align_view/`
- Installed version from loader: `1.2.1`.
- Creator: Vo Quoc Hai / Curic.
- Package contents: Ruby loader, encrypted `.rbe` files, and icons; no `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found.

Read `references/curic-align-view-workflow.md` for installation checks, view recipes, and QA.

## Core workflow

1. **Define the view purpose**
   - Wall/elevation review: align to selected wall face and use parallel projection.
   - Cabinet/millwork front: align to cabinet front plane and lock a scene.
   - Material/detail shot: align to feature plane, set consistent FOV, crop tightly.
   - AI Render source: align to a clear perspective/orthographic base image for predictable generation.
   - Before/after comparison: lock one camera and reuse it for both states.

2. **Prepare target geometry**
   - Select or isolate the reference face/edge/object.
   - Ensure the target plane is actually planar and not a nested hidden face.
   - Hide construction clutter, guides, and irrelevant tags.
   - Set section planes if the aligned view needs interior cutaway depth.

3. **Align and refine**
   - Use Curic Align View to align current view to face/edge/standard direction.
   - Switch between perspective and parallel projection depending on deliverable.
   - Correct rotation/spin so verticals/horizontals read cleanly.
   - Adjust FOV or zoom consistently across comparable views.
   - Lock/save the camera as a named SketchUp Scene.

4. **Name scene deliberately**
   - `CAM_Living_TVWall_Elev_01`
   - `CAM_Kitchen_CabinetFront_01`
   - `CAM_Bedroom_Headboard_Material_01`
   - `CAM_AIRender_Living_WhiteModel_01`

5. **QA**
   - Vertical lines are vertical unless intentionally dynamic.
   - Wall/cabinet plane is not skewed.
   - Door/window/furniture proportions remain readable.
   - Before/after scenes have same camera, crop, projection, FOV, and visible tags.

## Output pattern

```text
视图目标：
目标面/对象：
投影方式：Perspective / Parallel Projection
Curic Align View 操作：
相机/FOV/旋转建议：
场景命名：
导出用途：AI Render / D5 / Enscape / PDF / Figma
QA 检查：
```
