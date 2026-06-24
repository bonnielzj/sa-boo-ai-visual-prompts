# MCP / Tool Routing for Visual Prompt Work

Use this when the user asks which MCP, plugin, or tool should handle a visual task.

## Current usable routes in this Codex environment

### Built-in image generation (`imagegen` skill + `image_gen` tool)

Use for: bitmap concept images, product shots, social visuals, raster mockups, edits, style variants.

Route:
`brief → prompt operating system → image_gen → inspect/iterate → save final asset if project-bound`

Notes:
- For transparent assets, use chroma-key removal first unless true native transparency is explicitly confirmed.
- For exact text, generate background/visual separately and set typography in Figma/Canva/PPT.

### Figma plugin skills/MCP tools

Use for: design systems, screens, components, layouts, diagrams, proposal pages, social cover systems, reusable templates.

Relevant skill routes:
- `figma:figma-use` before Figma write/read actions.
- `figma:figma-generate-design` for full screens/pages.
- `figma:figma-generate-library` for components/tokens/design systems.
- `figma:figma-generate-diagram` for FigJam/Mermaid-style diagrams.
- `figma:figma-code-connect` for mapping Figma components to code.

Best visual workflow:
`prompt visual concept → generate/reference image if needed → build Figma layout with tokens/grid/text → export PNG/PDF/PPT`

### Browser/control and shell/node

Use for: inspecting public trend pages, capturing references where permitted, comparing visual examples, building local moodboard HTML, scraping only compliant public data.

### Documents / presentations / pdf

Use for: turning prompt systems into client-facing proposal decks, PDF trend reports, prompt playbooks, or workshop material.

## Canva MCP route — available as official remote MCP, not necessarily installed here

Official docs: https://www.canva.dev/docs/mcp/

Canva states its MCP can support design generation/editing, design discovery, asset and brand management, export in multiple formats, and comments. It uses remote server:

`https://mcp.canva.com/mcp`

If an AI assistant does not support remote MCP directly, Canva documents `mcp-remote` as a bridge. Setup generally requires a Canva account, OAuth/connector authorization, and a client that supports MCP. Some integrations may require waitlist/allowlist or plan-specific features.

Use when connected:
`brief → Canva template/brand kit search → generate or edit design → resize/export → comment/review`

Do not claim Canva MCP is active unless the current tool list exposes a callable Canva tool.

## Figma official MCP context

Official blog: https://www.figma.com/blog/introducing-figma-mcp-server/

Figma frames MCP as design-context for coding/design workflows: component metadata, variables/styles, screenshots, interactivity/code representation, and content/layer names help LLMs preserve design intent. In this Codex environment, prefer existing Figma plugin skills for actual file creation/editing unless a separate official Figma MCP is explicitly available.

## Plugin installation policy for this environment

- Install only if a matching plugin/connector appears in the available install list and exactly matches the user's request.
- If no Canva/Pinterest/Behance/Adobe plugin is available, report that clearly and provide future setup steps.
- Do not modify local proxy or AiMaMi relay configuration.
- For private/client files, ask before connecting external accounts or uploading assets.

## Decision matrix

| Goal | Best route | Why |
|---|---|---|
| Visual concept image | imagegen | Fast bitmap exploration |
| Exact typography social cover | imagegen background + Figma/Canva layout | Models often distort text |
| Brand kit / reusable templates | Figma or Canva MCP if connected | Tokens, layouts, exports |
| Proposal deck | presentations/pdf + Figma assets | Client-ready structure |
| Web/UI direction | Figma generate-design + optional imagegen hero | System/grid/control |
| Trend research | web/browser + design-research-radar | Current evidence needed |
| Batch content calendar visuals | prompt matrix + Figma/Canva templates | Consistency and speed |
