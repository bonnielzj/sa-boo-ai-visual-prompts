---
name: sketchup-1001bit-architectural-tools
description: SketchUp 1001bit Tools Freeware 1.0.5 workflow for SketchUp 2025 architectural and interior hard-modeling utilities. Use when Codex needs to plan, prepare, audit, or guide fast white-model and hardscape generation such as walls, openings, door/window frames, stairs, spiral stairs, escalator-like steps, rafters, roofs, louvres, grilles, screens, panels, arrays, edge/face helper operations, chamfers/fillets, simple construction geometry, or when deciding between 1001bit, Profile Builder, MyPanelGrid, Edge Tools, TrueBend, Soap Skin Bubble, Artisan, or native SketchUp tools.
---

# SketchUp 1001bit Architectural Tools

Use this skill to guide architectural and interior hard-modeling workflows with 1001bit Tools Freeware. Treat it as a B-level utility toolkit for fast white-model production and architectural components, not as the main high-end parametric/modeling system.

Codex usually cannot click individual 1001bit tools directly; prepare the modeling sequence, geometric prerequisites, plugin choice, cleanup, naming, and QA. Use SketchUp MCP for file checks, simple geometry creation, organization, or model inspection where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/1001bit_freeware_v1.0.5.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/1001bit_freeware.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/1001bit_freeware/`
- Extension name: `1001bit tools`.
- Version: `freeware 1.0.5`.
- Creator: `Goh Chun Hee, GohCH`.
- Extension Warehouse ID: `e5b1211a-8d1a-4813-bdc3-b321e5477d7b`.
- Version ID: `fbd307e2-d0f0-4880-9568-80d2032f0ffe`.
- Package contents: Ruby loader, encrypted `.rbs` tool files, HTML dialogs, icons; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Transparency note: many implementation files are encrypted `.rbs`, so use more conservatively than fully readable Ruby plugins.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present, menu loader present, and extension listed as loaded in the current session.

Read `references/1001bit-workflow.md` for detailed tool grouping, decision rules, and QA.

## Core workflow

1. **Decide whether 1001bit is the right tool**
   - Use 1001bit for quick architecture/white-model utilities: walls, openings, frames, stairs, louvres, grilles, roofs, arrays, simple chamfers/fillets, helper construction geometry.
   - Use Profile Builder for repeatable profile assemblies, trims, mouldings, slats, frames, and construction-like components that need reuse and controlled profiles.
   - Use MyPanelGrid for regular floor/wall/ceiling panel layouts.
   - Use Edge Tools² for CAD cleanup, gap closing, collinear cleanup, stray edges, and edge repair.
   - Use TrueBend for precise bending of linear objects.
   - Use Soap Skin Bubble or Artisan for membranes, soft surfaces, and organic geometry.

2. **Prepare modeling intent**
   - Identify the target category: wall/opening, stairs, roof/rafter, louvre/grille/screen, array/panel, edge helper, or face helper.
   - Work on a copy for client-visible models; some 1001bit commands generate raw geometry quickly and may need cleanup.
   - Keep CAD import and final render model organized with tags/groups.
   - For old-tool reliability, test the command on a small sample before applying to the main room/model.

3. **Use 1001bit for fast generation**
   - Choose the relevant 1001bit menu/tool based on the target geometry.
   - Use practical project dimensions, not arbitrary defaults.
   - Immediately group generated geometry and name it with a prefix such as `1001_Wall_`, `1001_Stair_`, `1001_Louvre_`, or `1001_Frame_`.
   - Delete or hide failed experiments instead of leaving duplicate raw edges.

4. **Refine with the rest of the plugin stack**
   - Use Edge Tools² after generation if edges/faces are fragmented.
   - Use Solid Inspector if generated forms must be solid/manifold.
   - Use Profile Builder to rebuild final trims, frames, or slat assemblies if 1001bit output is only a white-model placeholder.
   - Use Material Replacer and Texture Positioning before render handoff.
   - Use Advanced Camera Tools / Curic Align View to capture elevation or client proposal views.

5. **QA before keeping result**
   - Geometry is grouped/componentized.
   - Scale/dimensions match design intent.
   - No stray edges, duplicate faces, reversed faces, or tiny broken fragments.
   - Generated architectural element is appropriate for white-model, construction study, or render model.
   - If the plugin command behaved oddly, revert and use native/Profile Builder/manual modeling instead.

## Output pattern

```text
建模目标：
对象类型：墙体 / 门窗洞 / 楼梯 / 百叶 / 格栅 / 屏风 / 屋顶 / 阵列 / 辅助线面
建议工具：1001bit / Profile Builder / MyPanelGrid / Edge Tools / TrueBend / 其他
准备工作：尺寸、基准线/边界、分组、备份、CAD清理
操作步骤：
后续处理：分组命名 / 清理 / 修实体 / 材质 / 相机视图
QA 检查：
```
