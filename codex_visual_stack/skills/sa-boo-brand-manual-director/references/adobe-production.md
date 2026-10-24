# Adobe Production

## Figma Text Production When Figma Is the Selected Backend

Load the installed Figma-use skill before its MCP call. This recipe addresses a
specific clipping regression observed on a live brand-manual proof: calling
`resize(width, 10)` after setting `textAutoResize = "HEIGHT"` left nonempty text
with a 10-pixel box and clipped the export. Set width before restoring automatic
height, then populate the actual text last. Load the actual font first.

```javascript
await figma.loadFontAsync(loadedFont);
const text = figma.createText();
text.fontName = loadedFont;
text.fontSize = typeSize;
text.resize(columnWidth, 10); // Temporary height, before auto-height.
text.lineHeight = { unit: "PIXELS", value: leading };
text.letterSpacing = { unit: "PIXELS", value: tracking };
text.textAutoResize = "HEIGHT";
text.characters = actualCopy;
```

For text inside a vertical auto-layout frame, append the child before assigning
its layout sizing. Use `text.layoutSizingHorizontal = "FIXED"` and
`text.layoutSizingVertical = "HUG"` for a fixed reading width and natural text
height. Use `parent.primaryAxisSizingMode = "AUTO"` and
`parent.clipsContent = false` where the authored parent should grow to its copy.
Do not overwrite a deliberately fixed or clipping composition with this recipe.

Read actual text height, font size, line-height, and parent bounds after authoring,
then inspect the rendered/exported page. A nonempty box below 0.6× its font size
is a clipping warning checked by `scripts/check_editorial_pages.py`; a taller
box still does not prove all text is visible or well composed. Do not rerun a
complete build when a bounded repair of affected text nodes resolves the defect.

## Illustrator

Use Illustrator for:

- native source audit;
- master artwork and lockups;
- bounds and ratio evidence;
- clear-space proposals;
- minimum-size tests;
- positive, monochrome, and reverse variants;
- behavior envelopes;
- clean release masters.

Recommended layers:

```text
00_GUIDES
01_OFFICIAL_MASTERS_LOCKED
02_MEASURED_EVIDENCE
03_WORKING_PROPOSALS
04_APPROVAL_REQUIRED
05_NOTES_STATUS
```

Recommended governance artboards:

1. Source audit.
2. Master artwork inventory.
3. Measurement evidence.
4. Asset hierarchy.
5. Clear space.
6. Minimum size.
7. Color/mono/reverse.
8. Placement.
9. Expression behavior.

Adapt this list to the identity. Do not force irrelevant boards.

Run `scripts/illustrator_identity_audit.jsx` with the best source open. The
script writes an audit JSON beside the document. Save a working copy before
organizing layers or artboards.

## InDesign Template Audit

Open a copy of the template and run
`scripts/indesign_template_audit.jsx`. Review:

- page size, facing pages, and page count;
- masters;
- frame counts and bounds;
- paragraph and character styles;
- fonts and link status;
- swatches;
- preview PDF;
- template rights.

Do not build by numeric frame index until a frame map is captured. Prefer
script labels or object names where possible because indexes are brittle.

Test multilingual glyph coverage in the selected font files. An installed font
can still lack required glyphs, so a missing-font count of zero does not prove
that Chinese, Japanese, Korean, Arabic, or special symbols render correctly.

## Build Script Pattern

Create one project-specific ExtendScript:

```text
find/open target document
-> define project paths and tokens
-> verify fonts and assets
-> populate labeled frames
-> place images with explicit fit rules
-> apply bilingual styles
-> check overset and links
-> save working INDD
-> export IDML and PDF
-> write QA report
```

Keep brand paths, fonts, page mappings, and copy in the project script or a
project config, never in this reusable Skill.

Use idempotent operations where practical. Write build errors to a visible log.
Do not silently shrink text until overset disappears. If a temporary fit pass
is used during prototyping, record every changed frame and fail release until
the intended type role, frame, copy, or page architecture is corrected.

