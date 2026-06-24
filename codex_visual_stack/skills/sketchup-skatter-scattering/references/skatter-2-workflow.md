# Skatter 2 Workflow Reference

## Plugin audit

Source RBZ: `/Users/bonnie/Downloads/skatter_2.2.1.rbz`

Install target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/skatter.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/skatter/
```

Visible loader facts from `skatter.rb`:

```text
Module: Lindale::Skatter
Extension name: Skatter, or Skatter 2 if Skatter v1 is also installed
Creator: Lindalë
Description: The most powerful scattering extension for SketchUp
Loader: skatter/menu
Extension ID: 23339f53-a400-40a4-a9c1-2aad7dc0213d
```

Compatibility facts from the local package:

- `core/mac/ruby_3.2.0/Skatter.bundle`: Mach-O universal binary, `x86_64 + arm64`.
- `core/mac/libembree3.3.dylib`: Mach-O universal binary, `x86_64 + arm64`.
- `core/mac/SketchupPathRewrite.bin`: Mach-O universal binary, `x86_64 + arm64`.
- Windows `.so` and `.bin` files are bundled for cross-platform packaging; do not use them on macOS.
- The package contains encrypted `.rbe` code; rely on visible loader info, UI strings, and official docs/forums for behavior.

Official/public references checked:

- Extension Warehouse page: `https://extensions.sketchup.com/extension/23339f53-a400-40a4-a9c1-2aad7dc0213d/skatter`
- Lindalë Skatter page: `https://lindale.io/skatter`
- Skatter 2.2.1 release forum: `https://forums.lindale.io/t/release-skatter-2-2-1/4043`
- Release notes: `https://skatter.help.lindale.io/release-notes`
- Support: `https://lindale.io/support?product=skatter`

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: Skatter is enabled.
2. Menus/toolbars show `Skatter` or `Skatter 2`.
3. Open Skatter once and confirm license/trial status.
4. If 3D Bazaar/library access is needed, sign in or install/activate the bundled `3dbazaar.rbz` if prompted by Skatter.

