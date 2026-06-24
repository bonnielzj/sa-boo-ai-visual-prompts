# Plugin / MCP / GitHub Evaluation for Figma Brand Kit

## Use available MCP first

If `use_figma` and Figma skills are available, they are the primary route for creating variables, styles, components, and templates directly in Figma.

Use:
- `figma-use` for safe Figma Plugin API calls.
- `figma-generate-library` for tokens/components/library architecture.
- `figma-create-new-file` before creating a new Figma file.
- `figma-generate-design` for full proposal/template pages.
- `figma-code-connect` only when mapping Figma components to code.

## Recommended Figma plugins for manual installation

These cannot always be installed by Codex directly; install from Figma Community if needed.

1. **Tokens Studio for Figma**
   - Best for: design tokens, GitHub sync, multi-brand/multi-theme systems.
   - Use when: SA&BOO wants token JSON versioning or future website/app handoff.
   - Risk: overkill for simple brand-kit files; set naming rules first.

2. **Iconify**
   - Best for: quick icon search/import.
   - Use when: proposal templates need consistent iconography.
   - Risk: mixed icon styles; limit to one icon family.

3. **Content Reel / Unsplash / similar content helpers**
   - Best for: placeholder content.
   - Risk: placeholder images can leak into final decks; replace with licensed/project assets.

4. **Stark / Contrast**
   - Best for: accessibility and contrast checks.
   - Risk: luxury low-contrast aesthetics may fail readability; client-facing pages must stay legible.

5. **Batch Styler / Themer / Design Lint**
   - Best for: style cleanup and consistency.
   - Risk: can mutate many nodes; duplicate file before bulk operations.

## GitHub resources worth knowing

- Figma MCP server guide: `figma/mcp-server-guide` — official guide for Figma Dev Mode MCP.
- `GLips/Figma-Context-MCP` — popular community MCP for exposing Figma layout context to coding agents.
- `Tokens Studio` documentation — token workflow and Git sync with Figma.
- `Style Dictionary` — convert token JSON into CSS/JS/native token formats.
- `Manavarya09/design-extract` — extracts website design systems into DTCG tokens and includes MCP ideas; useful for benchmarking, not a SA&BOO source of truth.

## Decision rules

- For SA&BOO proposal/social templates: use native Figma variables/components + Codex Figma MCP.
- For code/web handoff: add Tokens Studio + Style Dictionary.
- For inspiration/benchmarking: use community resources, but never copy visual identity directly.
- For social platform templates: build native Figma components and variants; do not rely on random template files.
