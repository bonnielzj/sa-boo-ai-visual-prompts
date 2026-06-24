---
name: sketchup-sketchyffd-deformation
description: SketchUp SketchyFFD Classic V7/V7.1 workflow for SketchUp 2025 free-form deformation, control-cage editing, lattice/cage-based mesh manipulation, curved walls, soft furniture massing, sculptural interior forms, organic panels, bent grids, warped white-model blocks, and concept-stage shape exploration. Use when Codex needs to plan, prepare, audit, or guide FFD-style deformation in SketchUp and decide when to use SketchyFFD versus Artisan, FredoScale, Profile Builder, or native modeling.
---

# SketchUp SketchyFFD Deformation

Use this skill to guide free-form deformation in SketchUp with SketchyFFD Classic. SketchyFFD adds a control cage to a selected object so the mesh can be manipulated through control points. It is best for concept-stage shape exploration: bending, bulging, tapering, warping, and soft-transforming existing geometry.

Codex usually cannot click SketchyFFD tools directly; prepare the geometry, cage strategy, deformation steps, backup/QA plan, and integration with other modeling plugins. Use SketchUp MCP for read-only checks, grouping, scene setup, or model organization where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/SketchyFFD_v7.1.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_SketchyFFD.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_SketchyFFD/`
- Extension name: `SketchyFFD (Classic)`.
- Loader version: `V7`; source file name indicates `v7.1`.
- Creator: `mind.sight.studios`.
- Package contents: Ruby loader, encrypted `.rbe` files, `.susig`, and `extension_info.txt`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file found.
- MCP check on install confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed, restart SketchUp after file install.

Read `references/sketchyffd-workflow.md` for detailed use cases, decision rules, and QA.

## Core workflow

1. **Decide whether FFD is the right tool**
   - Use SketchyFFD for global soft deformation of an existing object.
   - Use Artisan for subdivision sculpting, cushions, organic smoothing, or detailed soft forms.
   - Use FredoScale for precise taper, bend, twist, stretch, box scaling, and controlled transforms.
   - Use Profile Builder for repeatable trims, frames, slats, mouldings, and construction-like profiles.

2. **Prepare geometry**
   - Work on a copy; keep the original hidden/tagged as backup.
   - Make the target a group/component before deformation.
   - Add enough subdivisions/segments before deformation; FFD cannot make a low-poly object bend smoothly without geometry.
   - Clean stray edges and non-manifold issues if deformation behaves unpredictably.

3. **Create/control cage manually**
   - Select the group/component or mesh to deform.
   - Use SketchyFFD to add a suitable control cage.
   - Choose cage density based on intent:
     - Low density: broad bend/taper/bulge.
     - Medium density: furniture/soft wall shape.
     - Higher density: nuanced sculptural form, but harder to control.

4. **Deform deliberately**
   - Move control points in large, readable gestures first.
   - Keep symmetry by moving paired points consistently.
   - Check from plan, elevation, and camera view.
   - Avoid over-deforming construction-critical elements.

5. **Finalize and integrate**
   - Name the deformed group: `FFD_CurvedWall_Concept_01`, `FFD_SofaBack_Bulge_01`, etc.
   - Pair with Artisan if smoothing/subdivision refinement is needed after FFD.
   - Pair with Solid Inspector if the resulting object needs to remain solid/manifold.
   - Save render camera scenes before/after deformation for option comparison.

6. **QA before keeping result**
   - No accidental self-intersection.
   - Mesh density is enough for smooth render but not too heavy.
   - Furniture/walls still meet functional clearances.
   - Curved elements are visually intentional and buildable or clearly marked as concept-only.

## Output pattern

```text
变形目标：
对象类型：墙面 / 家具 / 天花 / 装置 / 白模体块
建议工具：SketchyFFD / Artisan / FredoScale / 其他
几何准备：分段 / 成组 / 备份 / 清理
控制笼策略：低 / 中 / 高密度，控制点方向
操作步骤：
后续处理：平滑 / 修实体 / 材质 / 渲染场景
QA 检查：
```
