# SketchyFFD Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/SketchyFFD_v7.1.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_SketchyFFD.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_SketchyFFD/
```

Visible loader facts:

```text
Extension name: SketchyFFD (Classic)
Loader version: V7
Source file name: SketchyFFD_v7.1.rbz
Creator: mind.sight.studios
Description: Adds a control cage to an object that allows the mesh to be manipulated via control points.
Copyright: 2021, MindSight Studios Inc.
Extension ID: 95cddcf7-58df-43ca-957c-3991103acaae
```

Package safety facts:

- Contains `DM_SketchyFFD.rb`, encrypted `main.rbe`, encrypted `incompatible.rbe`, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, command file, or app bundle was found.
- Main implementation is encrypted `.rbe`, so do not assume internal implementation beyond visible loader metadata and observed behavior.
- SHA256 of source RBZ: `023038dc9ad6eb20dca3dadbb17a90305a7945be1f12383277aeffbbe10f722f`.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `SketchyFFD (Classic)` is enabled.
2. Menu/toolbar entries appear for SketchyFFD.
3. Test on a subdivided box or simple grouped mesh copy.
4. Add a control cage, move a few control points, and confirm the target object deforms.
5. Undo and save a clean backup before using it in a real project.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'DM_SketchyFFD.rb')
dir = File.join(plugin_dir, 'DM_SketchyFFD')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  plugin_name_line: (File.readlines(loader).grep(/PLUGIN_NAME/).first.strip rescue nil),
  version_line: (File.readlines(loader).grep(/VERSION =/).first.strip rescue nil),
  has_main: File.exist?(File.join(dir, 'main.rbe')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('sketchyffd') || e[:description].to_s.downcase.include?('control cage') }
})
```

## Decision rules: SketchyFFD vs other tools

### Use SketchyFFD when

- The design needs a broad deformation of an existing mesh.
- You want to bend/bulge/taper/warp a white-model mass quickly.
- You need a control-cage approach rather than sculpting by brush.
- The object already has enough segments to deform smoothly.
- The output is a concept shape or visual form, not precise construction detailing.

### Use Artisan instead when

- You need subdivision modeling, smoothing, sculpting, or organic refinement.
- You are making cushions, sofas, pillows, terrain-like forms, or soft furniture.
- You need brush-like push/pull or mesh smoothing after deformation.

### Use FredoScale instead when

- You need more predictable bend, twist, taper, stretch, radial bend, or box scaling.
- You need dimensionally controlled transforms or repeated operations.

### Use Profile Builder instead when

- The shape is a linear trim/profile/slat/frame/moulding along a path.
- It needs repeatable construction logic and profile editing.

## Interior design recipes

### Curved feature wall concept

```text
Goal: test a softly curved/bulging wall or display surface
Preparation:
1. Copy the wall mass into a separate group.
2. Add enough vertical/horizontal subdivisions.
3. Use SketchyFFD with a medium cage.
4. Move center control points subtly; keep floor/ceiling boundary points stable if needed.
QA: wall does not self-intersect; curve reads in plan and render camera; buildability is marked concept/proposal.
```

### Soft sofa/backrest massing

```text
Goal: create a soft curved sofa/backrest from blockout geometry
Preparation:
1. Start with a subdivided rectangular mass.
2. FFD the back/arm silhouette.
3. Use Artisan afterward for smoothing/softening if needed.
QA: seat height/depth remain functional; edge loops do not collapse.
```

### Warped ceiling or acoustic feature

```text
Goal: test gentle ceiling wave or acoustic panel movement
Preparation:
1. Create a subdivided ceiling panel field.
2. Use a low/medium cage to lift/drop selected control regions.
3. Keep mechanical/light fixture zones visible.
QA: head clearance, fixture clearance, and sprinkler/HVAC conflicts are considered.
```

### Sculptural partition or art installation

```text
Goal: explore expressive partition geometry
Preparation:
1. Create a clean subdivided panel or volume.
2. Use FFD to twist/bend broad silhouette.
3. Export camera views for concept comparison.
QA: model is not too heavy; form remains readable from main approach path.
```

### White-model option study

```text
Goal: quickly compare organic volume options before detailed modeling
Preparation:
1. Duplicate block model for option A/B/C.
2. Apply different control-cage deformations.
3. Lock the same camera with Advanced Camera Tools.
4. Export clay screenshots or AI Render source images.
QA: compare shape language, not accidental camera change.
```

## QA checklist

- Save before adding the control cage.
- Keep an undeformed copy.
- Add subdivisions before deforming if smooth curvature is needed.
- Avoid using FFD directly on final construction geometry unless you know the consequences.
- Check model in plan/elevation/section and render camera.
- Inspect for collapsed faces, reversed faces, holes, self-intersections, and overly dense meshes.
- Use Solid Inspector if the result must be solid/manifold.
- Use Edge Tools cleanup if imported geometry behaves badly.

## Integration with other skills/plugins

- Pair with `sketchup-artisan-organic-modeling` for smoothing and organic refinement after FFD.
- Pair with `sketchup-solid-inspector-repair` when deformed geometry must remain solid.
- Pair with `sketchup-edge-tools-cleanup` before FFD on imported or messy geometry.
- Pair with `sketchup-advanced-camera-tools` for before/after option cameras.
- Pair with `sketchup-ai-render-workflow` to turn deformed clay masses into concept render prompts.
- Pair with `sketchup-profile-builder` after deformation only if trim/frame/slat details need separate clean construction geometry.
