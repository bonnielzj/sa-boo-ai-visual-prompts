# Floor Panel Grid Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/MyPanelGrid.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/MyPanelGrid.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/MyPanelGrid/
```

Visible loader facts:

```text
Extension name: Floor Generator
Version: 1.0.0
Creator: PV Arjun
Description: Creates a grid of panels on a selected face with user input sizes.
Extension ID: 130ffacc-6909-4bf3-9132-2d4d198aeb45
```

Package safety facts:

- Contains `MyPanelGrid.rb`, `MyPanelGrid/main.rb`, two PNG icons, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, command file, or app bundle was found.
- No network, shell, file deletion, or suspicious Ruby patterns were found in visible source.
- SHA256 of source RBZ: `6cdf34b38e424956928f86266d685ec129f8e0300c9e7324e50d811cc02f2ecd`.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Floor Generator` is enabled.
2. `Plugins > Floor Generator` exists.
3. The `Floor Generator` toolbar is visible or can be shown.
4. Draw a simple rectangle face, select only the face, run the tool.
5. Enter a small test such as width `80`, height `160`, thickness `9`, spacing `3`.
6. Confirm a new group of raised panels appears and can be selected independently.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'MyPanelGrid.rb')
dir = File.join(plugin_dir, 'MyPanelGrid')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  loader_version_line: (File.readlines(loader).grep(/ex\.version/).first.strip rescue nil),
  has_main: File.exist?(File.join(dir, 'main.rb')),
  has_icons: File.exist?(File.join(dir, 'panel_grid_tool_16.png')) && File.exist?(File.join(dir, 'panel_grid_tool_24.png')),
  mypanel_defined: !!defined?(MyPanelGrid),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('floor generator') || e[:name].to_s.downcase.include?('panel') }
})
```

## Important behavior and limitations

- The tool requires exactly one selected `Sketchup::Face`.
- It uses the first edge of the selected face to decide the panel X axis; if the grain/module direction is wrong, rotate/redraw the guide face or select a face whose first edge direction fits the design.
- It uses the outer loop bounding extents in local coordinates; irregular or concave shapes may generate panels based on the bounding area, not a perfect clipped panelization.
- It creates one group in active entities and pushpulls panel faces by the given thickness.
- It applies one material to front, back, and side faces.
- It creates partial panels at the last row/column if remaining space is large enough; check edge slivers.
- It does not automatically cut around doors, drains, columns, furniture, or complex obstacles. Use separate faces/masks or edit afterward.

## Size recipes for interior design

### Wood floor planks

```text
Use: quick wood floor massing or render base
Panel Width: 18–24 cm
Panel Height: 90–180 cm
Thickness: 3–8 mm for visual relief, 12–18 mm for construction-like boards
Spacing: 1–3 mm
Notes: Align long direction with circulation or window light direction; apply wood material and adjust texture scale/rotation afterward.
```

### Large stone or porcelain slabs

```text
Use: luxury floor/wall slab grid
Panel Width: 60–120 cm
Panel Height: 120–240 cm
Thickness: 6–12 mm visually; use project-realistic values if detailing
Spacing: 2–5 mm
Notes: Avoid tiny edge cuts at focal walls; plan centered layout before running if client-facing.
```

### Feature wall panels

```text
Use: headboard wall, TV wall, corridor wall, office background
Panel Width: 30–80 cm
Panel Height: 120–300 cm depending on ceiling and module rhythm
Thickness: 6–18 mm
Spacing: 3–10 mm
Notes: Select the wall face inside the wall group; test orientation; save before running.
```

### Acoustic or ceiling modules

```text
Use: acoustic panels, ceiling rafts, modular ceiling grid
Panel Width: 60 cm or 120 cm
Panel Height: 60 cm or 120 cm
Thickness: 10–30 mm
Spacing: 5–20 mm
Notes: Keep lighting/air-conditioning conflicts visible; use tags to compare density options.
```

### White-model material ideation

```text
Use: raised panel rhythm before assigning final material
Panel Width/Height: choose module from concept grid
Thickness: 5–10 mm
Spacing: 3–6 mm
Material: create neutral material such as Clay_Panel_WarmWhite
Notes: Pair with sketchup-ai-render-workflow prompts for material exploration.
```

## QA checklist

- Save model before generating many panels.
- Confirm selection is one face, not a group/component.
- Confirm units: width/height are centimeters; thickness/spacing are millimeters.
- Check panel direction against material grain.
- Check edge residual panels; adjust width/height/spacing if slivers appear.
- Check collisions with doors, skirting boards, cabinetry, wall base, and furniture.
- Rename and tag generated group immediately.
- For rendering, verify material texture scale and UV orientation after generation.

## Integration with other skills/plugins

- Pair with `sketchup-edge-tools-cleanup` when a CAD-imported face will not select or panelize cleanly.
- Pair with `sketchup-profile-builder` for skirting, trims, frames, and panel border profiles after grid generation.
- Pair with `sketchup-curic-align-view` to review wall panel grids front-on.
- Pair with `sketchup-advanced-camera-tools` and `sketchup-ai-render-workflow` for locked render views and white-model-to-material explorations.
- Pair with `sa-boo-material-supplier-budget-db` when translating panel modules into material schedules, quantities, and budget lines.
