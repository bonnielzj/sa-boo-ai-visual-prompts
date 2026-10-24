# Local helpers

These helpers support construction and inspection; neither designs a finished wordmark or judges Chinese anatomy. Use a Python interpreter with `fontTools` for outlining; `preflight_svg.py` uses only the standard library. Discover a suitable runtime in the current environment. In Codex desktop, `load_workspace_dependencies` can locate the bundled runtime instead of guessing its path.

## Font coverage and outline extraction

```sh
python3 scripts/outline_text.py --font /path/to/font.otf --text '春日花开' --inspect
python3 scripts/outline_text.py --font /path/to/font.otf --text '春日花开' --output /path/to/work/lettering-base.svg
```

For a TTC collection, select the correct `--font-index` and inspect its returned family/style. Index 0 is not necessarily Simplified Chinese: the tested macOS PingFang collection's index 0 was PingFang HK Regular. Do not infer the region from the filename. A font collection can be enumerated with `fontTools.ttLib.TTCollection` when needed.

The output keeps each character in an independent group, with source glyph name, advance and baseline metadata. It flips the font's upward Y axis into SVG's downward Y axis. It is intentionally a simple horizontal cmap-to-outline operation:

- supported: single-line Han, ASCII and common CJK/full-width punctuation;
- missing glyphs fail explicitly; no substitute squares or fallback fonts;
- combining marks, variation selectors, control sequences and other scripts needing shaping fail explicitly;
- no shaping, kerning, vertical composition, font fallback or variable-axis selection;
- font-derived contours are not evidence of original drawing, and no font license is determined or bundled.

Use a shaping-capable engine and native font tools for IVS, contextual alternates, regional shaping or an actual font project. An extracted default variable-font instance is not a designed family.

## SVG structure

```sh
python3 scripts/preflight_svg.py /path/to/wordmark.svg --require-outlined --text '春日花开'
```

This reports paths, live text, embedded images, dimensions, external references, masks, filters and stroke declarations. `--require-outlined` requires a nonempty path or basic vector element and fails for image/feImage, text/tspan/textPath or foreignObject elements. Empty SVGs and empty path data fail. It does not resolve CSS, external resources or `<use>` references; inspect these warnings before claiming a self-contained asset. Presence of vector elements still does not prove useful, visible or correct drawing.

`--text` records expected copy only. `text_verified` deliberately remains false: there is no OCR or semantic glyph test here. Stroke declarations are reported but minimum physical stroke width is not measured.

## Verification scope

Check the current runtime and helpers before relying on their output. Useful
coverage includes glyph order and Y direction, missing glyphs, combining marks,
variation selectors, mixed image/text, empty SVGs and empty path data. Render
outline outputs and inspect the actual characters. These checks address helper
behavior; they do not establish aesthetic or production approval.
