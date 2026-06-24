---
name: sketchup-texture-positioning
description: SketchUp Eneroth Texture Positioning Tools 1.0.3 workflow for SketchUp 2025 texture/UV alignment, rotating textures 90° or custom angles, aligning textures to face edges or a selected edge, depatternizing repeated textures, and render-prep QA for wood grain, stone slabs, tile, brick, wallpaper, fabric, leather, rugs, panel grids, and imported model materials. Use when Codex needs to plan, prepare, audit, or guide texture direction/position cleanup in SketchUp before AI Render, D5, Enscape, LightUp, screenshots, or material proposals.
---

# SketchUp Texture Positioning

Use this skill to guide texture direction and UV cleanup in SketchUp with Eneroth Texture Positioning Tools. It is useful after materials exist: align wood grain, rotate tile/stone/wallpaper, align textures to an edge, or randomize texture offsets to reduce visible repetition.

Codex usually cannot click the toolbar directly; prepare the face selection, reference edge, rotation angle, depatternizing strategy, and QA. Use SketchUp MCP for read-only checks, scene planning, or material audits where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/ene_texturepositioning_v1.0.3.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/ene_texturepositioning.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/ene_texturepositioning/`
- Extension name: `Eneroth Texture Positioning Tools`.
- Installed version: `1.0.3`.
- Creator: Julia Christina Eneroth / Eneroth3.
- Package contents: Ruby source files, PNG icons, and `extension_info.txt`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files and icons present. If the extension is not listed, restart SketchUp after file install.

Read `references/texture-positioning-workflow.md` for command behavior, material recipes, and QA.

## Core workflow

1. **Define texture problem**
   - Direction wrong: wood grain, fabric weave, stone vein, tile line rotates incorrectly.
   - Multi-face mismatch: adjacent faces have inconsistent orientation.
   - Need edge alignment: align all selected faces to one selected edge.
   - Repetition visible: pattern repeats too obviously across many faces.

2. **Prepare selection**
   - Select only faces with textured materials.
   - Enter group/component edit context first if needed.
   - For edge alignment, select exactly one reference edge plus the target faces.
   - Save before changing many faces.

3. **Run correct command manually**
   - `Plugins > Texture Positioning > Align Texture`: align each selected face texture to its own face side.
   - `Align Texture To Edge`: align selected faces to one selected edge.
   - `Rotate Clockwise` / `Rotate Counter Clockwise`: rotate selected face textures by 90°.
   - `Rotate Custom angle`: rotate by a custom counter-clockwise angle.
   - `Depatternize`: randomly offset textures to reduce repeated patterning.

4. **Check in render camera**
   - Use locked Advanced Camera Tools scenes for before/after comparison.
   - For wall/floor surfaces, also check aligned/elevation views with Curic Align View.
   - Make sure texture scale is correct; this plugin changes position/orientation, not material dimensions.

5. **QA before rendering**
   - Wood/stone/fabric direction follows design intent.
   - Adjacent faces do not create obvious seams unless intentional.
   - Depatternize improves repetition without looking chaotic.
   - Texture direction still matches construction logic and supplier material direction.

## Output pattern

```text
贴图问题：方向 / 接缝 / 重复图案 / 参考边对齐
材质对象：木纹 / 石材 / 瓷砖 / 墙纸 / 布料 / 皮革 / 地毯
选择策略：哪些 faces，是否需要 reference edge
命令：Align Texture / Align To Edge / Rotate 90 / Custom Angle / Depatternize
角度/方向：
QA 检查：纹理方向 / 接缝 / 比例 / 渲染镜头
后续：Material Replacer / ColorMaker / AI Render / D5 / Enscape
```
