---
name: sketchup-artisan-organic-modeling
description: SketchUp Artisan 2 workflow for organic and subdivision modeling in SketchUp 2025. Use when Codex needs to plan, prepare, audit, or guide soft/curved/interpolated geometry such as sofas, cushions, curved furniture, sculptural walls, organic partitions, irregular decor objects, terrain-like forms, smoothed meshes, subdivision surfaces, sculpting, soft transformation, or Artisan-ready quad/mesh workflows in an interior design project.
---

# SketchUp Artisan Organic Modeling

Use Artisan for forms that should feel sculpted, soft, subdivided, or organically curved instead of built from simple boxes and trims.

## Core Route

1. Confirm SketchUp 2025 is the target and Artisan 2 is installed.
2. Read `references/artisan-2.md` for local install notes and task patterns when needed.
3. Use SketchUp MCP to prepare base geometry, tags, components, scenes, and white-model placeholders.
4. Use Artisan interactively for subdivision, smoothing, sculpting, soft selection, brush edits, reduce, crease, and organic refinements.
5. Return to SketchUp MCP for cleanup, naming, scale checks, save/export, and review scenes.

## Best Uses

- Soft furniture massing: sofas, cushions, ottomans, poufs, pillows.
- Curved feature elements: sculptural walls, curved counters, reception desks, display plinths.
- Organic decor: vases, art objects, irregular stone/coffee-table masses.
- Smooth transitions and subdivided surfaces where native SketchUp geometry looks too faceted.
- Concept exploration before deciding whether a detail should be remodeled in Rhino/Blender.

## MCP Preparation

Use SketchUp MCP `eval_ruby` to:

- Create low-poly base meshes or bounding volumes.
- Tag objects as `ARTISAN_BASE`, `ARTISAN_WORK`, `ARTISAN_OUTPUT`.
- Save a copy before sculpting or subdividing.
- Create scenes for checking silhouette, close-up surface quality, and overall fit.

Keep base meshes light. Artisan works best when the starting form has enough topology to shape, but not so much that SketchUp becomes slow.

## Modeling Guidance

- Start with large silhouette first; do not sculpt small wrinkles before proportions are approved.
- Prefer quad-like, evenly distributed geometry before subdivision.
- Use crease/edge control for furniture seams, cushion edges, panel breaks, and intentional hard transitions.
- Use reduce/cleanup after sculpting if the object becomes too heavy for the interior model.
- For final renders, keep high-detail organic objects as separate groups/components so they can be hidden or proxied.

## QA Checklist

- Verify scale against real furniture dimensions before sculpting.
- Check face orientation and stray edges before subdivision.
- Save a pre-Artisan copy and a post-Artisan copy.
- Inspect object weight: excessive faces slow SketchUp, Enscape, V-Ray, and Twinmotion exports.
- Keep a low-detail proxy for white-model and client-layout review.

## SA&BOO Defaults

- Use Artisan as a refinement layer after the spatial massing is already approved.
- For concept white models, create simple clay masses first, then use Artisan only on hero objects.
- In client-facing notes, call Artisan outputs "form exploration" unless dimensions and fabrication details are resolved.
