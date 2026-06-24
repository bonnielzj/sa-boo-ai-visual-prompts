# Profile Builder 4 Reference

## Local Install

- SketchUp version verified: SketchUp 2025 `25.0.659`.
- Plugin version installed: Profile Builder `4.0.5`.
- Loader: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_ProfileBuilder4.rb`
- Plugin folder: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_ProfileBuilder4`
- Mac/SU2025 loader component: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_ProfileBuilder4/rgloader/rgloader25.darwin.bundle`
- Source RBZ: `/Users/bonnie/Downloads/ProfileBuilder-v4.0.5.rbz`

## Best Uses for Interior Work

- Skirting/baseboards, crown moulding, wall trim, decorative reveals.
- Door and window casings, jamb/frame massing, repeated panel frames.
- Cabinet frames, shelving rails, partition grids, slat/grille systems.
- Curved trim following arcs or non-orthogonal paths.
- Repeated profile members along paths that must stay editable.
- Assemblies where repeated spacing, offsets, and member profiles matter.

## Use with SketchUp MCP

Before Profile Builder:

```ruby
model = Sketchup.active_model
model.start_operation("Prepare Profile Builder paths", true)
paths_layer = model.layers["PB_PATHS"] || model.layers.add("PB_PATHS")
output_layer = model.layers["PB_OUTPUT"] || model.layers.add("PB_OUTPUT")
model.commit_operation
```

Create clean guide paths, grouped by design element, then use Profile Builder UI to build along those paths. Keep path groups in `PB_PATHS` so they can be hidden after output.

After Profile Builder:

```ruby
model = Sketchup.active_model
model.active_entities.grep(Sketchup::Group).each do |g|
  g.name = "PB_OUTPUT_" + g.entityID.to_s if g.name.empty?
end
model.active_view.zoom_extents
model.save
```

## Practical Prompt Patterns

- "Use Profile Builder to plan baseboards and ceiling trim for this SketchUp room."
- "Prepare PB paths for a slatted partition at 80 mm spacing."
- "Create a white-model wall panel grid that I can later build with Profile Builder."
- "Audit this model for Profile Builder readiness before I run the plugin."
- "Set up SketchUp tags/scenes for Profile Builder trim review."

## Cautions

- Some Profile Builder operations require interactive UI and licensing; do not force automation through private internals.
- Save a copy before large cut-opening or assembly operations.
- Do not over-detail concept white models; create profile placeholders first, then refine.
- If SketchUp startup errors mention Profile Builder licensing or `rgloader`, verify the `rgloader25.darwin.bundle` file exists.
