---
name: sketchup-soap-skin-bubble-surfaces
description: SketchUp Soap Skin Bubble 1.0.36 workflow for SketchUp 2025 membrane, tensile, soap-skin, bubble, canopy, smooth surface, soft curved panel, dome, sail, cushion-like, and organic surface generation. Use when Codex needs to plan, prepare, audit, or guide creating surfaces from boundary curves/edges, inflating or pressure-forming a mesh, form-finding concept membranes, sculptural ceilings, stretched fabric-like features, curved wall panels, decorative installations, furniture shell studies, or when deciding between Soap Skin Bubble, Artisan, SketchyFFD, TrueBend, Profile Builder, or native Sandbox tools.
---

# SketchUp Soap Skin Bubble Surfaces

Use this skill to guide membrane and bubble surface creation in SketchUp with Soap Skin Bubble. The plugin creates a subdivided mesh from selected boundary edges/curves, then can inflate/relax it into soap-skin or bubble-like forms.

Codex usually cannot click Soap Skin Bubble tools directly; prepare the boundary, segmentation, surface-density, pressure/form-finding strategy, QA checks, and follow-up modeling/render steps. Use SketchUp MCP for file checks, simple boundary geometry, grouping, scene organization, or QA where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/JL_SoapSkinBubble_v1.0.36.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/SoapSkinBubble.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/SoapSkinBubble/`
- Extension info:
  - `ID=c8d49537-51db-40a7-ac0e-474a244eb525`
  - `VERSION_ID=0cbc13b3-256b-47a9-b94f-7003de02830e`
- Package contents: Ruby loader, encrypted `.rbe` implementation files, icons, HTML help, `.susig`; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Legacy note: package contains `SoapSkinBubble/Help/Segel.swf`, an old Flash help/demo asset. It is not required for the modeling workflow and should be ignored if macOS cannot open it.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed, fully quit and reopen SketchUp after file install.

Read `references/soap-skin-bubble-workflow.md` for detailed use cases, plugin combinations, and QA.

## Core workflow

1. **Decide if Soap Skin Bubble is the right tool**
   - Use Soap Skin Bubble for surfaces generated from a boundary loop: membranes, canopies, tensile forms, cushion panels, soft domes, bubble/pressure surfaces.
   - Use Artisan for subdivision sculpting, smoothing, cushions, and free sculpted organic furniture.
   - Use SketchyFFD for deforming an existing solid/group with a control cage.
   - Use TrueBend for precise length-preserving bending of linear objects.
   - Use Profile Builder/MyPanelGrid for repeatable hard profiles/panels, not relaxed membrane form-finding.
   - Use native Sandbox when terrain-like draped/lofted surfaces are enough.

2. **Prepare boundary geometry**
   - Draw or import a clean closed boundary loop; avoid tiny gaps and duplicated edges.
   - Keep boundary curves simple at first. Complex curves should be rebuilt or simplified before generating the mesh.
   - Group a backup boundary before creating the skin.
   - Decide grid density/segmentation based on scale:
     - Low density for concept white model and quick iterations.
     - Medium density for render studies.
     - High density only for final detail; it can become heavy.

3. **Generate surface**
   - Select the closed boundary edges/curves.
   - Use Soap Skin Bubble to create the initial soap skin/net.
   - Adjust subdivision/grid parameters before accepting when possible.
   - Apply bubble/pressure or form-finding operations if a raised or inflated surface is needed.
   - Save versions: flat skin, low-pressure, high-pressure, edited ratio.

4. **Refine and integrate**
   - Smooth/soften edges after generation.
   - If needed, use Artisan for additional smoothing/sculpting after the base surface is generated.
   - Use Solid Inspector only when the surface needs to become a closed solid; open membrane surfaces are not expected to be solids.
   - Use Texture Positioning for fabric/wood/stone direction after surface creation.
   - Use AI Render/D5/Enscape-style render workflows with clear material prompts: stretched fabric, translucent membrane, acoustic felt, soft leather, plaster, etc.

5. **QA before finalizing**
   - Boundary is closed and backed up.
   - Mesh density is enough for the visual purpose but not too heavy.
   - Surface has no inverted/chaotic triangles or self-intersections.
   - Form reads correctly from camera and orthographic views.
   - Buildability is clarified: conceptual membrane vs constructible curved panel.

## Output pattern

```text
曲面目标：
对象类型：张拉膜 / 穹顶 / 软包 / 曲面墙板 / 天花装置 / 家具壳体 / 白模体块
建议工具：Soap Skin Bubble / Artisan / SketchyFFD / TrueBend / Sandbox / 其他
边界准备：闭合边界、分段、备份、清理
生成参数：网格密度、压力/鼓起程度、版本编号
操作步骤：
后续处理：平滑 / 厚度 / 材质UV / 渲染场景 / 可施工性说明
QA 检查：
```
