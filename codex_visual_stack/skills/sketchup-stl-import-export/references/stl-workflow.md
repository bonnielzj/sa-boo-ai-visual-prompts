# SketchUp STL Import & Export 2.2.0 Workflow Reference

## Plugin audit

Source package:

```text
/Users/bonnie/Downloads/sketchup-stl-2.2.0.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/sketchup-stl.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/sketchup-stl/
```

Visible loader facts:

```text
Extension name: STL Import & Export
Version: 2.2.0
Creator: J. Foltz, N. Bromham, K. Shroeder, SketchUp Team
Description: Adds STL file format import and export; open-source project sponsored by the SketchUp team.
Extension ID from package: 412723d4-1f7a-4a5f-b866-281a3e223337
```

Package safety notes:

- Pure Ruby/HTML/JS package; no native `.bundle`, `.dylib`, `.dll`, or `.exe` files found.
- Includes SKUI/webdialog UI code and importer/exporter Ruby files.
- Good for STL exchange; not a replacement for render asset formats like SKP, FBX, OBJ, or glTF when materials/UVs matter.

## Interior design use cases

### Product/decor prototype export

Use for furniture handles, knobs, small decor, lighting brackets, custom feet, sample details, installation jigs, or 3D-printable study models.

Recommended process:

1. Isolate the object as one group/component.
2. Set model units to match vendor/slicer expectation, usually millimeters.
3. Use Solid Inspector before export.
4. Export only the selected object if available in the dialog/workflow.
5. Re-import or open in slicer to verify scale and orientation.

### STL import for reference

Use when receiving mesh-only manufacturer/vendor/prototype files.

Recommended process:

1. Import into a blank temporary SketchUp file first.
2. Choose the unit expected from the source.
3. Measure a known dimension immediately.
4. Simplify or group before copying into the project model.
5. Apply placeholder material only after scale and geometry are acceptable.

### Not ideal for final render assets

Avoid STL when the goal is high-quality render-ready furniture/material assets because STL generally loses:

- material assignments beyond basic face color/workflow-specific metadata,
- texture coordinates/UV detail,
- component hierarchy,
- editable parametric structure,
- efficient SketchUp-native organization.

For render assets, prefer SKP, properly sourced models, Poliigon/Architextures material workflows, or clean OBJ/FBX/glTF pipelines if needed.

## Unit guidance

- Interior prototypes and 3D printing: millimeters.
- Larger study masses/site context: meters only if the downstream tool expects meters.
- US vendor files: confirm inch vs millimeter before import.
- Always check one known length after import/export; STL files can be unitless in practice.

## Solid/manifold QA before export

Use `sketchup-solid-inspector-repair` for printable objects. Check:

- group/component reports as solid,
- no reversed faces,
- no internal faces,
- no holes or non-manifold edges,
- no tiny stray edges/faces,
- wall thickness is printable/processable,
- object scale is correct.

## Export QA

After exporting:

1. Open STL in slicer or import into a temporary SketchUp file.
2. Measure width/depth/height.
3. Check up-axis/orientation.
4. Check visible holes or flipped normals.
5. Save a project note: source SKP path, exported STL path, units, export date, and target vendor/slicer.

## MCP verification snippet

If SketchUp MCP is running, verify installation with:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  file_exists: File.exist?(File.join(plugin_dir, 'sketchup-stl.rb')),
  dir_exists: Dir.exist?(File.join(plugin_dir, 'sketchup-stl')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('stl') }
})
```

## Handoff map

- Use `sketchup-solid-inspector-repair` before STL export if the object must be printable.
- Use `sketchup-edge-tools-cleanup` for problematic imported line/edge geometry; STL meshes are triangulated, so edge cleanup may be limited.
- Use `sketchup-artisan-organic-modeling` or `sketchup-sketchyffd-deformation` before export only while geometry remains editable in SketchUp.
- Keep editable SKP as the master; use STL as delivery/exchange output.
