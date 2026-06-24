# ColorMaker Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/DBUR_ColorMaker_v1.0.1.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DBUR_ColorMaker.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DBUR_ColorMaker/
```

Visible loader facts:

```text
Extension name: ColorMaker
Loader version: 1.0.0
Source file name: DBUR_ColorMaker_v1.0.1.rbz
Creator: D. Bur
Description: Create materials using colors based on industry and standards
Extension ID: 98d470a8-8505-4a39-83eb-2192d1e58ad7
```

Package safety facts:

- Contains `DBUR_ColorMaker.rb`, encrypted `ColorMaker.rbe`, `DBUR_ColorMaker.hash`, `.susig`, palette `.txt` files, icons, CSS, and a 3-page PDF help file.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, command file, or app bundle was found.
- Main implementation is encrypted `.rbe`, so do not assume internals beyond visible loader metadata and observed behavior.
- SHA256 of source RBZ: `3e4958cd9b8e2fb2d837d36a67bb170310c63911168d6c7cebac1d694a27eac4`.

## Palette resources installed

Palette files found in `DBUR_ColorMaker/Resources/`:

```text
AS-2700 Colors.txt
AUTOCAD Colors.txt
BOOTSTRAP Colors.txt
Color temperatures Colors.txt
HTML-SU Colors.txt
MUNSELL Colors.txt
NBS Colors.txt
NCS Colors.txt
PMS Colors.txt
Pantone 100 Colors.txt
Pantone 200 Colors.txt
Pantone 300 Colors.txt
Pantone 400 Colors.txt
Pantone 500 Colors.txt
Pantone 600 Colors.txt
Pantone 700 Colors.txt
Pantone 800 Colors.txt
RAL Colors.txt
RESENE Colors.txt
UK-BS381 Colors.txt
USA-FS595C Colors.txt
WEB Colors.txt
X11 Colors.txt
```

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `ColorMaker` is enabled.
2. ColorMaker menu/toolbar appears.
3. Open the ColorMaker dialog and load a small palette such as RAL or Web colors.
4. Create one material, apply it to a test face, and confirm it appears in SketchUp Materials.
5. If ColorMaker does not open in SketchUp 2025, treat it as compatibility-limited and use the palette `.txt` files manually for color values.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'DBUR_ColorMaker.rb')
dir = File.join(plugin_dir, 'DBUR_ColorMaker')
resources = File.join(dir, 'Resources')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  version_line: (File.readlines(loader).grep(/version/).first.strip rescue nil),
  has_main: File.exist?(File.join(dir, 'ColorMaker.rbe')),
  palette_count: Dir.glob(File.join(resources, '*Colors.txt')).length,
  has_help_pdf: File.exist?(File.join(resources, 'ColorMakerHelp.pdf')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('colormaker') }
})
```

## Interior design recipes

### RAL/NCS wall paint study

```text
Goal: compare architectural paint directions
Steps:
1. Select 3-8 RAL/NCS candidates, not the full palette.
2. Create named SketchUp materials with ColorMaker.
3. Apply to duplicate wall scenes or use Material Replacer for A/B swaps.
4. View under daylight and night scenes.
QA: real paint must be confirmed with physical samples; viewport RGB is only an approximation.
```

### Brand color in interior proposal

```text
Goal: translate brand colors into spatial accents
Steps:
1. Identify Pantone/PMS/Web/HEX source.
2. Create brand material references with ColorMaker or manual HEX.
3. Apply to signage, feature wall, furniture accent, or proposal swatches.
4. Pair with brand/visual identity notes.
QA: check saturation under render lighting; reduce intensity if color overpowers space.
```

### Soft furnishing palette

```text
Goal: test fabric/curtain/cushion color families
Steps:
1. Use Pantone/PMS/Web or NCS approximate colors.
2. Create a small family of 5-12 colors.
3. Apply to simplified furniture blocks or material boards.
4. Export locked camera comparisons.
QA: flat colors do not replace texture/fabric material; add texture later for final rendering.
```

### White-model zoning colors

```text
Goal: communicate program or option zones
Steps:
1. Use muted Web/X11/Bootstrap colors for clear but not noisy zoning.
2. Create materials like `ZONE_Public`, `ZONE_Private`, `ZONE_Service`.
3. Apply to plan/axon views and export diagrams.
QA: avoid confusing zoning colors with final material selections.
```

### Lighting color-temperature reference

```text
Goal: create visual reference swatches for warm/cool light discussion
Steps:
1. Use `Color temperatures Colors.txt` to create 2700K/3000K/3500K/4000K reference materials.
2. Apply only to diagram swatches or explanatory cards, not actual light emitters unless renderer supports it.
3. Pair with LightUp/D5/Enscape light settings.
QA: material color is not the same as physical light color temperature.
```

## QA checklist

- Keep created palette small and project-specific.
- Include standard/code in material names.
- Use Material Replacer for controlled global swaps after materials exist.
- Confirm colors under project lighting/camera scenes.
- Do not claim exact Pantone/RAL/NCS reproduction from SketchUp RGB alone.
- Use physical samples or supplier swatches for final client/施工 confirmation.
- If the ColorMaker UI fails in SU2025, use the installed `.txt` palettes as a local color-code reference and create materials manually.

## Integration with other skills/plugins

- Pair with `sketchup-material-replacer` for batch replacing placeholders with standard colors.
- Pair with `sketchup-ai-render-workflow` when translating color palettes into AI render prompts.
- Pair with `sketchup-lightup-lighting` to test how color changes under daylight/night lighting.
- Pair with `sa-boo-brand-director` and `sa-boo-figma-brand-kit` for brand-color consistency.
- Pair with `sa-boo-material-supplier-budget-db` when mapping color selections to paint/supplier records.
