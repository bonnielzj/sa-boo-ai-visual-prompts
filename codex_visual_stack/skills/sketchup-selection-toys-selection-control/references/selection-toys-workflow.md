# Selection Toys 2.4.0 Workflow Reference

## Plugin audit

Source package:

```text
/Users/bonnie/Downloads/tt_selection_toys-2.4.0.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_selection_toys.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_selection_toys/
```

Visible loader facts:

```text
Extension name: Selection Toys
Version: 2.4.0
Description: Suite of tools to create, manipulate and filter selections.
Creator: Thomas Thomassen (thomas@thomthom.net)
Plugin ID: TT_Selection_Toys
```

Package safety notes:

- No `.exe`, `.dll`, `.dylib`, `.bundle`, or `.so` native binaries found.
- Package contains Ruby, HTML/JS webdialog UI, icons, config files, and signature/hash files.
- It is independent from TT_Lib according to changelog since 2.2.2, but ThomThom ecosystem plugins usually coexist with TT_Lib².

## Common command groups

### Select Only filters

Use to reduce current selection to one type:

- Edges
- Faces
- Groups
- Components
- Guides / Guide Points
- Text
- Images
- Section Planes
- Curves / Arcs / Circles / Polygons / n-Gons / 3D Polylines
- Linear / Radial Dimensions
- Front Default Material / Back Default Material
- Hidden
- Soft Edges / Smooth Edges
- Border Edges / Selection Border

### Deselect filters

Use to remove protected or irrelevant entity types from the current selection:

- Deselect Edges / Faces / Groups / Components
- Deselect Guides / Text / Images / Sections
- Deselect Hidden / Soft / Smooth / Border Edges
- Deselect default-material entities when cleaning materials.

### Similar instance selection

Use when repeated components/groups need selection:

- Select active/all similar component instances.
- Select by same layer/tag.
- Select active/all similar groups.
- Convert group copies into components only on a copy or when model organization is understood.

### Face relationship selection

Useful for modeling and cleanup:

- Connected coplanar faces.
- Connected parallel/perpendicular faces.
- Connected by material or layer/tag.
- Same direction, coplanar, parallel, perpendicular, same area, opposite faces.
- Quad-face loops / face loops when topology matters.

## CAD import cleanup recipes

### Remove CAD text/dimensions after import

1. Enter the imported CAD group if editable.
2. Select all inside the group.
3. Use `Select Only > Text`, dimensions, guide points, or images as needed.
4. Delete only after confirming these are not needed as scale/reference evidence.
5. Keep a locked unedited original CAD reference elsewhere.

### Isolate edges for Edge Tools

1. Select imported CAD group contents or a copied problem area.
2. Use `Select Only > Edges`.
3. Run `sketchup-edge-tools-cleanup` commands such as gap finding, stray curve erase, or curve simplification.
4. Do not run broad cleanup on door gaps, reveals, tile joints, or intentional openings without checking.

### Find hidden/soft/smooth problem edges

1. Select target group/component contents.
2. Use `Select Only > Hidden`, `Soft Edges`, or `Smooth Edges`.
3. Inspect whether hidden smoothing is intentional, especially on imported furniture or curved surfaces.
4. Deselect protected groups/components before erase or harden operations.

### Prepare material cleanup

1. Select all model or target group.
2. Use same material / connected material commands to inspect material islands.
3. Use default material filters to find unassigned faces or wrong backside material.
4. Hand off to `sketchup-material-replacer` for replacement rather than manual random painting.

### Prepare Profile Builder paths

1. Select candidate edges/curves.
2. Use curve/arc/circle/polygon filters to isolate the path type.
3. Remove non-path edges from selection.
4. Run Edge Tools if gaps or tiny segments exist.
5. Hand off to `sketchup-profile-builder`.

## Risk notes

- Selection filters can select much more than expected if run at model root. Prefer working inside a copied group/context.
- Do not delete selected entities before visually checking the selection set.
- Be careful with hidden entities: some may be intentional construction or component details.
- `Convert Group Copies into Components` changes model organization; use only after saving a version or duplicating the model.
- Large selections can be slow; work by room, group, layer/tag, or import segment.

## MCP verification snippet

If SketchUp MCP is running, verify installation with:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  file_exists: File.exist?(File.join(plugin_dir, 'tt_selection_toys.rb')),
  dir_exists: Dir.exist?(File.join(plugin_dir, 'tt_selection_toys')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('selection toys') }
})
```

## QA checklist

- Correct editing context is active.
- Selected set contains only intended entity types.
- Locked CAD reference or source geometry is protected.
- Deletion/material replacement/cleanup action is reversible.
- Downstream tool receives a clean, intentional selection.
