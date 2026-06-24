# Material Replacer Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/tt_material_replacer-1.3.0.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_material_replacer.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/tt_material_replacer/
```

Visible loader facts:

```text
Extension name: Material Replacer
Version: 1.3.0
Creator: Thomas Thomassen (thomas@thomthom.net)
Description: Tool that let you replace materials by picking from the model.
Dependency: TT_Lib² >= 2.7.0
```

Package safety facts:

- Contains `tt_material_replacer.rb`, `tt_material_replacer/core.rb`, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, command file, or app bundle was found.
- Source is plain Ruby and was readable.
- The only URL is a ThomThom TT_Lib² missing-dependency help page shown when TT_Lib² is not installed.
- SHA256 of source RBZ: `34a1d226c72c74f7a7991faac053db6a81c7b5773ab19298d9f3dfe7f468a3b1`.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Material Replacer` is enabled.
2. `Tools > Material Replacer` exists.
3. TT_Lib² is installed and enabled.
4. Create two colored materials on two faces, run Material Replacer, pick old then new, and confirm replacement.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'tt_material_replacer.rb')
dir = File.join(plugin_dir, 'tt_material_replacer')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  version_line: (File.readlines(loader).grep(/PLUGIN_VERSION/).first.strip rescue nil),
  has_core: File.exist?(File.join(dir, 'core.rb')),
  tt_lib2_file: File.exist?(File.join(plugin_dir, 'TT_Lib2.rb')),
  tt_lib2_dir: Dir.exist?(File.join(plugin_dir, 'TT_Lib2')),
  material_replacer_defined: !!defined?(TT::Plugins::MaterialReplacer),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('material replacer') }
})
```

## Behavior notes

- First pick selects the source material to replace.
- Second pick selects the replacement material.
- The plugin replaces matching materials in:
  - `model.entities`
  - non-image component definitions' entities
  - entity material and face back material when they match the source
- It can replace `Default` material with a picked material, or a picked material with `Default`, depending on the two picks.
- It does not create a new material; create/name the replacement material first.

## Interior design recipes

### White model to finish material

```text
Goal: quickly convert clay/white model elements to selected finish material
Steps:
1. Save model copy or option scene.
2. Create/rename replacement material.
3. Run Material Replacer.
4. Pick clay/default/wrong material, then pick target finish material.
5. Check hero render cameras.
QA: make sure all objects using the old material truly should change.
```

### Scheme A/B material swap

```text
Goal: compare two material palettes with identical geometry/camera
Steps:
1. Duplicate model file or keep a tagged option copy.
2. Rename materials by scheme: `A`, `B`, `C`.
3. Replace material A with material B.
4. Keep Advanced Camera Tools scenes locked for before/after export.
QA: differences should be material only, not camera/geometry drift.
```

### Imported model cleanup

```text
Goal: normalize messy imported furniture/material names before rendering
Steps:
1. Inspect material list and identify duplicate/garbage materials.
2. Create clean project material names.
3. Replace one bad material at a time.
4. Purge unused materials only after visual QA.
QA: avoid replacing materials that share the same apparent color but represent different finishes.
```

### Render prep standardization

```text
Goal: prepare model for AI Render, D5, Enscape, or LightUp
Steps:
1. Replace placeholder materials with final named materials.
2. Standardize wall/ceiling/floor/furniture material families.
3. Export screenshots or run render tests.
4. Update material schedule if needed.
QA: texture scale/UV may still need separate adjustment after replacement.
```

## QA checklist

- Save before global replacement.
- Rename materials clearly before swapping.
- Avoid replacing a source material that is used in multiple unrelated objects.
- Check nested components, back faces, and hidden tags.
- Do not purge until after visual QA.
- If material texture orientation/scale is wrong, use texture/UV tools after replacement.
- Record material swaps when they affect client options or budget/supplier schedules.

## Integration with other skills/plugins

- Pair with `sketchup-ai-render-workflow` for white-model-to-material prompt and visual option generation.
- Pair with `sketchup-lightup-lighting` when material reflectance changes lighting perception.
- Pair with `sketchup-advanced-camera-tools` for locked A/B material comparison views.
- Pair with `sketchup-floor-panel-grid` for replacing generated panel materials.
- Pair with `sa-boo-material-supplier-budget-db` when mapping SketchUp materials to supplier/budget records.