If SketchUp MCP is running and a read-only verification is needed, evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  plugin_file: File.exist?(File.join(plugin_dir, 'skatter.rb')),
  plugin_dir: Dir.exist?(File.join(plugin_dir, 'skatter')),
  skatter_module: !!defined?(Lindale::Skatter),
  skatter_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('skatter') || e[:creator].to_s.downcase.include?('lindal') }
})
```

## Interior use cases

### Rug / carpet pile

- Host: rug surface group, slightly above floor to avoid z-fighting.
- Objects: short fiber clumps or low-poly hair cards, 2-4 variants.
- Distribution: random surface distribution.
- Density: start low; use render-only for final.
- Scale: 70-130% random, uniform scale on.
- Rotation: full random Z rotation; slight tilt only if geometry supports it.
- Masks: area mask below sofa/table legs to avoid intersection; soft falloff on rug edge.
- QA: fibers should not look like grass unless intentionally shaggy.

### Indoor planter / potted greenery

- Host: soil surface or planter inset.
- Objects: leaf clusters, small stems, pebbles.
- Distribution: surface host with density variations.
- Scale: 80-140% random.
- Rotation: random Z, slight X/Y variation.
- Masks: exclude planter rim and furniture collision zones.
- QA: do not let leaves pass through walls, glass, or ceiling.

### Books / decor / retail props

- Host: shelf plane or table display zone.
- Objects: component set with correct origins.
- Distribution: points host for controlled placement; surface random for casual props.
- Rotation: small controlled range, not fully random unless messy display is intended.
- QA: keep composition legible; luxury shelf styling needs whitespace.

### Acoustic / ceiling / facade modules

- Host: ceiling plane, curve path, or facade surface.
- Objects: slats, baffles, panels, pendant lights.
- Distribution: curve or surface with aligned axes.
- Rotation: keep orthogonal or follow curve axis.
- Masks: exclude sprinkler/light slots and access panels.
- QA: verify buildability, spacing, maintenance access, and collision with MEP.

## Landscape use cases

### Lawn / meadow

- Host: lawn/terrain surface group.
- Objects: 3-8 grass/weed variants, proxies if needed.
- Distribution: random with density/falloff.
- Masks: paths, paving, building footprints, furniture, water edges.
- Filters: slope/altitude where terrain exists.
- Render: render-only for high density; generate lower-density geometry only for clay previews.

### Gravel / mulch / rocks

- Host: bed or path surface.
- Objects: small pebble/stone variants.
- Distribution: random, collision if available/needed.
- Scale: broad but plausible random range.
- Masks: edge falloff to avoid hard CG borders unless edged by metal/stone trim.

### Trees / shrubs

- Host: landscape zones or curves along paths.
- Objects: tree/shrub proxies or render assets.
- Camera: use distance-to-camera falloff/culling for large scenes.
- QA: keep trunks out of paving, facade, underground covers, and sightlines.

## UI feature map from local strings

Observed Skatter controls include:

- Hosts: surface, curve, points.
- Objects: scattered objects, scale multiplier.
- Distribution: random.
- Filters: altitude, slope, collisions.
- Masks: paint, area, image, path, composition; inclusive/exclusive.
- Camera: selected camera, scene camera, distance to camera, falloff distance/curve, offset.
- Transforms: random scale, random translation, random rotation, uniform scale, orthogonal 90/180/270 rotation, look-at target.
- Materials: pick materials from list or viewport.
- Options: seed/random seed/new seed.
- Output/performance: preview, in-model, render-only, composition manager, export scattered objects/materials, Octane CSV export.

## Recommended settings templates

### High-end interior rug pass

```text
Host: SK_HOST_rug_surface_01
Objects: 2-3 short fiber components or fine fur cards
Mode: Render only for final, preview low density
Density: low/medium until camera reads softness; avoid visible repeated clumps
Scale: 0.7-1.25 random, uniform
Rotation: random Z, tiny tilt only
Masks: furniture contact exclusion + edge falloff
Camera: fixed scene camera; no need for far-distance scatter
```

### Courtyard planting pass

```text
Host: SK_HOST_planting_bed_01 + SK_HOST_planter_02
Objects: shrub_A/B, grass_A/B, pebble_A
Distribution: random surface
Density: layered by object type: groundcover high, shrubs low
Scale: groundcover 0.75-1.35; shrubs 0.85-1.25
Rotation: random Z
Masks: path/door/furniture exclusions; paint mask for organic gaps
Render: render-only for vegetation; generate only hero plants if export requires
```

### Linear path lights / bollards

```text
Host: SK_HOST_curve_path_light_01
Objects: bollard component with origin at base center
Distribution: curve host
Spacing/density: exact rhythm if possible, otherwise low density with aligned axis
Transform: align instance axis with curve; keep upright
Masks: exclude doorways/turning points if needed
QA: check code/safety spacing and door clearances manually
```

## Performance rules

- Always save before generating dense in-model scatter.
- Use components, not loose groups, for scatter objects.
- Keep scatter object origins and axes correct before opening Skatter.
- Use preview while tuning; final can use render-only if renderer supports it.
- Use camera culling for fixed views and large scenes.
- Split heavy systems into separate compositions: grass, shrubs, rocks, trees, decor.
- Name compositions by purpose and camera, e.g. `SK_CMP_Lawn_Cam01_RenderOnly`.

## Troubleshooting

- Skatter does not appear: restart SketchUp; verify `skatter.rb` and `skatter/` are in the 2025 Plugins folder; check Extension Manager.
- License dialog appears: start trial, activate, or use offline activation according to Lindalë account/license status.
- Viewport becomes slow: lower preview density, turn off preview, use render-only, split compositions, or reduce object polycount.
- Objects penetrate furniture/walls: add area masks, lower object scale, adjust host surface, or use collision controls if suitable.
- Scatter appears too artificial: increase variant count, random scale/rotation/translation, add falloff, and avoid perfectly even density.
- Renderer misses render-only objects: test with the target renderer; if unsupported, generate in-model geometry at reduced density or use renderer-native scatter/proxy workflow.
