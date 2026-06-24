---
name: sketchup-skatter-scattering
description: SketchUp Skatter 2 workflow for SketchUp 2025 interior, landscape, and visualization scattering. Use when Codex needs to plan, prepare, audit, or guide Skatter compositions for grass, plants, trees, gravel, carpet fibers, fabric fuzz, books, decor, people/crowds, facade modules, ceiling features, parametric assemblies, render-only scatter, masks, hosts, density/falloff, random scale/rotation/translation, camera culling, and performance-safe rendering workflows in SketchUp/D5/Enscape/V-Ray/Twinmotion-style projects.
---

# SketchUp Skatter Scattering

Use this skill to design controlled Skatter compositions for SketchUp 2025. Codex usually cannot operate Skatter's UI directly; prepare the SketchUp model, name hosts/objects, propose Skatter settings, write a manual operation checklist, and use SketchUp MCP only for model cleanup, grouping, tagging, camera setup, and verification.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS / Apple Silicon.
- Skatter source package: `/Users/bonnie/Downloads/skatter_2.2.1.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/skatter.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/skatter/`
- Native compatibility checked:
  - `skatter/core/mac/ruby_3.2.0/Skatter.bundle` is a universal `x86_64 + arm64` Mach-O bundle.
  - `skatter/core/mac/libembree3.3.dylib` and `SketchupPathRewrite.bin` are also universal.
- Skatter may require license/trial activation. UI strings include 15-day trial, activate/deactivate, and offline activation.

Read `references/skatter-2-workflow.md` when creating detailed scattering settings, installation checks, or troubleshooting.

## Core workflow

1. **Define the scattering task**
   - Interior: rug fibers, cushion seams/fuzz, books, table decor, indoor planting, ceiling baffles, wall modules.
   - Landscape: lawn/grass, shrubs, trees, gravel, mulch, rocks, leaves, path-side planting.
   - Commercial/city: crowds, facade panels, lights, street furniture, repeated props.
   - Render optimization: render-only high-density objects while keeping SketchUp light.

2. **Prepare hosts and scattered objects**
   - Make each host a clean group/component: floor patch, planter soil, rug surface, terrain, curve/path, or point set.
   - Make each scatter object a component with correct origin, scale, axes, and material.
   - Use low-poly proxies for viewport and high-quality render assets only when the target renderer supports it.
   - Name objects clearly: `SK_HOST_rug_01`, `SK_OBJ_grass_A`, `SK_MASK_path_01`.

3. **Choose host type**
   - Surface host: grass, gravel, rug fibers, leaves, objects on floors/terrain.
   - Curve host: linear planting, path lights, ceiling strips, facade rhythm, handrail/trim objects.
   - Points host: exact decorative placements with controlled randomization.

4. **Control distribution**
   - Start with low density and preview. Increase only after composition is readable.
   - Add random scale, rotation, and translation to avoid CG repetition.
   - Use falloff for edges, paths, rug borders, planting transitions, and density gradients.
   - Use slope/altitude filters for terrain and vertical surfaces.

5. **Use masks**
   - Area masks for no-scatter regions: circulation, door swing, stepping stones, furniture footprints.
   - Path masks for borders/tracks/linear exclusions.
   - Paint masks for art-directed density and organic transitions.
   - Image masks only when texture coordinates are meaningful and stable.

6. **Performance and rendering**
   - Prefer preview + render-only for very dense vegetation/fibers.
   - Use camera culling/falloff for scenes with fixed client cameras.
   - Generate real geometry only when needed for export, clash checking, or renderer compatibility.
   - Save before generating large in-model scatter.

## Output pattern

```text
Skatter 任务：
场景/镜头：
Host：
Scatter Object：
Distribution：
Density / Count：
Scale / Rotation / Translation：
Masks / Filters：
Render-only / In-model：
性能风险：
手动操作步骤：
QA 检查：
```

## SA&BOO quality rules

- Use Skatter to support design intention, not to hide weak space planning.
- Keep interior scatter restrained: luxury usually means controlled irregularity, not visual noise.
- Never let scatter block circulation, doors, key furniture, or client-readable spatial relationships.
- For proposal renders, lock camera and compare before/after with the same composition settings.
