# Figma and vector execution notes

These are observations from the September 2026 environment, not a guarantee that every future server supports the same API. Load the installed `figma-use` skill and inspect the relevant API docs before use. Discover actual tool names rather than assuming an MCP from the research catalog is connected.

## Editable structure

- Inspect the current page and source node before changing it. Preserve old directions; create a sibling version for a major redesign. Use returned node IDs, never guessed next IDs.
- A new wordmark may be imported with `figma.createNodeFromSvg(svg)`. Check the resulting children are VECTOR nodes, not image fills. Keep a plain-text source string in the project record.
- Font mutations require the current fonts to be loaded first. Use verified family/style names. Noto Sans SC Medium was available in this file; its presence elsewhere must be checked.
- Native `createTextPath` can keep secondary orbit copy editable. Define a vector path first, create the text path, and set its font/content after loading fonts. In the tested environment conversion reparented the returned TEXT_PATH to the page. Append the **returned node** back to the intended frame and then apply its relative transform. Inspect parent ID and actual screenshot.
- `setRangeFontSize` and `setRangeLetterSpacing` allow smooth per-character motion on a native text path. Do not mutate the underlying vector after conversion without checking current API support.
- Artwork coordinates and text paths are geometric composition; an auto-layout row is not a substitute for orbit geometry. Use normal auto-layout for accompanying editorial blocks when needed.

## A useful orbit construction

For ellipse radii a,b and parameter θ, the tangent is `(-a sinθ, b cosθ)`. Numerically integrate `sqrt(a² sin²θ + b² cos²θ)` to sample equal arc lengths. For native text paths, use the editor's measured glyph advances and controlled tracking.

A smooth size rule such as `s(u)=mean+amplitude*cos(2π(u-phase))`, with `u∈[0,1)`, can express perspective. Keep the same value/derivative at the seam. If glyph widths vary, calculate total advance after applying the sizes; simply multiplying character count by nominal font size is insufficient for mixed scripts or proportional characters.

Always inspect the screenshot; correct mathematics alone does not establish good spacing or copy visibility.

## Generated concepts and tracing

Use the provided image-generation workflow for image generation/editing. A traced concept is useful only after inspecting and correcting its character skeleton. Preserve the generated source and do not claim its pixels were native vectors.

VTracer 0.6.15 was locally exercised with this starting point for a clean monochrome concept:

```python
vtracer.convert_image_to_svg_py(
    input_path, output_path,
    colormode="binary", mode="spline", filter_speckle=2,
    corner_threshold=30, length_threshold=3.5,
    max_iterations=20, splice_threshold=20, path_precision=4,
)
```

This is a tunable example, not a prescribed aesthetic. Thresholding may erase fine tips or enlarge counters. A high source/trace IoU measures pixel overlap, not Chinese correctness, originality or curve quality. After tracing, inspect at least: holes, disconnected islands, tiny fragments, contour kinks and vulnerable radicals.

## Export without false editability

Keep a live Figma source when available, a standalone contour SVG, and a PNG of the actual canvas. Export outline text for a portable contour asset; retain editable secondary text in the native source. An outlined SVG does not remain editable as a typed font string, though its paths remain editable.

Check whether a white artboard rectangle was exported. For a transparent deliverable, remove only the known artboard background, not white counters/masks that are part of the design. Verify all paths and the alpha/background result. Render or inspect the actual export, not only the editor.

The tested `use_figma` response truncated a large returned SVG JSON string near 20,500 characters, even though `exportAsync` succeeded. A truncated JSON response is not an empty export. Preferred route: use a supported file export/download result. If unavailable, read the declared total length and fetch deterministic, indexed slices smaller than the transport cap (19,000 characters worked), checking every chunk, final length, parseability and export identity before writing. Keep the canvas unchanged during chunked reads. Do not invent a file URL or silently accept partial SVG.

The local helper `preflight_svg.py` checks structure only. A file can contain pure paths and still have an incorrect character or a poor silhouette.
