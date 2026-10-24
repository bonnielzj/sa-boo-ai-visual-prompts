---
name: sa-boo-print-production-preflight
description: SA&BOO large-format print production preflight for hoardings, murals, signage, retail graphics, wall wraps, banners, and vendor handoff packages. Use when Hermes needs to turn approved visual concepts into printable artwork, check image/PDF physical size, DPI, ratio, bleed, panel splits, source-image lock, CAD-vs-hero-size conflicts, or create/review print deliverables before giving files to a printer.
---

# SA&BOO Print Production Preflight

Use this skill as the hard gate between an approved visual concept and a vendor-ready large-format print package.

Match the current request: **inspection** returns findings on existing artwork;
**single-file production** exports the requested print file; **panelled vendor
package** exports the contracted master, panels and handoff materials. A size/DPI
check or a single-file request does not require the full package.

## Non-Negotiable Gate

Before exporting final print files, answer these in writing or in a spec JSON:

1. **Which size is being produced?** Distinguish hero artwork size, installed visible face, CAD unfolded perimeter, panel size, and bleed size.
2. **Is the ratio locked?** Compare source ratio, target physical ratio, and output pixel ratio.
3. **How is mismatch handled?** State `crop`, `extend`, `tile`, `panelize`, or `do not proceed`. Never silently stretch.
4. **What resolution standard is used?** State full-size DPI and/or scaled artboard DPI.
5. **Where are guides?** Keep trim, door, cut, and panel guides out of print masters unless the printer explicitly asks for marked files.
6. **What is approved-source locked?** Once Bonnie approves a concept image, do not regenerate or alter composition unless she asks.

If an answer needed for final production is unclear, stop that export and ask one
focused question or mark that part `BLOCKED`. For an inspection, report the exact
unknown and keep dependent conclusions conditional. Mark irrelevant panel/guide
requirements as not applicable rather than expanding the task.

## Workflow

1. **Brief lock**
   - Record project name, approved source image, intended print size, applicable bleed, panel width when panelled, material/vendor assumptions, and whether CAD dimensions are placement reference or artwork size.
   - For hoardings, explicitly separate “visible announcement artwork” from “full unfolded site perimeter.”

2. **Ratio and DPI preflight**
   - Use `scripts/preflight_image.py` for relevant raster masters and representative panels. Its report is auxiliary evidence: `--expected-dpi` compares embedded metadata, not effective print resolution. Compare `effective_full_size_dpi_for_target` separately against the chosen viewing-distance/vendor requirement; missing or rewritten metadata does not change image detail.
   - The script's default ratio tolerance is a strict 0.5% fail threshold. The general inspection standard below has a 0.5–1% warning band; distinguish that design judgment from script status, and set a different accepted tolerance explicitly when applicable. Do not use `--warn-only` as production approval or treat a script PASS as full print acceptance.
   - Treat ratio mismatch over `0.5%` as a warning and over `1%` as a fail unless the output is intentionally cropped.
   - Treat missing DPI metadata as a warning; physical size cannot be trusted without a clear scale note.

3. **Production export**
   - Export only the contracted files: a clean or bleed master as required, and panel files when panelization is requested.
   - Create proof-only guides/contact sheets when they resolve a production risk or are part of the requested handoff; keep them separate from print masters.

4. **Vendor package**
   - For a requested vendor package, include the contracted print masters, applicable panels, useful proof, production specs, and source/crop metadata. Add separate README/spec JSON files only when the handoff needs them.
   - Label applicable folders clearly: `master/`, `panels/`, `proof/`, `assets/`.
   - Zip only when requested or required by the vendor handoff; include only the final set.

5. **Final QA**
   - Verify pixel size, DPI, physical size, ratio, approved-source fidelity, and applicable bleed. Check panel count/continuity when panelled, PDF render when PDF is delivered, and ZIP integrity when a ZIP is delivered.
   - Visually inspect the actual artwork, exact text and Logo geometry, and relevant font fidelity. Inspect an overview and panel contact sheet when panel continuity needs them.
   - State any remaining vendor decisions: CMYK conversion, black density, material, lamination, overlap, site trimming, vector text/QR.

## Preferred Large-Format Presets

Use one of these unless the printer gives another spec:

- **Full-size 72dpi**: practical for hoarding and mural print masters.
- **Full-size 100dpi**: safer when close viewing distance matters and file size is acceptable.
- **1:10 / 300dpi**: proof or lighter production file, equals full-size 30dpi.
- **1:10 / 720dpi**: equals full-size 72dpi; good for large-format master artboards.

For a `13000mm x 3000mm` hoarding:

- Full-size `72dpi` = about `36850 x 8504 px`.
- `1:10 / 300dpi` = about `15354 x 3543 px`.
- `1:10 / 720dpi` = same pixels as full-size `72dpi`.

Read `references/large-format-print-standards.md` when the project needs deeper size/panel/vendor judgment.

## Approved Source Lock

For production export, reuse the existing approval/source record or create an
`approved_source.json` when needed to preserve the approved source and crop.
An inspection alone does not require a new approval record:

```json
{
  "approved_source_file": "/path/to/image.png",
  "approved_crop_box_xyxy": [0, 173, 2140, 636],
  "locked_intent": "black Night Chalk / Smoke X-Ray hoarding",
  "target_print_size_mm": [13000, 3000],
  "forbidden_changes": [
    "no regenerated composition drift",
    "no silent stretching",
    "no mirrored typography",
    "no guide marks in print master"
  ]
}
```

## Script

Use:

```bash
python "$HOME/.codex/skills/sa-boo-print-production-preflight/scripts/preflight_image.py" \
  --input /path/to/master.jpg \
  --target-mm 13000x3000 \
  --expected-dpi 72 \
  --ratio-tolerance 0.005
```

The script prints a JSON report and exits nonzero on fail unless `--warn-only` is passed.
