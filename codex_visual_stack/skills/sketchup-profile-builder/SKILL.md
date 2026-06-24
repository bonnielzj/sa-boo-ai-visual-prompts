---
name: sketchup-profile-builder
description: SketchUp Profile Builder 4 workflow for interior design modeling in SketchUp 2025 via SketchUp MCP or manual SketchUp guidance. Use when Codex needs to create, plan, audit, or guide reusable profile/assembly geometry such as skirting boards, trim, mouldings, wall panels, door/window frames, cabinet frames, grille/slat systems, rails, curved profile members, path extrusions, cut openings, or Profile Builder libraries in an interior project.
---

# SketchUp Profile Builder

Use this skill when a SketchUp 2025 interior task should be accelerated with Profile Builder 4 instead of hand-modeling repeated geometry.

## Core Route

1. Confirm SketchUp 2025 is the active modeling target and the `sketchup` MCP server is connected when automation is needed.
2. Read `references/profile-builder-4.md` when installation paths, version notes, or task-specific patterns are needed.
3. Use Profile Builder for repeated path-based or assembly-based geometry: trim, baseboards, crown moulding, wall frames, slats, rails, cabinet skeletons, openings, and parametric repeated members.
4. Use native SketchUp MCP Ruby automation for setup geometry, tags, paths, guide curves, component naming, scene creation, and quality checks.
5. Leave final interactive Profile Builder tool clicks to SketchUp when license dialogs, extension UI, or proprietary Profile Builder commands are not scriptable.

## Modeling Strategy

- Build clean paths first: edges, curves, arcs, or grouped guide lines named by function.
- Separate tags before building: `PB_PATHS`, `PB_PROFILES`, `PB_ASSEMBLIES`, `PB_OUTPUT`, `PB_OPENINGS`.
- Use profiles for linear details: skirting, trim, ceiling lines, door casing, cabinet rails.
- Use assemblies for repeated constructed elements: grille walls, wainscot panels, fence-like partitions, shelving bays, curtain tracks, cabinet frames.
- Use cut openings for door/window/frame logic only after wall masses are stable.
- Keep early white-model members simple; add material, bevel, and fine profile detail after proportions are approved.

## MCP Use

Use SketchUp MCP `eval_ruby` to:

- Create or clean path curves before invoking Profile Builder.
- Name groups/components so Profile Builder output stays readable.
- Add tags/layers and assign placeholder materials.
- Create scenes for checking linear details and repeated assemblies.
- Export or save test versions before risky plugin operations.

Do not assume Profile Builder's private Ruby API is stable. Prefer UI/manual Profile Builder actions unless the current installed plugin exposes a documented method.

## QA Checklist

- Confirm the model is saved before using Profile Builder operations.
- Check paths are welded/continuous where the result must be continuous.
- Avoid duplicate hidden edges before building profiles; use CleanUp/Edge Tools when available.
- Check face orientation before cut openings or profile extrusion.
- Keep Profile Builder output grouped or componentized.
- After output, verify scale, tag, material, instance count, and scene visibility.

## SA&BOO Interior Defaults

- Start profile details as clay/white massing in concept phase.
- Use restrained detail density: one strong rhythm is better than many decorative lines.
- For client previews, create locked camera scenes showing: full space, profile close-up, corner condition, and before/after massing.
- Mark early Profile Builder results as concept/detail intent until construction drawings and material samples are confirmed.
