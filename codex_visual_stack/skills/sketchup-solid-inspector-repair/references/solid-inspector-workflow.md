# Solid Inspector Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/su插件/tt_solid_inspector-1.3.0.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_solid_inspector.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_solid_inspector/
```

Visible loader facts:

```text
Plugin name: Solid Inspector
Version: 1.3.0
Description: Inspects and highlight problems with solids.
Creator: Thomas Thomassen (thomas@thomthom.net)
Extension ID: 3b19edfa-3c55-4699-b42d-7a47880262d9
```

Package safety facts:

- Contains `.rb`, `.html`, `.js`, `.css`, `.png`, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found.
- Pure Ruby/web asset package, so no macOS native binary compatibility issue was found.

Dependency found in `tt_solid_inspector/core.rb`:

```ruby
require 'TT_Lib2/core.rb'
TT::Lib.compatible?( '2.7.0', 'Solid Inspector' )
```

Current local status: Solid Inspector 1.3.0 is installed and TT_Lib² 2.15.1 is installed in the SketchUp 2025 Plugins folder. Restart SketchUp 2025 after installing/updating so the dependency is loaded.

TT_Lib² dependency page used by the plugin:

```text
http://www.thomthom.net/software/sketchup/tt_lib2/errors/not-installed
```

Modern upgrade note from the package:

- `Solid Inspector² for SketchUp 2014 or newer is available` is shown in bundled upgrade UI.
- For SketchUp 2025, prefer installing `Solid Inspector²` if available, because it provides clearer reporting and more automatic fixes than this legacy Solid Inspector 1.3.0.

## Manual verification after installing dependencies

Restart SketchUp 2025 after installing/updating TT_Lib² and Solid Inspector. Then check:

1. `Window > Extension Manager`: `Solid Inspector` is enabled.
2. `Tools > Solid Inspector` menu appears.
3. If a TT_Lib² warning appears, install/update TT_Lib² and restart SketchUp.
4. If prompted to install Solid Inspector², consider using the newer version for SketchUp 2025.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  solid_inspector_file: File.exist?(File.join(plugin_dir, 'tt_solid_inspector.rb')),
  solid_inspector_dir: Dir.exist?(File.join(plugin_dir, 'tt_solid_inspector')),
  solid_inspector2_file: File.exist?(File.join(plugin_dir, 'tt_solid_inspector2.rb')),
  tt_lib2_core_candidates: Dir.glob(File.join(plugin_dir, '**/TT_Lib2/core.rb')),
  tt_lib_defined: !!defined?(TT::Lib),
  solid_inspector_defined: !!defined?(TT::Plugins::SolidInspector),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('solid inspector') || e[:name].to_s.downcase.include?('tt_lib') }
})
```

## What Solid Inspector 1.3.0 checks

The visible code identifies error edges as:

```ruby
e.is_a?( Sketchup::Edge ) && e.faces.length != 2
```

Interpretation:

- Edge with 0 faces: loose/stray edge.
- Edge with 1 face: boundary/hole/open shell edge.
- Edge with more than 2 faces: non-manifold/internal overlapping geometry.

The tool groups connected error edges and allows cycling/zooming through error groups.

## Repair recipes

### Boolean operation fails

1. Confirm both operands are groups/components, not loose geometry.
2. Inspect each operand separately.
3. Fix open shell edges and internal faces.
4. Check Entity Info for `Solid Group` / `Solid Component`.
5. Retry boolean on duplicated geometry.

### Cabinet/furniture body not solid

1. Duplicate the object.
2. Inspect outer shell.
3. Fill missing bottom/back/side faces if the object is intended to be closed.
4. Delete internal construction faces and loose guide edges.
5. Reverse faces outward.
6. Validate before using booleans, export, or material/render handoff.

### Imported CAD/SketchUp object has many tiny holes

1. Use `sketchup-edge-tools-cleanup` first for tiny gaps and stray curves.
2. Redraw critical boundaries manually if auto-close would distort dimensions.
3. Rerun Solid Inspector.
4. Keep a copy of original imported linework for dimension reference.

### Artisan/organic mesh cleanup

1. Avoid over-editing on the only copy; duplicate and simplify.
2. Look for non-manifold poles, holes, and internal folds.
3. Repair large holes manually; use mesh cleanup tools where available.
4. Validate only after final subdivision/smoothing state is set.

### 3D print/STL export prep

1. Ensure one connected watertight shell per printable part.
2. Remove internal faces and tiny loose geometry.
3. Validate SketchUp Entity Info solid status.
4. Export STL and re-check in slicer/repair tool if needed.

## Manual repair cues

- Orange/red highlighted loop around an opening: fill the hole or decide it is intentional.
- Highlighted isolated line: erase stray edge/curve.
- Highlighted line inside a surface/body: check for internal face or duplicate overlap.
- Many errors along one seam: redraw the seam cleanly; do not patch edge by edge if topology is bad.
- Error after Push/Pull: undo and redo with grouped geometry or use clean face boundaries.

## Integration with other skills/plugins

- Use `sketchup-edge-tools-cleanup` before solid repair when CAD-imported edges/gaps are the root issue.
- Use `sketchup-profile-builder` after validation when clean solids/paths are needed for trim, frames, panels, or rails.
- Use `sketchup-artisan-organic-modeling` before final inspection for organic/subdivision meshes.
- Use `sketchup-skatter-scattering` after host surfaces are clean; not every Skatter host needs to be solid, but it must be clean and predictable.
- Use `autocad-drafting` or CAD cleanup workflows for upstream DWG geometry problems before SketchUp import.
