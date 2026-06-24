---
name: sketchup-color-maker-palettes
description: SketchUp DBUR ColorMaker 1.0.0/1.0.1 workflow for SketchUp 2025 standard color material creation, RAL/NCS/Pantone/PMS/Munsell/Resene/Web/X11/AutoCAD/Bootstrap/HTML-SU/Color-temperature palettes, wall paint color studies, brand-color translation, soft-furnishing color schemes, white-model coloring, and material palette setup before Material Replacer, AI Render, D5, Enscape, LightUp, or proposal outputs. Use when Codex needs to plan, prepare, audit, or guide creating SketchUp materials from industry color standards.
---

# SketchUp ColorMaker Palettes

Use this skill to guide creation of standard color materials in SketchUp with DBUR ColorMaker. It is useful for wall paint studies, RAL/NCS/Pantone/brand-color palettes, soft-furnishing color options, white-model zoning colors, and color-temperature reference materials.

Codex usually cannot click the ColorMaker UI directly; prepare the palette choice, color names/codes, material naming, replacement plan, and QA. Use SketchUp MCP for read-only checks, material audits, or scene planning where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/DBUR_ColorMaker_v1.0.1.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DBUR_ColorMaker.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DBUR_ColorMaker/`
- Extension name: `ColorMaker`.
- Loader version: `1.0.0`; source file name indicates `v1.0.1`.
- Creator: `D. Bur` / Didier Bur.
- Package contents: Ruby loader, encrypted `ColorMaker.rbe`, 23 standard color palette text files, CSS/icons, and `ColorMakerHelp.pdf`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present, 23 palette files present. If the extension is not listed, restart SketchUp after file install.

Read `references/colormaker-workflow.md` for palette list, color recipes, and QA.

## Core workflow

1. **Define color purpose**
   - Wall paint / ceiling paint.
   - Brand color translation into spatial materials.
   - Soft furnishing color studies.
   - RAL/NCS/Pantone standard color proposal.
   - Color-temperature reference swatches.
   - White-model zoning or option comparison.

2. **Choose palette standard**
   - RAL/NCS: architectural/interior paint-like standards.
   - Pantone/PMS: brand, graphics, textile/soft furnishing references.
   - Munsell/NBS/Resene/AS/BS/FS: specialist regional or classification references.
   - Web/X11/Bootstrap/HTML-SU: digital/proposal/UI color mapping.
   - Color temperatures: lighting color reference materials, not physical paint.

3. **Create materials manually in ColorMaker**
   - Open ColorMaker after SketchUp restart.
   - Select palette file/standard.
   - Create one selected material or a controlled small set of swatches.
   - Avoid importing a full huge palette unless needed; too many materials clutter the model.

4. **Name and organize materials**
   - Prefer project naming after creation:
     - `MAT_Paint_RAL_1013_OysterWhite`
     - `MAT_Paint_NCS_0502-Y`
     - `MAT_Brand_Pantone_123`
     - `MAT_LightTemp_3000K_Ref`
   - Keep color-code source in material name or notes.

5. **Apply or replace materials**
   - Use native paint bucket for small tests.
   - Pair with `sketchup-material-replacer` for global swaps from placeholder colors.
   - Save A/B/C scenes or model copies for client options.

6. **QA**
   - Treat RGB approximations as visual references; real paint/print colors require physical samples.
   - Do not promise exact Pantone/RAL appearance in SketchUp viewport/render.
   - Check color under lighting conditions with LightUp/D5/Enscape/AI Render.
   - Keep palette small and project-specific.

## Output pattern

```text
色彩目标：墙漆 / 品牌色 / 软装 / 白模分区 / 灯光色温
标准色库：RAL / NCS / Pantone / PMS / Web / Color temperature / 其他
候选色号：
SketchUp 材质命名：
创建方式：ColorMaker 单色 / 小色板 / 全套色库
应用方式：手动上色 / Material Replacer 批量替换
QA 检查：色差 / 光照 / 渲染 / 真实样板确认
```
