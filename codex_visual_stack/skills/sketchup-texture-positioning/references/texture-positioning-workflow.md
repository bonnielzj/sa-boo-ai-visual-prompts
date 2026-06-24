# Texture Positioning Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/ene_texturepositioning_v1.0.3.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/ene_texturepositioning.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/ene_texturepositioning/
```

Visible loader facts:

```text
Extension name: Eneroth Texture Positioning Tools
Version: 1.0.3
Creator: Julia Christina (eneroth3) Eneroth
Description: Fast texture positioning on multiple faces. Align to faces' side, align to selected edge, rotate 90° clockwise/counter-clockwise, rotate custom angle, and depatternize.
Extension ID: 9d566697-9b02-4f3c-b769-9e1c57af7750
```

Package safety facts:

- Contains `ene_texturepositioning.rb`, `ene_texturepositioning/main.rb`, PNG icons, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, command file, or app bundle was found.
- Source is plain Ruby and was readable.
- SHA256 of source RBZ: `05ea25b003c737274b230735477b97d91a31359d0d98a6e32d52664fc512f087`.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Eneroth Texture Positioning Tools` is enabled.
2. `Plugins > Texture Positioning` menu exists.
3. Toolbar `Texture Positioning` appears or can be restored.
4. Apply a textured material to a few faces; select faces and test Rotate Clockwise.
5. Test Align Texture To Edge with exactly one selected edge and several selected faces.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'ene_texturepositioning.rb')
dir = File.join(plugin_dir, 'ene_texturepositioning')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  version_line: (File.readlines(loader).grep(/ex.version/).first.strip rescue nil),
  has_main: File.exist?(File.join(dir, 'main.rb')),
  icon_count: Dir.glob(File.join(dir, '*.png')).length,
  module_defined: !!defined?(Ene_texturePositioning),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('texture positioning') }
})
```

## Command behavior

### Align Texture

```text
Use when each selected face should align texture to its own first bounding edge.
Selection: textured faces only.
Good for: quick cleanup on separated panels or floor/tile faces.
Caution: orientation depends on each face's first edge; if inconsistent, use Align Texture To Edge.
```

### Align Texture To Edge

```text
Use when many faces need one shared texture direction.
Selection: exactly one reference edge plus target textured faces.
Good for: wood floors, wall panels, stone slabs, linear wallpaper, fabric weave.
Caution: selected reference edge vector must lie in the plane of target faces; faces not coplanar/compatible may be skipped.
```

### Rotate Clockwise / Counter Clockwise

```text
Use when texture direction is 90° off.
Selection: textured faces.
Good for: wood grain, floorboards, tile, wall panels, fabric/leather direction.
```

### Rotate Custom angle

```text
Use when texture needs a specific non-90° angle.
Selection: textured faces.
Input: counter-clockwise angle in degrees.
Good for: herringbone-like approximations, diagonal stone, custom graphic/wallpaper direction.
```

### Depatternize

```text
Use when many adjacent faces show repeated texture tiling.
Selection: textured faces.
Effect: random offset/rotation-like texture movement per face to break pattern repetition.
Good for: stone, brick, gravel, plaster, fabric, leather, vegetation-like surfaces.
Caution: not ideal for precise tile grids, bookmatched stone, or continuous wood grain where alignment matters.
```

## Interior design recipes

### Wood floor grain direction

```text
Goal: align wood floor texture with circulation/window axis
Steps:
1. Select floor faces with wood material.
2. Select one edge along desired plank/grain direction.
3. Run Align Texture To Edge.
4. Check main camera and plan view.
QA: grain direction supports room length; transitions at thresholds are intentional.
```

### Stone slab wall

```text
Goal: align stone veining on a feature wall
Steps:
1. Select slab/wall faces.
2. Use Align Texture To Edge or Rotate 90°.
3. Avoid Depatternize if slabs are meant to be continuous/bookmatched.
QA: veining direction reads premium and not random; seams match panel design.
```

### Wallpaper / fabric / leather

```text
Goal: make pattern/weave direction consistent
Steps:
1. Select vertical wall or furniture upholstery faces.
2. Use Align Texture To Edge with a vertical/horizontal reference.
3. Use Rotate Custom angle only for intentional diagonal patterns.
QA: repeat scale and pattern direction look intentional in camera view.
```

### Brick/tile cleanup

```text
Goal: correct tile or brick orientation before rendering
Steps:
1. Select tile/brick faces.
2. Rotate 90° if wrong.
3. Use Align Texture to normalize face-local orientation.
4. Do not Depatternize regular tile grids unless you intentionally want irregularity.
QA: grout/brick courses align with architecture.
```

### Depatternize plaster/stone/gravel/fabric

```text
Goal: reduce obvious repeated texture patterning
Steps:
1. Select many faces using the same repeated texture.
2. Run Depatternize.
3. Check from render camera.
4. Undo if randomness breaks continuity.
QA: pattern becomes natural, not noisy.
```

## QA checklist

- Save before applying to many faces.
- Select faces, not groups/components, unless editing inside the group/component.
- Verify materials have image textures; commands skip untextured materials.
- Use one clean reference edge for global alignment.
- Check texture scale separately; this plugin adjusts position/orientation, not material size.
- Use Material Replacer before texture positioning if you still need to swap material types.
- Do not depatternize precision materials that need exact alignment.

## Integration with other skills/plugins

- Pair with `sketchup-material-replacer` after material swaps to fix texture orientation.
- Pair with `sketchup-color-maker-palettes` for flat color materials; texture positioning is mostly for image textures.
- Pair with `sketchup-floor-panel-grid` for panel/tile/wood grid texture direction.
- Pair with `sketchup-advanced-camera-tools` for locked before/after texture QA views.
- Pair with `sketchup-ai-render-workflow`, D5, Enscape, or LightUp render prep when texture direction affects realism.
