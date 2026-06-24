---
name: sketchup-selection-toys-selection-control
description: SketchUp Selection Toys 2.4.0 workflow for SketchUp 2025 selection filtering and selection manipulation. Use when Codex needs to plan, prepare, audit, or guide advanced selection tasks in SketchUp such as selecting only edges/faces/groups/components, deselecting entity types, selecting hidden/soft/smooth/border edges, selecting by material/layer, selecting similar component/group instances, selecting connected coplanar/parallel/perpendicular faces, handling CAD-import cleanup, isolating problematic geometry, preparing selections before Edge Tools/CleanUp/Solid Inspector/Material Replacer/Profile Builder, or improving model cleanup precision.
---

# SketchUp Selection Toys Selection Control

Use this skill when selection precision is the bottleneck in SketchUp 2025. Selection Toys is not a geometry repair tool by itself; it makes cleanup, material replacement, CAD-import filtering, and modeling operations faster and safer by selecting the right entities first.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source RBZ: `/Users/bonnie/Downloads/tt_selection_toys-2.4.0.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_selection_toys.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_selection_toys/`
- Extension name: `Selection Toys`.
- Version: `2.4.0`.
- Creator: `Thomas Thomassen (thomas@thomthom.net)`.
- Safety: pure Ruby/HTML/JS/icons; no native binaries found in package.
- Current MCP validation on install: extension registered and loaded in SketchUp `25.0.659`, Ruby `3.2.2`.

Read `references/selection-toys-workflow.md` for CAD cleanup recipes, command groups, and QA checks.

## Core workflow

1. **Define what must be selected**
   - Entity type: edges, faces, groups, components, guides, text, images, section planes.
   - Geometry condition: hidden, soft, smooth, border edges, curves, arcs, circles, polygons.
   - Relationship: same material, same layer/tag, connected coplanar/parallel/perpendicular faces, similar instances.

2. **Work in the right context**
   - Enter the relevant group/component before filtering local imported CAD or furniture geometry.
   - Keep raw CAD references grouped and locked when they should not be edited.
   - Use active-context commands when only the current editing context should be affected.

3. **Filter before action**
   - Use `Select Only` to reduce a messy selection to the target type.
   - Use `Deselect` to remove protected or irrelevant types from a selection.
   - Use same material/layer selection before material cleanup or tag cleanup.
   - Use hidden/soft/smooth/border edge filters before cleanup, face creation, or render QA.

4. **Hand off to the next tool**
   - Edge gaps/stray linework → `sketchup-edge-tools-cleanup`.
   - Whole-model cleanup → CleanUp³ if installed, or manual cleanup.
   - Solid repair → `sketchup-solid-inspector-repair`.
   - Batch material swap → `sketchup-material-replacer`.
   - Profile/path work → `sketchup-profile-builder` after path selection is clean.

5. **QA after selection-based operations**
   - Confirm the selection did not include locked references, intentional detail lines, or nested geometry outside the target context.
   - Undo immediately if a filter command selected too broadly.
   - Work on copies when converting groups to components or deleting large selected sets.

## Output pattern

```text
Selection goal:
Target context:
Recommended Selection Toys command/filter:
Protected geometry to avoid:
Next operation/tool:
QA checks:
```
