---
name: sketchup-stl-import-export
description: SketchUp STL Import & Export 2.2.0 workflow for SketchUp 2025 mesh exchange, product models, and 3D printing. Use when Codex needs to plan, prepare, audit, or guide importing STL meshes into SketchUp, exporting SketchUp groups/components as STL, checking units and scale, repairing solids before STL export, preparing furniture/decor/product prototypes, or coordinating SketchUp with slicers, 3D printing, CNC-adjacent mesh workflows, or external mesh/model tools.
---

# SketchUp STL Import Export

Use this skill to guide the official/community `STL Import & Export` extension in SketchUp 2025. It is useful for product/decor prototypes, 3D printing, mesh exchange, and occasional furniture/detail assets, but it is not a primary interior-rendering material plugin.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source RBZ: `/Users/bonnie/Downloads/sketchup-stl-2.2.0.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/sketchup-stl.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/sketchup-stl/`
- Extension name: `STL Import & Export`.
- Version: `2.2.0`.
- Creator: `J. Foltz, N. Bromham, K. Shroeder, SketchUp Team`.
- License/source note: open-source project sponsored by the SketchUp team.
- Current MCP validation on install: extension registered and loaded in SketchUp `25.0.659`, Ruby `3.2.2`.

Read `references/stl-workflow.md` for import/export settings, unit checks, solid QA, and MCP verification.

## Core workflow

1. **Decide why STL is needed**
   - Import: bring in product prototypes, scan-like mesh assets, or slicer-ready geometry for reference.
   - Export: send a selected solid group/component to a slicer, print vendor, mesh tool, or prototype workflow.
   - Avoid STL for normal textured render assets because STL does not preserve rich materials, UVs, components, or BIM-like data well.

2. **Control units and scale**
   - Confirm project units before import/export.
   - For interior product details, prefer millimeters unless a vendor specifies another unit.
   - After import, measure one known dimension immediately.

3. **Prepare geometry before export**
   - Export a single clean group/component when possible.
   - Run `sketchup-solid-inspector-repair` before export if the object must be printable or boolean-ready.
   - Orient the object logically for printing/processing.
   - Remove hidden stray faces, internal faces, duplicate shells, and tiny unintended edges.

4. **QA after STL operation**
   - Re-import exported STL into a temporary SketchUp file or slicer to check scale/orientation.
   - Check face orientation, watertightness, and triangle density.
   - Keep the editable SketchUp source file; do not treat STL as the master design file.

## Output pattern

```text
STL goal: import / export / print prep / mesh exchange
Target object/file:
Units:
Solid/manifold status:
Recommended SketchUp STL settings:
Manual operation steps:
Risks:
QA checks:
Next tool handoff:
```
