# Tool and MCP routing

Checked 2026-09-23 against original repositories, source code, licenses and the local environment. Recheck before installation or relying on a current API. None of the four newly researched MCP servers was installed, started or connected by this skill-creation task.

## Use the capability needed

| Need | Suitable route | Evidence and limitation |
|---|---|---|
| Invent a graphic wordmark and refine its contours | Existing Figma vector tools; image generation only where a new expressive visual exploration helps | Figma has been used for actual editable paths and native curved text. Neither Figma nor image generation guarantees Chinese anatomy. |
| Get a reliable character scaffold or detect missing glyphs | FontTools + `outline_text.py` | FontTools 4.63.0 exercised locally for cmap and SVG paths. Extracted font outlines are not original lettering and require a separate license check. |
| Turn a viable black/white image into initial contours | VTracer, followed by visual and semantic correction | VTracer 0.6.15 exercised in a project-local virtual environment, not the global Python environment. It traces pixels; it does not understand Chinese. |
| General vector nodes, Boolean operations and path cleanup | Figma now; Inkscape CLI/editor when available | Inkscape was not found in checked local locations. An MCP wrapper is optional, not necessary to the drawing method. |
| Small experimental installable font | Font Design MCP as a future isolated pilot, or established font tooling | Candidate code is verified, its runtime is not. Current implementation has limits detailed below. |
| Larger actual typeface with glyph metrics/build/shaping | FontForge, FontTools/fontmake/HarfBuzz, or an already-available professional editor | Requires a scoped glyph set and runtime verification. Two custom words do not constitute a CJK font family. |

## Open-source MCP candidates

**repository-verified** means the stated capability was found in source. **runtime-tested** means it was actually exercised locally. Keep these separate in future reports.

| Candidate / pinned revision | Useful operations | Material constraint | Local status |
|---|---|---|---|
| [Kydaix/Font-Design-MCP](https://github.com/Kydaix/Font-Design-MCP/tree/0544d650de5eb30d68c8bd3fc5b2beb7d386ca86) · MIT · 2026-09-11 | Typed path/node editing, UFO project revisions, batches, metrics, TTF/WOFF2 builds, HarfBuzz/FreeType preview | Unicode scalar input exists, but current limits include 512 glyphs, 50,000 points and 256 text characters. No arbitrary SVG/UFO import, autotrace or OTF export. Chinese quality is not certified. | repository-verified; not run. Most relevant candidate for a small font-engineering pilot, not an automatic logo designer. |
| [LHxis/fontforge-mcp](https://github.com/LHxis/fontforge-mcp/tree/acd03e9c0377d3f6a9e4c4e5ea5c00116edb6623) · MIT wrapper · 2026-08-09 | Draw SVG paths, transform/clean contours, set metrics, save SFD, export fonts and previews | Needs FontForge and Python dependencies; upstream says macOS was not tested on real hardware. Exposes arbitrary Python and broad file paths. | repository-verified; no local FontForge runtime found in checked locations. |
| [grumpydevorg/inkscape-mcps](https://github.com/grumpydevorg/inkscape-mcps/tree/e621da1a8287896fa3a7bf8e3cf4fd6a9c2f87ea) · MIT · 2025-10-22 | Inkscape actions, SVG DOM changes, cleanup and validation | General vector control, not a font compiler. Chinese depends on host fonts/rendering. Static review did not establish a fully contained action/file boundary; do not repeat the README's hardening claim as a local guarantee. | repository-verified; no local Inkscape runtime found in checked locations. |
| [thierryc/Glyphs-mcp](https://github.com/thierryc/Glyphs-mcp/tree/590053fedd7bcab13a2027fb3bce99b724072b57) · Apache-2.0 wrapper · 2026-09-16 | Native glyph nodes, paths, Unicode assignment, kerning, analysis and export | Requires the separately licensed commercial Glyphs application on macOS. Has general code-execution interfaces. An open-source connector does not make its host open source. | repository-verified; no local Glyphs app found in checked locations. |

Do not install a server merely to label the workflow “MCP.” Prefer a current callable editor or tested local library when it already performs the needed operation. If the user asks for an installation, inspect the current revision/dependencies, isolate the trial, and validate a small actual Chinese round trip: mapping → contours → export → rendered glyphs. Respect the session's authorization; this document creates no additional permission gate for ordinary local work.

## Mature open-source foundations

- [FontTools](https://github.com/fonttools/fonttools) — MIT; font tables, Unicode mappings, outlines, subsetting and builds. Library-level tools do not make design decisions.
- [FontForge](https://github.com/fontforge/fontforge) — font editor and scripting. See its actual license: the combined work is GPL-3.0-or-later with many BSD-3-Clause files. It is distinct from the MIT MCP wrapper.
- [Inkscape](https://gitlab.com/inkscape/inkscape) — vector editor/CLI. Most code GPL-2.0-or-later with listed exceptions. Its active source is GitLab; an old GitHub mirror date does not establish abandoned development.
- [VTracer](https://github.com/visioncortex/vtracer) — MIT raster-to-SVG tracing. A high overlap score is not glyph or aesthetic validation.
- Glyphs and RoboFont are commercial applications; useful scripting ecosystems do not change that status.

## Source evidence and tested environment

Detailed source links, fixed commits, source line citations, license/README discrepancies and scope limits: [open-source-research.md](open-source-research.md).

Historical local research artifacts and machine-specific interpreters are not included in this package. Discover current dependencies in the active environment; see [local-helpers.md](local-helpers.md). Historical runtime notes describe only the tested setup, not a portable installed capability.
