---
name: sketchup-material-replacer
description: SketchUp TT Material Replacer 1.3.0 workflow for SketchUp 2025 batch material replacement, material cleanup, scheme A/B swaps, replacing default or wrong imported materials, render-prep material standardization, white-model-to-finish material iteration, and model-wide front/back material replacement. Use when Codex needs to plan, prepare, audit, or guide replacing one material with another in a SketchUp interior design model using ThomThom Material Replacer and TT_Lib².
---

# SketchUp Material Replacer

Use this skill to guide fast model-wide material replacement in SketchUp with ThomThom Material Replacer. The tool lets the user pick a material to replace, then pick another material to replace it with. It changes matching front/back/entity materials across model entities and component definitions.

Codex usually cannot click the Material Replacer tool directly; prepare the material strategy, naming, backup, and QA sequence, then guide the manual tool operation. Use SketchUp MCP for read-only checks, material listing, scene setup, or scripted material audits when useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/tt_material_replacer-1.3.0.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_material_replacer.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_material_replacer/`
- Extension name: `Material Replacer`.
- Installed version: `1.3.0`.
- Creator: Thomas Thomassen / ThomThom.
- Dependency: `TT_Lib² >= 2.7.0`; installed `TT_Lib² 2.15.1` is present.
- Package contents: two Ruby source files, `.susig`, and `extension_info.txt`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files and TT_Lib² files present. If the extension is not listed, restart SketchUp after file install.

Read `references/material-replacer-workflow.md` for install checks, material-swap recipes, and QA.

## Core workflow

1. **Define replacement intent**
   - Cleanup: replace messy imported materials with clean project materials.
   - Scheme swap: wood A to wood B, stone A to stone B, wall paint A to wall paint B.
   - White model: replace default/clay materials with design-option materials.
   - Render prep: standardize materials before AI Render, D5, Enscape, or LightUp checks.

2. **Prepare material names**
   - Rename materials clearly before swapping:
     - `MAT_Wall_Paint_WarmWhite_A`
     - `MAT_Wood_Oak_Natural_A`
     - `MAT_Stone_Travertine_B`
   - Create the replacement material before running the tool.
   - Save a model copy or duplicate scene/state for A/B comparisons.

3. **Run plugin manually**
   - Use `Tools > Material Replacer`.
   - First click: pick the material to replace.
   - Second click: pick the replacement material.
   - The tool then replaces matching materials across model entities and component definitions.

4. **Verify scope**
   - It can affect nested component definitions, not only visible active context.
   - It handles front and back materials.
   - If two materials look similar, temporarily rename or color-code them before replacement.

5. **QA after swap**
   - Check hero camera views and aligned elevations.
   - Check hidden/nested components and back faces if relevant.
   - Purge unused materials only after confirming the swap is correct.
   - Keep option copies when client comparison is needed.

## Output pattern

```text
替换目标：清理 / 方案A-B / 渲染准备 / 白模转材质
原材质：
新材质：
影响范围：模型全局 / 组件定义 / 正反面
操作步骤：Tools > Material Replacer → 先点原材质 → 再点新材质
备份策略：
QA 检查：
后续：Purge / 场景导出 / AI Render / D5 / Enscape
```
