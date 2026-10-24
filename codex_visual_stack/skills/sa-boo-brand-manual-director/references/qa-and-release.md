# QA and Release

## Four QA Layers

### 1. Evidence and Content

- authoritative sources are named;
- originals remain untouched;
- rule status is visible;
- fixed and proposed content are not mixed;
- approver, date, and version support every approved standard;
- every activated companion workstream links one bounded output and has no
  unresolved `PLANNED`, `ACTIVE`, or `BLOCKED` release dependency;
- translations match meaning and hierarchy;
- application examples do not imply unapproved permissions or official event use;
- related creative worlds have a legible bridge without inventing a shared style;
- song/lyric authorship is distinct from drawing or generated-derivative authorship;
- the book opens, develops its chapters, and closes with an intelligible purpose.

### 2. Editorial and Visual

- cover identifies the brand and document status;
- contents and page numbering are correct;
- hierarchy remains legible at normal viewing size;
- smallest type and bilingual lines are readable;
- page rhythm has intentional variation;
- the densest pages do not collapse;
- headings do not contain accidental hyphenation or broken brand terms;
- bilingual text contains no missing-glyph/tofu boxes or fallback-font drift;
- no auto-fit or font-shrinking pass has damaged the intended type hierarchy;
- widows, orphans, and awkward single-word wraps are resolved where visible;
- supplied mark and logotype paths, lettering, spacing, and lockup remain intact;
- clear space and reproduction recommendations retain their actual approval status;
- Chinese and English have useful, deliberate compositional roles;
- caption baselines and lower margins follow the authored system;
- images are sharp, correctly cropped, and legally usable;
- product shape, seams, artwork, color, texture, and lighting are represented well;
- cutout edges have no residue, halos, doubled edges, or implausible joins;
- blank pages and full-bleed pages are intentional;
- the manual still feels like the brand without relying on the logo alone.

### 3. Editable Source

For InDesign/Adobe sources, required pass targets include:

- overset text frames: `0`;
- missing or modified links: `0`;
- missing/substituted fonts: `0`, unless a documented compatibility version;
- image-placement errors: `0`;
- accidental RGB/CMYK/spot conflicts: `0`;
- hidden/locked objects causing export errors: `0`;
- page size or bleed mismatches: `0`;
- export failures: `0`.

Run `scripts/indesign_preflight_report.jsx` and preserve the report.

For Figma, PPTX, DOCX, HTML, Affinity, or another backend, replace these with
equivalent checks for missing assets/fonts, overflow, broken components/links,
incorrect canvas/page sizes, and export failure. Do not require IDML or Adobe
preflight for a non-Adobe project.

### 4. Production and Release

- PDF preset and color profile recorded;
- bleed, crop marks, and spreads/single pages match the destination;
- image effective resolution is appropriate;
- spot colors and rich black are intentional;
- transparency and overprint are reviewed;
- font licenses and template rights are recorded;
- packaged links open on another machine when required;
- requested compatibility formats are tested;
- release manifest contains filenames, hashes, status, and date.

## Visual Review Set

Render the actual deliverable and inspect every page at normal viewing scale.
Use contact sheets to review sequence and repetition, not as the sole quality
check. Inspect relevant photographs and retouched boundaries at 100%. Prioritize:

1. cover;
2. contents;
3. strategy spread;
4. master identity spread;
5. densest rule spread;
6. smallest type;
7. every language and special-symbol sample;
8. darkest and lightest page;
9. full-bleed/cropped image page;
10. application page;
11. chapter bridges and the final spread's actual closing function.

A background-removed product with collapsed shape, damaged texture, distorted
artwork, or poor lighting is not a finished hero. Make a faithful targeted repair,
select a better source view, or defer that application. A file opening correctly
and having adequate pixels cannot override a visible defect.

Automated blank-page detection is only a warning. Editorial blanks may be
intentional.

Zoom into headings and multilingual samples in the rendered pages. An
InDesign report can show zero missing fonts while the PDF still contains tofu
boxes because an installed Latin font lacks the required glyphs.

## Check Actual Authored Text Readback

Use `scripts/check_editorial_pages.py` when repeated authored pages need a small
geometry and omission check. Supply actual Figma/backend readback, not just the
intended layout plan. This tool reports specific page/node defects; it does not
assess typography, translation, photograph quality, or aesthetic approval.

```bash
"$PY" scripts/check_editorial_pages.py /path/to/page-readback.json \
  --margin 96 --content-bottom 824 --out /path/to/editorial-check.json
```

The defaults suit a 1600×1000 working canvas; override them for the actual authored
system. Input is `{"pages": [{"id", "name", "width", "height", "nodes": [...]}]}`.
Each text node supplies `id`, `name`, `characters`, page-relative `x`, `y`, `width`,
`height`, and `missingFont`. Name paired copy `Copy / zh / role` and
`Copy / en / role`. Both need nonempty actual text; set `bilingualRequired: false`
only for an intentionally unpaired role. A pair remains required if either member
declares it required. This checks presence, not faithful translation or hierarchy.

Ordinary text stays within content margins. `Footer` names are exempt from content
limits but remain within page bounds. Intentional display bleed uses
`allowBleed: true` or an `AllowBleed` name tag. Optional `--baseline-step` checks
only nodes with `snapBaseline: true` and an explicit authored `baselineY`; never
infer typographic baselines from bounding-box edges. Exit codes are 0 for no listed
violations, 1 for violations, and 2 for malformed input or CLI values. Inspect the
rendered spreads regardless of the result.

Include optional actual `fontSize` and `lineHeight` in readback. Nonempty text
whose actual box height is below 0.6× font size produces `degenerate_text_height`,
catching the observed Figma auto-height/resize regression. Line-height is retained
in the defect details for repair; it is not treated as a universal minimum height.
Read the narrow Figma recipe in [adobe-production.md](adobe-production.md) when
Figma is the selected backend and this clipping defect appears.

## Release Status

Use one:

- `INTERNAL_WORKING_MANUAL`;
- `CLIENT_REVIEW`;
- `APPROVED_GUIDELINE`;
- `PRODUCTION_RELEASE`;
- `SUPERSEDED`.

Do not use `final`, `final2`, `new`, or `use-this`.

## Release Package

```text
08_RELEASE_PACKAGE/
  editable/
  compatibility/
  pdf/
  assets/
  fonts_or_license_notes/
  approvals/
  qa/
  manifest/
```

The release folder must contain only the current approved set. Keep old
versions under `99_SUPERSEDED`.

After the payload is frozen, build its manifest with the verified Hermes Python
interpreter:

```bash
"$PY" scripts/build_release_manifest.py \
  --root "/path/to/project" \
  --status "CLIENT_REVIEW"

"$PY" scripts/validate_brand_manual_project.py \
  --root "/path/to/project" \
  --release
```

The manifest excludes its own directory, lists every payload path, size, and
SHA-256, and is invalidated by any later payload change. `APPROVED_GUIDELINE`
and `PRODUCTION_RELEASE` require at least one editable source file; a
`CLIENT_REVIEW` may be PDF-only only when the project config requests PDF only.
