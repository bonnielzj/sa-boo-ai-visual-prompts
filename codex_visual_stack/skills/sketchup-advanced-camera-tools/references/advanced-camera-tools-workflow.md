# Advanced Camera Tools Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/su_advancedcameratools-1.3.4.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_advancedcameratools.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/su_advancedcameratools/
```

Visible loader facts:

```text
Plugin name: Advanced Camera Tools
Version: 1.3.4
Creator: SketchUp
Copyright: 2018-2020, Trimble Inc.
Description: places real-world cameras, with film/video/digital/still camera presets, aspect ratio, focal length, safe zones, and camera properties.
```

Package safety facts:

- Contains `.rb`, encrypted `.rbe`, camera preset `.skp`, `.csv`, `.png`, `.svg`, `.pdf`, `.strings`, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, or command file was found.
- No macOS native binary compatibility issue was found; main implementation is encrypted `.rbe`, so do not assume internals beyond visible loader metadata and observed behavior.
- SHA256 of source RBZ: `29eb9b8cb9a10316d58979fe224065b7c42dde9d0d2702c360ca45096a37c883`.

Camera preset data:

- `cameradata/cameras.csv` contains film/video/digital/still camera formats.
- Examples include 16mm, 35mm, 65mm, VistaVision, full-frame DSLR, APS-C, Four Thirds, large format, medium format, and video/digital camera formats.
- The plugin exposes controls such as Create Camera, Edit Camera, Look Through Camera, Lock/Unlock Camera, Reset Camera, Show/Hide Cameras, Show/Hide Frustum Lines/Volume, safe zones, center mark, stats, aspect ratio, focal length, roll, tilt, truck/dolly, and pedestal.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `Advanced Camera Tools` is enabled.
2. `Tools > Advanced Camera Tools` exists; toolbar can be shown from SketchUp toolbar/view controls.
3. `Create Camera` creates a visible physical camera object.
4. `Look Through Camera` enters the camera view.
5. `Lock Camera` prevents accidental movement.
6. Frustum/safe-zone toggles work and can be hidden before final export.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
loader = File.join(plugin_dir, 'su_advancedcameratools.rb')
dir = File.join(plugin_dir, 'su_advancedcameratools')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(loader),
  plugin_dir: Dir.exist?(dir),
  loader_version_line: (File.readlines(loader).grep(/fs_extension.version/).first.strip rescue nil),
  has_actloader: File.exist?(File.join(dir, 'actloader.rbe')),
  has_main: File.exist?(File.join(dir, 'advancedcameratools_main.rbe')),
  has_cameras_csv: File.exist?(File.join(dir, 'cameradata', 'cameras.csv')),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('camera') }
})
```

## Interior camera recipes

### White-model AI Render source view

```text
Goal: stable base view for material/mood AI generation
Format: usually 16:9 for presentation or 4:5 for social/proposal close-up
Lens: 28–35 mm equivalent for room view; 35–50 mm for more premium less-distorted feel
Steps:
1. Build clean white/clay massing with major furniture blocks.
2. Create ACT camera from main entry/diagonal corner/hero axis.
3. Look through camera; keep verticals controlled and avoid ceiling/floor over-stretch.
4. Save scene CAM_AIRender_WhiteModel_[Room]_[Lens]_01.
5. Feed same scene to sketchup-ai-render-workflow prompt.
QA: geometry relationships must be readable even before material prompt.
```

### Living/dining hero render

```text
Goal: client-facing mood render showing spatial hierarchy
Format: 16:9 or A3 landscape
Lens: 28–35 mm equivalent; avoid ultra-wide if furniture distorts
Camera height: 1.35–1.55 m unless a lower editorial view is intentional
Steps:
1. Place camera near a natural human standing/sitting route.
2. Frame foreground edge, main seating/dining zone, and background feature wall.
3. Lock camera after approval.
4. Duplicate scene for material/lighting options.
QA: sofa/table edges not warped; verticals feel intentional; main design feature has breathing room.
```

### Detail/material camera

```text
Goal: show stone, wood, fabric, metal, joinery, lighting detail
Format: 4:5, 1:1, or close crop for proposal page
Lens: 50–85 mm equivalent
Camera height: match object centerline; use shallow angle only if it helps material reading
Steps:
1. Create tighter ACT camera facing the material transition or detail object.
2. Reduce wide-angle distortion by using longer focal length and backing up camera.
3. Lock camera; save scene CAM_ACT_[Room]_[Detail]_55mm_01.
QA: material grain direction, reveals, and seam relationships are clear.
```

### Option A/B comparison

```text
Goal: compare two design schemes with identical composition
Format: same for all options
Lens/camera: locked master camera
Steps:
1. Create and approve the master ACT camera.
2. Save CAM_ACT_[Room]_Master_01.
3. Duplicate scenes for A/B, changing only tags/materials/components.
4. Do not orbit, pan, or alter focal length after duplication.
QA: exported images overlay cleanly; differences are design changes, not camera drift.
```

### Camera documentation plate

```text
Goal: show camera position/frustum for internal render planning
Format: plan/axon screenshot, not final client render
Steps:
1. Show all ACT cameras and frustum lines/volume.
2. Capture a top/axon view with scene names annotated.
3. Hide frustums again before final render scenes.
QA: documentation view does not contaminate final scenes.
```

## Composition standards for SA&BOO interior output

- Use camera to express spatial hierarchy first; prompts/materials support the composition.
- Prefer a premium restrained lens language: 30–50 mm equivalent where possible, 24–28 mm only for tight spaces.
- Avoid extreme wide-angle ceilings, stretched sofas, and warped verticals unless intentionally explaining a tiny room.
- Keep a consistent camera-height family across one project so the proposal feels coherent.
- Save every render source as a named scene before AI generation or renderer export.
- Keep locked approved cameras; duplicate scenes for schemes instead of re-aiming the camera.
- Record camera notes in the render prompt: scene name, lens, aspect, light direction, key materials, and mood.

## Integration with other skills/plugins

- Pair with `sketchup-ai-render-workflow` for white-model-to-material prompts and AI Render iterations.
- Pair with `sketchup-curic-align-view` for wall elevations, face-aligned front views, and pre-aligned axes before physical camera setup.
- Pair with `sa-boo-realtime-render-presentation` for D5/Enscape/Twinmotion shot lists and final export packs.
- Pair with `sketchup-profile-builder`, `sketchup-artisan-organic-modeling`, and `sketchup-skatter-scattering` when camera composition depends on trim, organic furniture, or decorative scatter density.
- Pair with `sa-boo-proposal-deck-director` when selecting which ACT scenes belong in a client-facing PDF/PPT/Figma proposal.
