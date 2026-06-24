# Edge Tools² 2.2.0 Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/su插件/tt_edgetools-2.2.0.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_edgetools.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_edgetools/
```

Visible loader facts:

```text
Plugin name: Edge Tools²
Version: 2.2.0
Description: Suite of tools for manipulating edges.
Creator: Thomas Thomassen (thomas@thomthom.net)
Extension ID: 52ab7474-469f-4a62-baa0-63c2b6390373
```

Dependency found in `tt_edgetools/core.rb`:

```ruby
require 'TT_Lib2/core.rb'
TT::Lib.compatible?( '2.7.0', 'Edge Tools²' )
```

Therefore install **TT_Lib² version 2.7.0 or newer** before expecting Edge Tools² to appear in SketchUp. The TT_Lib² not-installed page points to:

```text
https://extensions.sketchup.com/extension/c03a2b93-3365-4ef1-95f4-f35158757622/tt-lib
```

Current local status: Edge Tools² 2.2.0 is installed and TT_Lib² 2.15.1 is installed in the SketchUp 2025 Plugins folder. Restart SketchUp 2025 after installing/updating so the dependency is loaded.

## Commands found in the package

Menu/tool commands:

- `Divide Face` — split faces into multiple pieces.
- `Find Edge Gaps` — inspect and close edge gaps interactively.
- `Close All Edge Gaps` — batch close all edge gaps under a tolerance and optionally remove small edges.
- `Erase Stray Curves` — erase loose/stray curves.
- `Simplify Curves` — simplify selected curves using a tolerance/epsilon.
- `Co-linear from start to end` — make selected vertices colinear between the first and last point.
- `Co-linear to Red (X) Axis` — force selected vertices colinear in X axis.
- `Co-linear to Green (Y) Axis` — force selected vertices colinear in Y axis.
- `Co-linear to Blue (Z) Axis` — force selected vertices colinear in Z axis.

## Manual verification after installing TT_Lib²

Restart SketchUp 2025 after installing or updating TT_Lib² and Edge Tools². Then check:

1. `Window > Extension Manager`: Edge Tools² is enabled.
2. `Tools > Edge Tools²`: command submenu appears.
3. Toolbar `Edge Tools²` can be shown.
4. If a TT_Lib² warning appears, install/update TT_Lib² and restart SketchUp again.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  edge_tools_file: File.exist?(File.join(plugin_dir, 'tt_edgetools.rb')),
  edge_tools_dir: Dir.exist?(File.join(plugin_dir, 'tt_edgetools')),
  tt_lib_core_candidates: Dir.glob(File.join(plugin_dir, '**/TT_Lib2/core.rb')),
  tt_lib_defined: !!defined?(TT::Lib),
  edge_tools_defined: !!defined?(TT::Plugins::EdgeTools),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('edge tools') || e[:name].to_s.downcase.include?('tt_lib') }
})
```

## Interior/CAD cleanup recipes

### Imported DWG floor plan will not form faces

1. Work inside a copied group of the imported plan.
2. Hide dimensions, hatches, furniture blocks, and text layers.
3. Run `Find Edge Gaps` near problem areas.
4. Use `Close All Edge Gaps` only with a small tolerance first.
5. Run `Erase Stray Curves` after confirming no reference curves are needed.
6. Try forming faces again; if faces still fail, inspect for non-coplanar edges or duplicate overlaps.

Risk: CAD imports often contain intentional small openings, reveals, door gaps, and double lines. Do not blindly merge everything at large tolerance.

### Path cleanup before Profile Builder

1. Select the intended extrusion path only.
2. Use `Simplify Curves` to reduce excessive segments while preserving corners/radii.
3. Use `Co-linear from start to end` or axis co-linear commands to straighten almost-straight segments.
4. Verify no tiny edges remain at turns.
5. Hand off to `sketchup-profile-builder` for trim, skirting, moulding, frames, or rails.

### Host cleanup before Skatter

1. Ensure the host boundary is closed and planar.
2. Use `Close All Edge Gaps` on small boundary gaps.
3. Use `Erase Stray Curves` for loose internal curves not needed as masks.
4. Keep intentional mask/path curves separate and named.
5. Hand off to `sketchup-skatter-scattering`.

### Organic/Artisan preparation

1. Use Edge Tools only for hard edge/path cleanup before organic tools.
2. Avoid over-simplifying curves that define sculptural silhouettes.
3. For subdivision meshes, prefer quad-oriented cleanup tools over Edge Tools when topology matters.

## Tolerance guidance

- Fine interior details: start below `2 mm` if close-gap input allows it.
- General imported floor plan linework: `2–5 mm` first pass.
- Rough survey/landscape paths: `5–10 mm` only if design intent permits.
- Avoid tolerance larger than the smallest intentional design gap.

The plugin code default for `Close All Edge Gaps` is `10.mm`; treat that as a convenience default, not always safe for interior construction geometry.

## QA checklist

- Faces form only where expected.
- Doors/windows/openings remain open.
- Wall thicknesses and cabinet dimensions are unchanged.
- Reveal lines, panel grooves, grout, shadow gaps, and expansion joints are not accidentally closed.
- Curves remain visually smooth enough after simplification.
- Downstream plugin path now works: Profile Builder extrusion, Push/Pull, Skatter host, or render export.
