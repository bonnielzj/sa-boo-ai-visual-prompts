# SketchUp 2025 Stability Plugin Policy

Last updated: 2026-06-25

## Purpose

This note records the stable operating policy for Bonnie's SketchUp 2025 environment after repeated crashes around cleanup / purge workflows.

## High-level diagnosis

The crash pattern observed on 2026-06-25 pointed to SketchUp cleanup / purge operations triggering Ruby observer callbacks. The practical stability response is to keep SketchUp's plugin environment light, avoid unnecessary always-on render/scatter/legacy plugins, and use reversible plugin disable folders.

## Actions already taken locally

- LightUp was removed from the active SketchUp 2025 plugin directory after Bonnie explicitly allowed deletion.
- These plugins were moved out of the active plugin directory into a disabled folder:
  - `ladb_opencutlist`
  - `skatter`
  - `CAUL_Flowify`
  - `DM_SketchUV`

## Default policy

### Keep active unless a new crash points to them

- `1001bit_freeware`
- `DM_ProfileBuilder4`
- `curic_align_view`
- `su_advancedcameratools`
- `ene_texturepositioning`
- `tt_material_replacer`
- `tt_selection_toys`
- `tt_edgetools`
- `tt_solid_inspector2`
- `tt_cleanup` with caution
- SketchUp built-in utility plugins
- `Enscape`, unless render-related crashes continue

### Keep disabled or on-demand

- `ladb_opencutlist`
- `skatter`
- `CAUL_Flowify`
- `DM_SketchUV`
- `su_diffusion`, if AI Render is not actively used
- `DM_artisan2`, unless organic/subdivision modeling is needed
- `SketchUcation`, unless plugin management is needed
- `sketchup-stl`, unless STL import/export is needed

## Reversible disable method

When disabling plugins, quit SketchUp first, then move both the loader and matching folder out of the active plugin directory. Example pairs:

- `plugin_name.rb`
- `plugin_name/`

Use a disabled directory rather than deleting, unless Bonnie explicitly asks to delete the plugin.

## Work habit

Before running broad cleanup / purge operations:

1. Save a versioned copy of the model.
2. Restart SketchUp after plugin changes.
3. Avoid running heavy cleanup tools on the full model without isolating geometry.
4. Test save, scene switching, and `Purge Unused` after each plugin batch change.
