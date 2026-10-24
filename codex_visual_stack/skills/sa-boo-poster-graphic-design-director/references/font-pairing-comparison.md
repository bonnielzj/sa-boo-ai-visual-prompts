# Comparing font combinations in an existing design

Use when the user requests font alternatives or an unresolved font choice materially
affects the work. The active brand, graphic, presentation, or UI owner retains the
brief and authoring surface. This is a comparison method, not a new design-review
front door or a replacement for original lettering.

## Choose meaningful alternatives

Inspect the actual design and copy before choosing faces. Identify purpose,
audience, density, visual tone, and text roles; note what the current typography
does well. Keep analysis brief enough to reach a visible comparison promptly.

Select a small set that tests distinct, relevant typographic relationships. Follow
the requested number and directions; do not automatically add five alternatives,
an adventurous option, or a serif/sans contrast. A single family with appropriate
weights may serve the brief. Font swapping cannot repair a weak message or turn
ordinary text into custom lettering.

Use the same representative project copy across alternatives, including long
headings and dense detail where relevant. Compare on the current layout or useful
representative slides/screens, not only in isolated font specimens. A speculative
reconstruction from a raster image is not an edit to the original artwork.

## Preserve authority and classify roles

- Keep the original intact. Put requested alternatives in separate versions,
  duplicate frames, or previews appropriate to the current authoring surface.
  Do not create a new Figma file or change tools merely to compare fonts.
- Exclude supplied logos, wordmarks, custom lettering, and approved master
  typography unless their revision is explicitly authorized. Preserve copy,
  imagery, colors, and unrelated layout while testing font choices.
- Map headline, body, caption, numeral, and accent roles by actual hierarchy and
  text styles, not original family alone. One family may serve multiple roles.
  Preserve meaningful inline emphasis, links, and mixed-script runs.
- Initially keeping size, spacing, and line height comparable can isolate the
  effect of a family change. It does not preserve geometry: widths, baselines,
  wraps, and apparent weight can change. Check the result before showing it;
  make scoped optical adjustments when allowed, or flag the needed adjustment
  when the brief fixes those metrics. Avoid silently rewriting copy to make a
  candidate fit.

## Evaluate Chinese and bilingual typography

Verify the actual required glyphs and regional forms, punctuation, numerals, and
weights. Look for missing characters and unexpected fallback; a valid Latin face
does not demonstrate Chinese support. If separate faces serve different scripts,
make that pairing explicit.

Compare apparent size, weight, density, baseline, spacing, and punctuation between
scripts. Judge their intended semantic roles and cultural voice rather than
forcing identical shapes or mechanical size ratios. Test actual Chinese and Latin
strings at the intended output scale. Web body-size conventions do not determine
poster, slide, print, or signage typography.

Font availability is specific to the editor and current user environment; it is
not synonymous with the Google Fonts catalog. Check the intended use and license
before downloading, embedding, distributing, or including fonts in a production
master. An available or successfully loaded font does not establish those rights.

## Figma execution, only when Figma is the working surface

Load the current `figma:figma-use` skill before `use_figma`. Establish access to the
actual editable selection; these API names alone do not demonstrate a working
integration or permission to edit an unrelated file.

- Query `figma.listAvailableFontsAsync()` and use the exact returned family/style
  values. Do not normalize style names by inserting or removing spaces. Check
  `hasMissingFont`; do not silently replace a missing authoritative font.
- Load the fonts required by the operation with `figma.loadFontAsync()`. For
  content or layout-property edits, account for fonts already used in the text.
  Inspect mixed runs with `getStyledTextSegments()` or range APIs and apply font
  changes to the relevant ranges; do not flatten a mixed node to one font.
- Preserve role and emphasis when mapping weights/styles to the available family.
  Where a corresponding style is absent, choose an intentional available
  alternative and inspect the result rather than inventing a style name.
- Respect component overrides, linked text styles, auto layout, and frame bounds.
  Keep the approved original and avoid editing a shared main component or text
  style merely to create a comparison variant.

Consult [Figma's text API guide](https://developers.figma.com/docs/plugins/working-with-text/)
for current loading, mixed-run, variable-font, and missing-font behavior when those
details affect implementation.

## Inspect and present the comparison

Inspect each actual rendered alternative at viewing scale and relevant detail.
Check Chinese characters, fallback, wraps, clipping, overlap, baseline, hierarchy,
and type-image relationships; compare with the original and protect unchanged
identity. For slides, inspect the native render/export where font substitution
could differ from the authoring view. For UI, check the affected narrow width and
long-content case, not every unrelated breakpoint.

Show the alternatives together when useful, with concise font names and the
design difference being tested. Use consistent project text so the comparison is
fair. Fixed label dimensions, English joke copy, decorative specimen boards, and
extra reports are not default deliverables. A recommendation should explain the
visible benefit and any trade-off; selection and approval remain the user's.

This is an independently written adaptation of useful ideas in the user-supplied
Font Pairings text reviewed on 2026-10-24. No upstream plugin, code, font, or
runtime is included, and no source authorship or license is inferred from that
attachment.
