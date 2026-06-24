---
name: sketchup-architextures-materials
description: SketchUp Architextures 1.1.2254 workflow for SketchUp 2025 seamless material generation and hard-finish texture setup. Use when Codex needs to plan, prepare, audit, or guide creating, importing, editing, scaling, and organizing seamless textures for tiles, wood flooring, stone slabs, brick, terrazzo, concrete, plaster, wallpaper, carpet, fabric-like surfaces, wall/floor/ceiling finishes, white-model-to-material concept studies, or when deciding between Architextures, Poliigon, DBUR ColorMaker, TT Material Replacer, Eneroth Texture Positioning, MyPanelGrid, or render-engine material libraries.
---

# SketchUp Architextures Materials

Use this skill to guide SketchUp material workflows with Architextures. The extension connects SketchUp to the Architextures web material editor/library so hard-finish patterns can be generated or edited as seamless textures and brought into the model at controlled scale.

Codex usually cannot operate the web material editor directly unless the user shares screen/context; prepare the material selection, pattern scale, finish categories, texture QA, plugin handoff, and render-readiness checks. Use SketchUp MCP for file checks, material naming, simple model organization, or material audits where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/Architextures_SUExt.1.1.2254.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/Architextures_SUExt.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/Architextures_SUExt/`
- Extension name after restart: `Architextures`.
- Version: `1.1.2254`.
- Creator: `Informaxyz, for Architextures`.
- Extension Warehouse ID: `1a0e0f80-7186-48da-8dd4-f6337dac0873`.
- Version ID: `0756de47-de98-4e99-ac64-acf2f501558e`.
- Package contents: Ruby loader, encrypted `.rbe` implementation file, icons, `.susig`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Network/account note: Architextures is an online material library/editor. Some downloads/features may depend on account/subscription/usage rights.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed, fully quit and reopen SketchUp after file install.

Read `references/architextures-workflow.md` for detailed material categories, decision rules, and QA.

## Core workflow

1. **Decide if Architextures is the right tool**
   - Use Architextures for seamless, pattern-controlled materials: tile, brick, stone, terrazzo, wood flooring, concrete, plaster, wallpaper, carpet/fabric-like repeating finishes.
   - Use Poliigon for photoreal PBR scans, HDRI, and asset/model libraries.
   - Use DBUR ColorMaker for flat standard colors such as RAL/NCS/Pantone-style color schemes.
   - Use TT Material Replacer to batch swap or standardize materials after testing options.
   - Use Eneroth Texture Positioning to rotate, align, or depattern textures after application.
   - Use MyPanelGrid when the finish needs actual geometric panel/tile grooves or thickness, not only texture.

2. **Prepare material intent**
   - Identify finish category, scale, grout/joint size, color range, and render purpose.
   - Decide whether the material is concept-only, client proposal, or render-ready.
   - Use consistent naming: `AT_Tile_Travertine_600x600_Warm01`, `AT_Wood_Oak_Herringbone_01`, etc.
   - Note if final renderer needs PBR maps beyond SketchUp's viewport texture.

3. **Create/import/edit material**
   - Open Architextures from SketchUp after restart.
   - Choose or create a seamless texture in the Architextures editor.
   - Set physical dimensions before import so SketchUp scale is correct.
   - Apply to a clean face/group/component; avoid applying final textures to messy raw CAD imports.
   - If editing an applied material, use Architextures edit workflow where available.

4. **Refine in SketchUp**
   - Use Texture Positioning for grain direction, tile alignment, wall/floor orientation, and slab seams.
   - Use Material Replacer for option swaps across the model.
   - Use MyPanelGrid/Profile Builder if grooves, trim, edge profiles, or physical seams are required.
   - Use AI Render/D5/Enscape/V-Ray workflow with clear material notes if exporting to another renderer.

5. **QA before client/render output**
   - Pattern scale matches real-world dimensions.
   - Texture direction aligns with design intent.
   - Seam/repeat is acceptable from main camera distances.
   - Material names are clean and grouped by finish family.
   - Usage rights and source are noted for client/commercial output.

## Output pattern

```text
材质目标：
材料类型：瓷砖 / 木地板 / 石材 / 砖 / 水磨石 / 混凝土 / 壁纸 / 地毯 / 其他
建议工具：Architextures / Poliigon / ColorMaker / Texture Positioning / MyPanelGrid / 其他
准备参数：真实尺寸、接缝、颜色、纹理方向、用途
操作步骤：
后续处理：UV对齐 / 批量替换 / 几何分缝 / 渲染材质 / 来源记录
QA 检查：
```
