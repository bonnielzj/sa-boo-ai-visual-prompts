---
name: sketchup-truebend-bending
description: SketchUp True Bend 1.2.1 workflow for SketchUp 2025 precise length-preserving bending of groups/components. Use when Codex needs to plan, prepare, audit, or guide bending linear interior objects such as trims, mouldings, slats, wall panels, curved counters, arches, railings, cabinet details, furniture ribs, decorative strips, white-model blocks, and profile assemblies; or decide when to use TrueBend versus SketchyFFD, Artisan, FredoScale, Profile Builder, or native modeling.
---

# SketchUp TrueBend Bending

Use this skill to guide precise one-axis bending in SketchUp with ThomThom True Bend. TrueBend bends a selected group/component to a given angle while preserving the original length, making it useful for converting straight assemblies into controlled curved pieces.

Codex usually cannot click the TrueBend tool directly; prepare the geometry, segmentation, axis/orientation, angle/radius intent, QA checks, and follow-up modeling/render steps. Use SketchUp MCP for file checks, model organization, scene setup, or simple geometry creation where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/tt_truebend-1.2.1.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_truebend.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_truebend/`
- Extension name: `True Bend`.
- Version: `1.2.1`.
- Creator: `Thomas Thomassen` / ThomThom.
- License: MIT License.
- Package contents: readable Ruby source, icons, JSON metadata, bundled error reporter UI resources; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Dependency note: package scan found no `TT_Lib2`, `LibFredo`, or Fredo dependency. Existing TT_Lib² may remain useful for other ThomThom plugins but is not required by this package scan.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed in SketchUp, fully quit and reopen SketchUp after file install.
- Privacy note: bundled error reporter can show/send crash reports if an exception occurs; treat as low risk but avoid sending project-sensitive details in optional report text.

Read `references/truebend-workflow.md` for detailed decision rules, interior use cases, and QA.

## Core workflow

1. **Decide if TrueBend is the right tool**
   - Use TrueBend for controlled arc bending of a straight group/component where original length matters.
   - Use SketchyFFD for free-form cage warping, organic bulges, or non-uniform concept deformation.
   - Use Artisan for subdivision sculpting, cushions, soft furniture, and smoothed organic surfaces.
   - Use Profile Builder first when the object is a repeatable straight profile/assembly; then use TrueBend on a copied assembly if a curved version is needed.
   - Use FredoScale when available for broader deformation types such as twist, taper, box scale, or alternate bend controls.

2. **Prepare geometry**
   - Work on a copy; keep the original straight object hidden/tagged as backup.
   - Make the target exactly one group or component; TrueBend activates on one selected group/component.
   - Orient the object so the bend length runs along the local X axis; zero X length cannot bend.
   - Add enough lengthwise segments before bending. Low-segment objects bend faceted; trim/panel/slat assemblies need subdivisions where curvature should appear.
   - Clean imported CAD/mesh edges with Edge Tools or native cleanup if faces are fragmented.

3. **Bend deliberately**
   - Select one group/component.
   - Run `Tools > TrueBend` or the TrueBend toolbar/context menu.
   - Drag the handle or type the intended angle in the VCB/measurements box.
   - Start with 30°, 45°, 90°, 180°, or project-specific radius/angle studies; keep a duplicate for each option.
   - Check plan/elevation/camera while bending; curved geometry can drift visually even when length is preserved.

4. **Integrate into the model**
   - Name results clearly, e.g. `TB_CurvedSlatWall_R2400_01`, `TB_ArchTrim_90deg_01`, `TB_CounterFront_Curve_01`.
   - Pair with Material Replacer and Texture Positioning after bending because UV/texture direction may need correction.
   - Pair with Solid Inspector when the bent result must remain manifold/boolean-ready.
   - Pair with Advanced Camera Tools / Curic Align View to capture before/after or elevation-like views.

5. **QA before finalizing**
   - Original backup exists.
   - Bend direction and angle match the design intent.
   - Segment density is smooth enough for render but not excessive.
   - No broken faces, reversed faces, self-intersections, or distorted components.
   - Dimensions/clearances remain plausible for construction and furniture use.

## Output pattern

```text
弯曲目标：
对象类型：线脚 / 格栅 / 墙板 / 柜体 / 家具 / 装置 / 白模体块
建议工具：TrueBend / Profile Builder+TrueBend / SketchyFFD / Artisan / 其他
准备工作：成组/组件、X轴方向、分段、备份、清理
弯曲参数：角度 / 半径意图 / 分段密度 / 版本编号
操作步骤：
后续处理：修面 / 平滑 / 材质UV / 实体检查 / 场景
QA 检查：
```
