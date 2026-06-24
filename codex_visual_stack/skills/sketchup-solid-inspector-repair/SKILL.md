---
name: sketchup-solid-inspector-repair
description: SketchUp Solid Inspector and Solid Inspector² workflow for SketchUp 2025 solid/manifold geometry diagnosis and repair. Use when Codex needs to plan, prepare, audit, or guide fixing non-solid groups/components, boolean failures, 3D-print/export STL problems, Profile Builder/Artisan/Skatter host issues, reversed/internal faces, holes, stray edges, edges without exactly two faces, nested geometry problems, shell cleanup, or model QA before rendering/export. The installed Solid Inspector 1.3.0 requires TT_Lib² version 2.7.0 or newer; for SketchUp 2014+ prefer Solid Inspector² when available.
---

# SketchUp Solid Inspector Repair

Use this skill to diagnose and repair SketchUp groups/components that are expected to be valid solids. For SketchUp, a reliable solid should be a watertight manifold shell: no holes, no stray/internal edges, no internal faces, no self-intersections, and each shell edge should normally belong to exactly two faces.

Codex usually cannot click Solid Inspector directly; prepare the model, isolate suspect geometry, propose inspection/fix steps, use SketchUp MCP for read-only or scripted geometry checks where safe, and provide manual repair guidance.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Solid Inspector source package: `/Users/bonnie/Downloads/su插件/tt_solid_inspector-1.3.0.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_solid_inspector.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_solid_inspector/`
- Installed version from loader: `1.3.0`.
- Creator: Thomas Thomassen / ThomThom.
- Dependency: `TT_Lib²` version 2.7.0 or newer is required for this installed version to load. TT_Lib² version 2.15.1 is installed in the SketchUp 2025 Plugins folder; restart SketchUp after installation so Solid Inspector can load against it.
- Upgrade note: The package itself promotes `Solid Inspector²` for SketchUp 2014 or newer; prefer Solid Inspector² for modern SketchUp 2025 workflows when available.

Read `references/solid-inspector-workflow.md` for dependency checks, issue types, and repair recipes.

## Core workflow

1. **Clarify what must be solid**
   - Boolean/subtract/union part.
   - 3D print/STL export object.
   - Closed custom furniture/cabinet/body.
   - Terrain/host object that must act as a closed shell.
   - Organic mesh from Artisan/subdivision that needs export cleanup.

2. **Isolate the object**
   - Work on a copy of the group/component.
   - Enter the correct edit context or select one group/component only.
   - Hide unrelated tags/objects.
   - Explode nested wrappers only if necessary and only on a duplicate.

3. **Inspect**
   - Prefer Solid Inspector² if installed.
   - Otherwise use Solid Inspector after TT_Lib² is installed.
   - Cycle through highlighted errors; zoom to each issue.
   - Interpret every highlighted edge as a symptom, not always the root cause.

4. **Repair common problems**
   - Fill holes with faces.
   - Delete stray edges/curves that do not bound faces.
   - Remove internal faces and duplicate overlapping surfaces.
   - Fix reversed faces so front faces point outward.
   - Merge or redraw tiny broken edges/gaps.
   - Resolve nested geometry by making the solid a single clean group/component definition.

5. **Validate**
   - SketchUp Entity Info should report `Solid Group` or `Solid Component` when appropriate.
   - Rerun inspector until no errors remain.
   - Test target operation: boolean, export, push/pull, render proxy, or plugin handoff.

## Output pattern

```text
Solid repair goal:
Target object/context:
Dependency/plugin status:
Likely issue type:
Inspection steps:
Repair steps:
Do-not-change areas:
Validation checks:
Next handoff:
```

## Quality rules

- Never repair directly on the only copy of a client model; duplicate first.
- Do not close intentional openings in walls/cabinets/furniture just to make a shell solid unless the deliverable requires it.
- Keep construction meaning: a render-only decorative object may not need to be a solid; a boolean/STL object usually does.
- For complex organic meshes, use cleanup/subdivision tools first, then solid inspection as final QA.
