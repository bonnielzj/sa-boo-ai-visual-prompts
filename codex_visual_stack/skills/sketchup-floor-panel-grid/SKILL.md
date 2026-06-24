---
name: sketchup-floor-panel-grid
description: SketchUp Floor Generator / MyPanelGrid 1.0.0 workflow for SketchUp 2025 floor, wall, ceiling, stone, wood, tile, acoustic, and decorative panel grid generation. Use when Codex needs to plan, prepare, audit, or guide creating regular panel arrays on a selected SketchUp face with panel width, height, thickness, spacing, material selection, partial edge panels, floor/wall feature paneling, tile layouts, veneer/stone slab grids, acoustic wall panels, and interior white-model-to-material detailing.
---

# SketchUp Floor Panel Grid

Use this skill to turn one selected SketchUp face into a grouped grid of raised panels using the installed `Floor Generator` / `MyPanelGrid` extension. It is useful for fast flooring, wall panel, ceiling module, tile, stone slab, wood veneer, acoustic panel, or feature-wall studies.

Codex usually cannot click the toolbar directly; prepare the selected-face requirements, panel dimensions, material choices, and QA checks, then guide the manual plugin run. Use SketchUp MCP for read-only checks, model preparation, scene setup, or verification where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/MyPanelGrid.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/MyPanelGrid.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/MyPanelGrid/`
- Extension menu/toolbar name: `Floor Generator`.
- Installed version from loader: `1.0.0`.
- Creator: `PV Arjun`.
- Package contents: Ruby loader, `main.rb`, two PNG toolbar icons, `.susig`, and `extension_info.txt`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed or `MyPanelGrid` is not defined, restart SketchUp after file install.

Read `references/floor-panel-grid-workflow.md` for install checks, size recipes, and QA.

## Core workflow

1. **Prepare the target face**
   - Select exactly one SketchUp `Face`, not a group/component.
   - Enter the group/component edit context first if the face is nested.
   - Ensure the face is flat, clean, and large enough for at least one panel.
   - For imported CAD faces, repair broken edges first with Edge Tools / native cleanup.

2. **Choose panel intent**
   - Flooring: wood planks, stone slabs, tile modules.
   - Wall: decorative panels, fluted/flat modules, acoustic panels, veneer slabs.
   - Ceiling: modular panels, light-box grid, acoustic ceiling modules.
   - White model: quick raised block grid for material/render ideation.

3. **Run plugin manually**
   - Select the face.
   - Use `Plugins > Floor Generator` or the `Floor Generator` toolbar button.
   - Choose an existing material or `Create New...`.
   - Enter:
     - Panel Width in cm.
     - Panel Height in cm.
     - Panel Thickness in mm.
     - Spacing Between Panels in mm.

4. **Understand generated output**
   - The plugin creates a new group in active entities.
   - It computes a grid from the selected face bounding area in local axes.
   - It adds partial edge panels when residual width/height is sufficient.
   - It pushpulls each panel by thickness and applies the chosen material.

5. **Post-process**
   - Rename the generated group, e.g. `PANELGRID_Living_Floor_Wood_01`.
   - Assign a tag/layer if the project uses visibility states.
   - Hide or delete original guide face only after confirming panels align.
   - Use ACT/Curic scenes to preview panel rhythm in render views.

6. **QA before rendering/export**
   - Panel direction follows the desired grain/module axis.
   - Edge partial panels are intentional, not tiny slivers.
   - Thickness is appropriate for scale and does not collide with doors, skirting, or furniture.
   - Material scale/texture direction matches panel direction.
   - Group stays editable and does not merge into existing walls/floors.

## Output pattern

```text
目标面/空间：
面板用途：地面 / 墙面 / 顶面 / 材质白模
面板尺寸：宽 cm × 高 cm
厚度：mm
缝隙：mm
材质：现有材质 / 新建材质
方向控制：沿哪条边/纹理方向
插件操作：Plugins > Floor Generator
生成组命名：
后续处理：材质缩放 / 标签 / 场景 / 渲染
QA 检查：
```
