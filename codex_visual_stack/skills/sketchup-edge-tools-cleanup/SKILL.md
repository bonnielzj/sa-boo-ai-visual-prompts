---
name: sketchup-edge-tools-cleanup
description: SketchUp Edge Tools² 2.2.0 workflow for SketchUp 2025 model cleanup and edge repair. Use when Codex needs to plan, prepare, audit, or guide fixing broken imported CAD/DWG linework, closing edge gaps, finding open vertices, erasing stray curves, simplifying curves, making vertices co-linear, dividing faces, cleaning paths before Profile Builder/Fredo/Artisan/Skatter workflows, or diagnosing why SketchUp faces will not form. Requires TT_Lib² version 2.7.0 or newer to be installed before the extension can fully load.
---

# SketchUp Edge Tools Cleanup

Use this skill to repair and simplify SketchUp edge geometry before modeling, rendering, or downstream plugins. Edge Tools² is most valuable after importing DWG/DXF linework, tracing floor plans, preparing trim/panel paths, cleaning curves for Profile Builder, or fixing surfaces before Push/Pull and Skatter hosts.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Edge Tools² source package: `/Users/bonnie/Downloads/su插件/tt_edgetools-2.2.0.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_edgetools.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_edgetools/`
- Installed version from loader: `2.2.0`.
- Creator: Thomas Thomassen / ThomThom.
- Dependency: `TT_Lib²` version 2.7.0 or newer is required. TT_Lib² version 2.15.1 is installed in the SketchUp 2025 Plugins folder; restart SketchUp after installation so Edge Tools² can load against it.

Read `references/edge-tools-2-workflow.md` for dependency checks, commands, and cleanup recipes.

## Core workflow

1. **Decide cleanup scope**
   - Imported CAD plan: work on a copy or isolated group.
   - Furniture/trim path: clean only selected curves/edges.
   - Face-not-forming issue: inspect gaps and stray edges first.
   - Curved path for Profile Builder/Skatter: simplify only enough to keep design intent.

2. **Prepare model safely**
   - Save a version before automatic closing/simplification.
   - Explode or enter the relevant group/component context before running tools.
   - Hide or lock unrelated geometry.
   - Work in top/orthographic view for 2D linework when possible.

3. **Choose Edge Tools² command**
   - `Find Edge Gaps`: inspect and manually close open-end vertices.
   - `Close All Edge Gaps`: batch close small gaps under a threshold.
   - `Erase Stray Curves`: remove loose curves not forming faces.
   - `Simplify Curves`: reduce excessive segments from imported or over-detailed curves.
   - `Co-linear from start to end`: straighten selected vertices between endpoints.
   - `Co-linear to Red/Green/Blue Axis`: force selected vertices onto X/Y/Z alignment.
   - `Divide Face`: split faces into multiple pieces.

4. **Use conservative tolerances**
   - Default code setting for close gaps is `10.mm`; for interior CAD cleanup, start smaller when dimensions matter.
   - Increase tolerance only after reviewing what will be merged.
   - Do not batch-close across intentional reveals, shadow gaps, door openings, grout joints, or furniture clearances.

5. **QA after cleanup**
   - Check whether faces form correctly.
   - Check dimensions around doors, walls, cabinets, trim, and panel lines.
   - Run a second gap inspection if downstream operations still fail.
   - Keep a backup of pre-cleanup linework for tracing or dimension reference.

## Output pattern

```text
Edge cleanup goal:
Target geometry/context:
Required dependency status:
Recommended Edge Tools² commands:
Tolerance / simplification settings:
Manual operation steps:
Risks / do-not-merge areas:
QA checks:
Next plugin handoff:
```
