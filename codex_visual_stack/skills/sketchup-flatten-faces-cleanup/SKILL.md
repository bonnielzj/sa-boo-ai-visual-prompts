---
name: sketchup-flatten-faces-cleanup
description: SketchUp Unwrap and Flatten Faces 2.6 workflow for SketchUp 2025 cleanup, panel flattening, and surface preparation. Use when Codex needs to plan, prepare, audit, or guide flattening selected SketchUp faces, unwrapping non-coplanar faces, smashing/projecting geometry to X/Y/Z planes, preparing CAD/imported surfaces for 2D cleanup, CNC/laser cutting, texture layout, material studies, white-model panel extraction, or diagnosing why a face set should be flattened before downstream modeling/rendering.
---

# SketchUp Flatten Faces Cleanup

Use this skill to guide the `Unwrap and Flatten Faces` extension by Alexander C. Schreyer in SketchUp 2025. The plugin is best for selected ungrouped faces that need to be copied into a flat grouped result for cleanup, CNC/laser prep, texture studies, or white-model panel extraction.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source RBZ: `/Users/bonnie/Downloads/as_flatten_2-6.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/as_flatten.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/as_flatten/`
- Extension name: `Unwrap and Flatten Faces`.
- Version: `2.6`.
- Creator: `Alexander C. Schreyer, www.alexschreyer.net`.
- Current MCP validation on install: extension registered and loaded in SketchUp `25.0.659`, Ruby `3.2.2`.

Read `references/flatten-faces-workflow.md` for command choice, settings, QA, and MCP checks.

## Core workflow

1. **Decide flattening intent**
   - Use `Unwrap` when adjacent non-coplanar faces need to lay out as connected panels with minimal distortion.
   - Use `Smash`/projection when geometry should be projected to an axis plane for a clean 2D reference.
   - Do not use it as a general mesh repair tool; pair with Edge Tools, Solid Inspector, Artisan, or Soap Skin Bubble as needed.

2. **Prepare selection**
   - Save a version or duplicate the source group/component.
   - Enter the correct group/component context.
   - Select **ungrouped faces** inside that context; explode only a temporary copy if needed.
   - Avoid selecting dimensions, edges alone, nested components, furniture blocks, or hidden construction geometry.

3. **Run the plugin conservatively**
   - Find the command under the Tools menu or context menu after selecting faces.
   - For complex organic surfaces, run on fewer faces first; the plugin notes that automatic unwrapping can vary by run.
   - Use colorizing when you need to match flattened panels back to the 3D source.
   - Set target plane to match output need: usually `Z_AXIS` for plan-like XY output; `X_AXIS` or `Y_AXIS` for elevation-like projection.

4. **QA result before downstream use**
   - Confirm the original geometry is preserved and the result is a separate group.
   - Check panel count, orientation, overlap, scale, and face direction.
   - Dimension critical edges before sending to CNC/laser/cutting.
   - If unwrap fails or overlaps, retry with fewer faces or split at logical seams.

## Output pattern

```text
Flattening goal:
Target geometry/context:
Recommended command: Unwrap / Smash / axis projection
Selection prep:
Settings:
Manual operation steps:
Risks / seams / distortion notes:
QA checks:
Next plugin handoff:
```
