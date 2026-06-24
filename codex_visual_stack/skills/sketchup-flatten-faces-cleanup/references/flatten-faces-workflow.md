# Unwrap and Flatten Faces 2.6 Workflow Reference

## Plugin audit

Source package:

```text
/Users/bonnie/Downloads/as_flatten_2-6.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/as_flatten.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/as_flatten/
```

Visible loader facts:

```text
Extension name: Unwrap and Flatten Faces
Version: 2.6
Creator: Alexander C. Schreyer, www.alexschreyer.net
Description: automatically unwrap or smash selected faces and lay them flat; useful for laser cutouts, CNC prep, texturing, etc.
Extension ID from package: 479b4faf-433a-40ab-8727-1c34dee1c829
```

Package safety notes:

- Pure Ruby package; no native `.bundle`, `.dylib`, `.dll`, or `.exe` files found.
- Uses SketchUp defaults for settings and opens help URL/dialogs.
- Designed for selected ungrouped faces.

## What it does

The plugin can:

- Unwrap selected faces and place a flattened grouped copy on a target plane.
- Automatically unwrap non-coplanar selected faces, with iterative attempts.
- Smash/project selected faces to an axis plane.
- Preserve original geometry and create flattened results as grouped copies.
- Optionally colorize flattened segments to help identify panel relationships.

## Where to use it in interior work

### White-model panel extraction

Use when a sculptural wall, ceiling baffle, curved cabinet face, or custom decorative surface needs 2D panel logic for discussion or documentation.

Steps:

1. Duplicate the source geometry.
2. Enter the duplicate group/component.
3. Select only the target faces.
4. Run `Unwrap and Flatten Faces`.
5. Use colorizing if each panel needs to be matched back to the 3D source.
6. Dimension and label the flattened panel group before fabrication discussion.

### CAD/import cleanup projection

Use when imported or modeled line/face geometry is slightly off plane and a clean 2D copy is needed for tracing or layout.

Steps:

1. Work on a copy, not the only source.
2. Choose projection/smash rather than unwrap if the goal is a flat 2D reference.
3. Use `Z_AXIS` for plan-like output or `X_AXIS`/`Y_AXIS` for elevation-like output.
4. Hand off to `sketchup-edge-tools-cleanup` for gap/edge repair if the flat result still has broken edges.

### Texture/material layout

Use when a set of faces needs a flat reference for material mapping, mural layout, stone slab discussion, or custom graphic alignment.

Steps:

1. Flatten a copy of the faces.
2. Export or screenshot the flat group for annotation.
3. Use `sketchup-texture-positioning` after applying actual materials back on the 3D source.

## Selection rules

- Select faces inside the active editing context.
- Avoid selecting whole nested components unless you have entered/exploded a working copy.
- Avoid huge mixed selections; split by room, wall, ceiling bay, or material zone.
- For organic meshes, unwrap in smaller seam-based islands.

## Settings guidance

- Confirmation dialogs: keep on during first test; hide later for batch-like work.
- Prompts: useful while learning, can be hidden when workflow is stable.
- Iterations: increase only if unwrap needs more attempts; large selections can be slow.
- Target axis:
  - `Z_AXIS`: typical floor-plan/XY flattening.
  - `X_AXIS`: projection to YZ-like elevation plane.
  - `Y_AXIS`: projection to XZ-like elevation plane.
- Colorize: enable when panel identity matters; disable for clean monochrome output.

## Failure modes and fixes

- **No result / warning:** selection may not contain ungrouped faces. Enter group context or select faces directly.
- **Overlapping panels:** split selection into smaller logical islands or add manual seam strategy.
- **Unexpected orientation:** change target axis or rotate final grouped result.
- **Distorted/unhelpful unwrap:** use smash/projection if exact connected unwrapping is not required.
- **Slow run:** reduce face count or simplify mesh before running.

## MCP verification snippet

If SketchUp MCP is running, verify installation with:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  file_exists: File.exist?(File.join(plugin_dir, 'as_flatten.rb')),
  dir_exists: Dir.exist?(File.join(plugin_dir, 'as_flatten')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('flatten') || e[:name].to_s.downcase.include?('unwrap') }
})
```

## QA checklist

- Original 3D geometry remains unchanged.
- Flattened output is grouped and separated from source.
- Face count and major edges correspond to source geometry.
- No unintended overlaps before fabrication or texture layout.
- Critical dimensions checked after flattening.
- Output is labeled with source room/object/material zone when used in a project file.
