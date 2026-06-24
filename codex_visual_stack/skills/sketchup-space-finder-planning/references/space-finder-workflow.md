# SketchUp Space Finder Workflow Reference

## Plugin audit

Source RBZ:

```text
/Users/bonnie/Downloads/SketchUpSpaceFinder.rbz
```

Installed target:

```text
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/habitat_space_use_plugin.rb
/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/habitat_space_use_plugin/
```

Visible loader facts:

```text
Extension name: SketchUp Space Finder
Version: 0.31.2
Creator: SketchUp
Description: Support the identification of spaces in SketchUp models.
Extension ID: a97d22f8-5968-4f43-bcf9-4f322fa7a8cb
```

Package safety facts:

- Contains `.rb`, encrypted `.rbe`, `.style`, `.svg`, `.pdf`, `.png`, `.susig`, and `extension_info.txt`.
- No `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found.
- Uses helper modules with names suggesting IFC and TrimBIM support, layers/tags, faces, scenes, styles, observers, and space components.

Public references checked:

- Extension Warehouse result identifies SketchUp Space Finder as a SketchUp extension for identifying spaces in 2D/3D models.
- Public summaries describe it as helping visualize/list floor plan spaces, supporting space planning and area reports.
- Forum guidance indicates it uses visible geometry; for complex models, create scenes that hide furniture/detail/context before running.

## Manual verification after install

Restart SketchUp 2025 after installing. Then check:

1. `Window > Extension Manager`: `SketchUp Space Finder` is enabled.
2. Toolbar/menu shows Space Finder / SketchUp Spaces controls.
3. Open a simple closed-room test model and run detection.
4. Verify the plugin creates/overlays spaces or shows a space list/dialog.

If SketchUp MCP is running, a read-only check can evaluate:

```ruby
require 'json'
plugin_dir = Sketchup.find_support_file('Plugins')
JSON.generate({
  sketchup_version: Sketchup.version,
  ruby_version: RUBY_VERSION,
  plugin_file: File.exist?(File.join(plugin_dir, 'habitat_space_use_plugin.rb')),
  plugin_dir: Dir.exist?(File.join(plugin_dir, 'habitat_space_use_plugin')),
  habitat_module: !!defined?(Habitat::SpaceUsePlugin),
  matching_extensions: Sketchup.extensions.map { |e|
    {name: e.name, version: (e.version rescue nil), creator: (e.creator rescue nil), loaded: (e.loaded? rescue nil)}
  }.select { |e| e[:name].to_s.downcase.include?('space finder') || e[:name].to_s.downcase.include?('space') || e[:creator].to_s.downcase.include?('sketchup') }
})
```

## Model preparation checklist

### Show

- Walls and partitions.
- Floor/slab or enclosing boundary geometry.
- Major room-defining doors/openings where appropriate.
- Envelope/boundaries for terraces, balconies, patios if they are part of the schedule.
- One floor at a time for multi-story buildings.

### Hide

- Furniture and loose decor.
- Skatter vegetation/scatter systems.
- High-poly render assets.
- Construction guides not used as boundaries.
- Ceiling/facade/context elements that confuse plan recognition.
- Duplicate imported CAD linework after it has been modeled into walls.

### Clean

- Close unintended wall gaps.
- Avoid overlapping duplicate walls/faces.
- Keep floors/walls grouped/tagged but visible for detection.
- Use `sketchup-edge-tools-cleanup` on CAD-derived boundaries before relying on space detection.

## Scene strategy

Create dedicated scenes such as:

```text
SPACE_Analysis_Level01_Clean
SPACE_Analysis_Level02_Clean
SPACE_OptionA_Level01
SPACE_OptionB_Level01
SPACE_PublicPrivate_Zoning
```

Scene settings:

- Top/orthographic or clean perspective depending on plugin UI needs.
- Relevant tags visible only.
- Style can use `SketchUp Spaces.style` if the plugin applies it.
- Keep camera identical for option comparison.

## Interior planning outputs

### Residential area table

Recommended columns:

```text
Space ID | Chinese Name | English Name | Zone | Area | Key adjacency | Notes | Issue/Risk
```

Zone options:

- Public: entry, living, dining, family room.
- Private: bedrooms, suite, study.
- Service: kitchen, bath, laundry, equipment.
- Storage: closet, cabinet zones, pantry.
- Circulation: corridor, stair, landing.
- Outdoor/semi-outdoor: balcony, terrace, courtyard.

### Client-facing diagrams

- Room color overlay.
- Public/private/service zoning.
- Circulation path overlay.
- Before/after area comparison.
- Option A/B table with net usable area and design advantage.

## Troubleshooting

- **Rooms merge together**: check wall gaps, missing boundary surfaces, large openings, or intentionally open-plan zones. Add temporary analysis boundaries if needed.
- **Rooms not detected**: simplify visible geometry, isolate one floor, close floor/wall gaps, hide clutter.
- **Detection is slow**: hide furniture/render assets/scatter and use a clean analysis scene.
- **Wrong area units**: check SketchUp model units before reporting.
- **Multi-story confusion**: use floor-by-floor scenes or section isolation.
- **Open-plan living/dining/kitchen**: decide whether to count as one space or split with conceptual/temporary boundary lines for reporting.

## Integration with other skills/plugins

- Use `interior-layout-optimizer` after Space Finder for layout critique, public/private zoning, circulation, storage, and option comparison.
- Use `sketchup-curic-align-view` to create clean top/elevation views and consistent before/after cameras.
- Use `sketchup-edge-tools-cleanup` before Space Finder when imported CAD boundaries are broken.
- Use `sa-boo-proposal-deck-director` to turn space overlays and area tables into client proposal pages.
- Use `sa-boo-material-supplier-budget-db` after room list is stable to build room-by-room material/FF&E/budget schedules.
- Use `sa-boo-autocad-construction-standard` for final area/room naming consistency with CAD/施工图 deliverables.
