# Artisan 2 Reference

## Local Install

- SketchUp version verified: SketchUp 2025 `25.0.659`.
- Plugin installed: Artisan `2.1.2`.
- Loader: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_artisan2.rb`
- Plugin folder: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_artisan2`
- Ruby 3.2 macOS bundle: `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/DM_artisan2/so/bundle/3.2/MSS_Licensing.bundle`
- Source RBZ: `/Users/bonnie/Downloads/Artisan-2.1.2.rbz`

## Useful Interior Patterns

- **Cushion base**: create a low rectangular cushion block, bevel/soften major edges, then use Artisan smoothing/sculpting.
- **Organic table**: create an irregular low-poly stone-like top, subdivide/smooth, then keep legs as simpler native SketchUp geometry.
- **Curved wall/panel**: create controlled segmented surface first, use Artisan only to soften the visual surface.
- **Hero object**: keep complex Artisan object in its own component and use a simplified proxy for layout work.

## MCP Prep Snippet

```ruby
model = Sketchup.active_model
model.start_operation("Prepare Artisan organic modeling", true)
["ARTISAN_BASE", "ARTISAN_WORK", "ARTISAN_OUTPUT", "ARTISAN_PROXY"].each do |name|
  model.layers.add(name) unless model.layers[name]
end
model.save
model.commit_operation
```

## Prompt Patterns

- "Use Artisan workflow to plan a soft curved sofa mass."
- "Prepare an Artisan-ready base mesh for an irregular stone coffee table."
- "Audit this object before Artisan subdivision."
- "Create low-detail and high-detail versions for an organic feature wall."

## Cautions

- Artisan is interactive and licensed; do not force private plugin APIs through Ruby unless documented.
- Subdivision can rapidly increase face count. Keep a low-poly source and a proxy component.
- For construction or production furniture, convert the sculpted result into dimensions, sections, or fabrication references before treating it as final.
