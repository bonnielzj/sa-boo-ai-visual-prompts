---
name: sketchup-s4u-slice-section-cuts
description: SketchUp s4u Slice 5.2.2 workflow for SketchUp 2025 slicing, cutting, detaching, group sections, section-cut geometry, exploded details, construction slices, cutaway views, model analysis, and interior detail presentation. Use when Codex needs to plan, prepare, audit, or guide cutting objects by plane/edge/face/section, splitting or detaching geometry, creating physical section groups, producing exploded axonometric or construction-layer studies, or deciding between s4u Slice, native Section Plane, Solid Tools, BoolTools, Edge Tools, Profile Builder, or manual modeling.
---

# SketchUp s4u Slice Section Cuts

Use this skill to guide cutting and slicing workflows in SketchUp with s4u Slice. It is best for turning design/analysis section intent into actual separated geometry or section groups, not just a visual section plane.

Codex usually cannot click s4u tools directly; prepare the cut strategy, backup, grouping, plane definition, cleanup, material/scene organization, and QA. Use SketchUp MCP for file checks, simple geometry, layer/tag organization, scene setup, or model inspection where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/s4u_slice_v5.2.2.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/s4u_slice.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/s4u_slice/`
- Extension name after restart should appear like `s4u-Slice` or localized equivalent.
- Version: `5.2.2`.
- Creator: `Suforyou` / `Huynh Duong Phuong Vi`.
- Extension Warehouse ID: `c568655c-a0b4-41b8-873e-ecd1bb2452cb`.
- Version ID: `548eec38-7f97-47ed-ac7d-740768776f9a`.
- Package contents: Ruby loader, encrypted `.rbe` files, localized strings, icons, settings; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Licensing note: s4u tools may require trial/activation/purchase depending on installation state. Use legitimate licensing if prompted.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed, fully quit and reopen SketchUp after file install.

Read `references/s4u-slice-workflow.md` for detailed decision rules, cut recipes, and QA.

## Core workflow

1. **Decide if s4u Slice is the right tool**
   - Use s4u Slice when you need actual split/cut/detached geometry or a grouped physical section.
   - Use native Section Plane when you only need a non-destructive visual cut for presentation.
   - Use Solid Tools/BoolTools when you need boolean operations on clean solids.
   - Use Edge Tools² before slicing if imported CAD/model geometry has broken edges or bad faces.
   - Use Profile Builder after slicing to rebuild clean trims, section caps, frames, or construction layers.

2. **Prepare the model**
   - Save a copy or duplicate target groups/components before destructive cuts.
   - Group or componentize targets; avoid slicing loose raw model-wide geometry.
   - Decide cut intent: analysis section, exploded layer, construction slice, detail reveal, or detachable piece.
   - Define cut plane method: section plane, selected face, selected edge/axis, 2/3-point plane, or tool-specific plane option.
   - Hide/lock unrelated geometry to avoid accidental slicing.

3. **Execute slicing/cutting manually**
   - Select target objects and the intended cut reference according to the s4u Slice command.
   - Choose Slice / Cut / Detach / Section mode based on the goal.
   - Keep generated pieces grouped and named immediately.
   - Save alternate versions for major cut options.

4. **Clean and present**
   - Inspect cut faces, reversed faces, open edges, and tiny fragments.
   - Use Solid Inspector if resulting pieces need to be solid/manifold.
   - Assign section/cut-face materials if helpful: white clay, red cut plane, construction layers.
   - Use Curic Align View or Advanced Camera Tools to create clean section/elevation/axon scenes.
   - Use Material Replacer to standardize cut-face or layer-study materials.

5. **QA before finalizing**
   - Original uncut version exists.
   - Cuts only affected intended groups/components.
   - New pieces are named and grouped.
   - Cut surfaces are visually clean from proposal camera and orthographic views.
   - If output is construction-facing, dimensions and layer thicknesses are checked.

## Output pattern

```text
切割目标：
对象类型：墙体 / 家具 / 柜体 / 构造层 / 白模体块 / 细部节点
建议工具：s4u Slice / 原生 Section Plane / Solid Tools / Edge Tools / 其他
准备工作：备份、分组、切割平面、隐藏无关对象、清理
切割方式：Slice / Cut / Detach / Group Section / 可视剖切
操作步骤：
后续处理：分组命名 / 修面 / 材质 / 场景 / 尺寸检查
QA 检查：
```
