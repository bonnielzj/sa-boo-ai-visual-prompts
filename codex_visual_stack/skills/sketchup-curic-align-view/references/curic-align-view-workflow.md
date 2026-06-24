# Curic Align View Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/su插件/curic_align_view_v1.2.1.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/curic_align_view.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/curic_align_view/
```

Visible loader facts:

```text
Plugin name: Curic Align View
Version: 1.2.1
Description: Align View
Creator: Vo Quoc Hai (curic4su@gmail.com)
Extension ID: 00ac5617-71f0-42d9-85bd-334f64cc7ee9
```

Package safety facts:

- Contains `.rb`, encrypted `.rbe`, `.png`, `.susig`, `.DS_Store`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found in the package.
- No native binary compatibility issue was found for macOS.
- Code is encrypted `.rbe`, so avoid assuming internal implementation beyond visible loader metadata and observed behavior.

Public references checked:

- Extension Warehouse search result identifies Curic Align View as a tool for aligning SketchUp view from current camera position to standard view, including features like face alignment, FOV, lock, and spin-style view controls.
- Curic plugin ecosystem is by Vo Quoc Hai / Curic.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Curic Align View` is enabled.
2. Toolbar/menu shows `Curic Align View` icons.
3. Test on a simple box: select a face or activate the tool and align view to the face.
4. Create a Scene from the aligned camera and verify returning to the Scene preserves view direction.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(File.join(plugin_dir, 'curic_align_view.rb')),
  plugin_dir: Dir.exist?(File.join(plugin_dir, 'curic_align_view')),
  curic_view_defined: !!defined?(CURIC::View),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('curic') || e[:name].to_s.downcase.include?('align view') }
})
```

## View recipes

### Interior wall elevation for proposal

```text
Goal: clean front elevation of TV wall / headboard / feature wall
Projection: Parallel Projection
Steps:
1. Isolate or select the target wall face.
2. Use Curic Align View to align view to that face.
3. Spin/rotate view until horizontal floor/ceiling lines are level.
4. Set visible tags: wall, built-ins, furniture silhouettes, key dimensions if needed.
5. Save Scene: CAM_[Room]_[Wall]_Elev_01.
6. Export screenshot or use in LayOut/Figma/PDF.
QA: no perspective skew; openings and panel modules appear true-to-plane.
```

### Cabinet or millwork front view

```text
Goal: cabinet/front face review for proportions and panel rhythm
Projection: Parallel Projection
Steps:
1. Select cabinet front face or a helper rectangle plane.
2. Align view to the face.
3. Hide side clutter; keep adjacent wall/floor reference if helpful.
4. Save scene and export as a design-review plate.
QA: handles, reveals, drawer lines, and vertical gaps are not distorted.
```

### AI Render white-model source view

```text
Goal: base image for AI Render material/mood generation
Projection: Perspective or Parallel, depending on image role
Steps:
1. Align to the major spatial axis or feature plane.
2. For client-friendly view, use two-point perspective or correct verticals.
3. Keep white/off-white clay materials; preserve geometry clarity.
4. Save scene: CAM_AIRender_[Space]_[Intent]_01.
5. Pair with sketchup-ai-render-workflow prompts.
QA: no accidental tilted camera; source view must explain spatial relationship.
```

### Before/after matching

```text
Goal: same camera for option A/B or existing/proposed comparison
Projection: same for both views
Steps:
1. Align once to target face/space axis.
2. Save Scene A as camera master.
3. Duplicate Scene for option B, changing only model state/tags/materials.
4. Do not alter FOV, aspect, projection, or camera after duplication.
QA: overlay-style comparison should line up exactly.
```

### Section/elevation hybrid

```text
Goal: show interior elevation while cutting away foreground
Projection: usually Parallel Projection
Steps:
1. Add a section plane before/after alignment depending on target.
2. Align to wall or section plane direction.
3. Save section visibility and style with the Scene.
4. Export with clear poche/cut line style if needed.
QA: section does not remove design-critical details; depth remains readable.
```

## Camera standards for SA&BOO interior output

- Keep verticals vertical for most client/proposal images.
- Use perspective for spatial atmosphere; use parallel projection for true elevation/detail review.
- Keep consistent FOV across a render pack.
- Avoid ultra-wide distortion unless deliberately used for small-space explanation.
- Save a named Scene before running AI Render, D5/Enscape export, or screenshot export.
- Record scene name and view intent in the proposal/render prompt notes.

## Integration with other skills/plugins

- Pair with `sketchup-ai-render-workflow` for clean source views and prompt-controlled image generation.
- Pair with `sa-boo-realtime-render-presentation` for D5/Enscape/Twinmotion shot lists.
- Pair with `sketchup-profile-builder` when front/elevation views are needed for trim, moulding, panels, frames, and slats.
- Pair with `sketchup-edge-tools-cleanup` when faces/planes fail to align because imported geometry is broken.
- Pair with `sketchup-skatter-scattering` for fixed-camera comparison of scatter density and masking.