Disable hyphenation on display headings unless the language and art direction
explicitly require it. Review bilingual line breaks in rendered pages; direct
formatting and installed-font checks do not catch missing-glyph boxes.

## Native MCP Audit Matrix

Use MCP only with a verified active document. Start with one
`get_document_info` (Illustrator) or `get_session_info` (InDesign) call. If no
document is open, stop before deeper inspection. Run a bounded serial sequence;
do not fan out many live-app MCP calls concurrently because clustered calls can
trip the bridge's unreachable/retry protection and make the workflow slower.

### Illustrator

Choose only the calls required by the current gate:

- structure: `get_document_info`, `get_artboards`, `get_layers`, `get_groups`;
- identity evidence: `get_path_items`, `list_text_frames`, `get_images`,
  `get_colors`;
- digital handoff: `extract_design_tokens`, then `figma-generate-library` plus
  validation/export when the scope explicitly requests tokens;
- accessibility: `check_contrast` on named pairs or a bounded auto-check;
- print/release: `get_overprint_info`, `get_separation_info`,
  `preflight_check`, and the requested export.

Treat extracted tokens, colors, bounds, and fonts as `MEASURED_EVIDENCE` until
approved. Read-only inspection does not authorize `replace_color`,
`modify_object`, outline conversion, relinking, or export from the official
master.

### InDesign

Use the connected UXP MCP for supported operations:

- structure: `get_document_info`, `get_document_layers`,
  `get_document_elements`, `get_page_content_summary`;
- system evidence: `get_document_colors`, `get_document_styles`,
  `get_document_grid_settings`, `get_document_stories`, `get_image_info`;
- QA: `validate_document`, `preflight_document`, page/image exports, and final
  `export_pdf` when the real document and preset requirements are known.

The bundled JSX audits remain deterministic fallbacks for measurements or
checks not covered by the live MCP. Do not run both paths merely to duplicate
the same report; choose one owner and preserve its artifact.

## macOS Launching

Load `bonnie-creative-backend-routing` and prove the real connection before
mutation. Preferred order:

1. `illustrator-mcp` for Illustrator; external JSX through
   an explicitly configured `VI_ILLUSTRATOR_JSX` adapter as the only fallback.
2. Connected `indesign-uxp` for supported InDesign DOM operations; external JSX
   through an explicitly configured `VI_INDESIGN_JSX` adapter when the bundled or
   project-specific audit/build requires ExtendScript.

Fallback patterns:

```bash
: "${VI_ILLUSTRATOR_JSX:?Set the path to an installed native JSX adapter}"
"$VI_ILLUSTRATOR_JSX" /absolute/path/to/script.jsx

: "${VI_INDESIGN_JSX:?Set the path to an installed native JSX adapter}"
"$VI_INDESIGN_JSX" /absolute/path/to/script.jsx
```

Native adapters are optional host capabilities and are not bundled here. Verify
that the selected adapter addresses the correct application, reads external JSX
and calls its native scripting interface. Keep production logic in external files. Do not
add a `#target indesign` directive when the InDesign wrapper passes source text;
InDesign 2026 can return exit code `0` without executing that source. A deliberate
no-document error is a valid transport smoke test; a silent zero is not.

Never use `System Events`, mouse/keyboard automation, menu selection, or
screenshot-driven clicking. Verify a named AI/INDD/IDML/PDF/export and reopen
the native document before claiming success.

## File Production

Keep:

- editable `.indd`;
- compatibility `.idml`;
- working `.ai`;
- review PDF;
- print PDF when required;
- packaged links;
- permitted fonts or a font/license note;
- build scripts;
- QA reports.

Do not put diagnostic experiments in the release folder.

## Automation Success

Do not call the workflow successful until:

1. The real Adobe file opens.
2. The script runs without hidden interaction.
3. The working file saves.
4. IDML/PDF exports are created.
5. Preflight finds no structural failure.
6. Rendered pages show no missing glyphs, accidental heading hyphenation, or
   auto-fit damage.
7. Rendered pages pass visual inspection.
