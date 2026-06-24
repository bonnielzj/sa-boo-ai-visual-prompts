# LightUp Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/LightUp_Demo.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/lightup.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/lightup/
```

Visible loader facts:

```text
Extension name: Lightup Tools
Loader version: 7.x
Internal version: 7.5.f
Creator: Adam Billyard
Description: Adds tools for soft lighting and realtime flythroughs
Copyright: 2007-2026 Adam Billyard
```

Package facts:

- Contains Ruby source, HTML/JS UI files, LightUp components, IES files, materials, images, and native render modules.
- Ruby 3.2 macOS bundle present: `lightup/Staging/3.2/LMapExt32_x64.bundle`, a Mach-O universal binary including arm64.
- Windows `.so` files are present for cross-platform distribution; do not use them on macOS.
- Source package SHA256: `b654f009b673b530ee246bb1cf49dc1a808a9d6b3102e2798a920d6213a5363d`.
- Demo/evaluation license text is present; verify license status before commercial output.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Lightup Tools` is enabled.
2. LightUp toolbar/menu appears.
3. Open a simple room model, place a LightUp point light or use included light components.
4. Run a small illumination preview; confirm no loader error appears.
5. If SketchUp reports LightUp needs upgrade for this SketchUp version, stop and request a newer official build.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'lightup.rb')
dir = File.join(plugin_dir, 'lightup')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  loader_version_line: (File.readlines(loader).grep(/toolsExtension.version/).first.strip rescue nil),
  internal_version_line: (File.readlines(File.join(dir,'lightmapui.rb')).grep(/VERSION =/).first.strip rescue nil),
  has_lightmaps: File.exist?(File.join(dir, 'lightmaps.rb')),
  has_lightmapui: File.exist?(File.join(dir, 'lightmapui.rb')),
  has_ruby32_mac_bundle: File.exist?(File.join(dir, 'Staging', '3.2', 'LMapExt32_x64.bundle')) || File.exist?(File.join(dir, 'Extensions', '3.2', 'LMapExt32_x64.bundle')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('lightup') }
})
```

## Interior lighting recipes

### Daylight reach check

```text
Goal: understand natural light distribution before material/render work
Scene: daytime, major openings visible
Steps:
1. Hide decorative clutter; keep walls, ceilings, floor, major furniture, windows.
2. Assign reasonable neutral materials; avoid pure white everywhere.
3. Run a daylight/sky-factor style LightUp preview.
4. Mark dark corners, glare zones, and places that need artificial fill.
QA: output should inform design decisions, not replace final render.
```

### Night mood lighting

```text
Goal: test layered residential lighting
Light layers:
- Ambient: ceiling/downlights/cove
- Task: kitchen counter, desk, vanity, reading
- Accent: wall washer, art light, shelf LED, decorative lamp
Steps:
1. Create separate scenes for ambient-only, task+ambient, and final mood.
2. Place or approximate fixtures with LightUp lights.
3. Test color temperature family: 2700K warm residential, 3000K premium neutral-warm, 3500K only when needed.
4. Adjust intensity to avoid flat overlit rooms.
QA: hero surfaces read clearly; dark contrast remains intentional.
```

### IES wall wash / grazing check

```text
Goal: test scallop rhythm and wall texture emphasis
Steps:
1. Use IES files or LightUp fixtures aimed at target wall.
2. Test fixture spacing, setback, beam spread, and height.
3. Use an aligned elevation scene to compare scallop pattern.
4. Translate successful spacing to final renderer or construction notes.
QA: no accidental hot spots on artwork/TV; grazing does not reveal unwanted wall defects unless intended.
```

### Task lighting check

```text
Goal: verify practical lighting zones
Zones:
- Kitchen countertop
- Dining table
- Bathroom vanity
- Desk/workbench
- Wardrobe/closet
Steps:
1. Place light meter grid or sample points around task surfaces.
2. Test light with relevant furniture and cabinetry present.
3. Adjust fixture count/location before final render setup.
QA: task surface is not blocked by upper cabinets, pendants, or human shadow.
```

### Realtime client preview

```text
Goal: quick walkthrough or internal design review
Steps:
1. Prepare lightweight model state.
2. Lock major cameras with Advanced Camera Tools.
3. Run LightUp preview and export screenshots/flythrough only if demo/license permits.
4. Use outputs as internal lighting proof or client explanation draft.
QA: do not deliver demo-watermarked/limited outputs as final commercial render unless acceptable.
```

## QA checklist

- Restart SketchUp after plugin install.
- Keep a duplicate model before illumination experiments.
- Use realistic material reflectance; avoid all-white clay when judging final light levels.
- Separate daylight, night, and fixture-test scenes.
- Check both camera view and plan/elevation light distribution.
- Record problems as design actions: add fill light, change wall color, widen opening, reduce glare, move fixture, adjust beam.
- If LightUp fails to load native bundle, request newer official build rather than forcing install.

## Integration with other skills/plugins

- Pair with `sketchup-advanced-camera-tools` for locked render cameras.
- Pair with `sketchup-curic-align-view` for wall washer/elevation checks.
- Pair with `sketchup-ai-render-workflow` to translate LightUp findings into prompt variables: warm cove lighting, soft wall wash, overcast daylight, etc.
- Pair with `sa-boo-realtime-render-presentation` when building a D5/Enscape/Twinmotion shot pack.
- Pair with `sa-boo-material-supplier-budget-db` when converting lighting tests into fixture schedules and budgets.
