# MCP / Tool Routing for Visual Prompt Work

Use this when the user asks which MCP, plugin, connector, or model route should
handle a visual task, or a required capability is missing. Start with relevant
tools exposed in the current session; do not enumerate unrelated tools or treat
a dated snapshot as current availability.

## Environment-specific discovery

Adobe/CAD bridges, Figma routes, and image backends are host capabilities, not
included dependencies or proven connections in this package. Inspect only the
relevant currently exposed capability. Historical tool names do not establish
present installation, account access, or supported operations.

## Proof within the actual task

An exposed, applicable capability may perform the authorized actual task directly.
Its result and necessary readback or rendered inspection establish scoped proof;
tool exposure alone does not prove success. Load required tool prerequisites and
confirm the intended account/file before a write. Do not precede every call with
a separate diagnostic generation or reversible mutation/export probe. Add a
focused check when the account, backend, permissions, or required capability
changes, or when actual execution reveals a failure. Preserve authorization and
data-destination boundaries.

## Bitmap generation/editing — Bonnie route

Use:

`brief/reference → concise prompt → current image generation/edit tool → inspect actual standard-resolution preview → targeted repair if needed → show result`

Rules:

- Use the relevant image capability exposed in this session and its documented
  inputs. A historical backend name does not override the current callable tool.
- Do not print or persist credentials.
- Check the actual preview for exact copy, character anatomy, count, supplied
  logo integrity, and requested change; preserve unrelated regions during edits.
- Use a local repair when it resolves a real text or identity defect. Enter an
  editable layout or production workflow only when that deliverable is requested.
- Upgrade to 2K/4K only after Bonnie selects the preview and explicitly requests it.

Upstream OpenAI reference: https://developers.openai.com/api/docs/guides/image-generation

## Canva: design connector vs developer-docs MCP

Do not conflate these two products:

1. **Canva plugin / AI Connector**
   - Production route for searching, creating, editing, resizing, translating, and exporting designs after install and authorization.
   - Canva's Magic Layers workflow can convert a flat image into editable design layers in supported AI-assistant integrations. Confirm the exact tool is exposed after connection.
   - Official capability source: https://www.canva.com/newsroom/news/magic-layers-ai-assistants/

2. **Canva Developer MCP**
   - Endpoint: `https://mcp.canva.dev/mcp`
   - Purpose: answer Canva Apps SDK development questions.
   - Limitation: cannot create or edit Canva designs.
   - Official docs: https://www.canva.dev/docs/mcp/

The current official Canva developer documentation lists `https://mcp.canva.com/mcp` as the remote server. Do not confuse it with the separate Canva developer-docs MCP page or with a local Canva plugin; production access still depends on client support, waitlist/eligibility where applicable, OAuth, and scopes.

## Figma official MCP

Remote endpoint: `https://mcp.figma.com/mcp`

Current official capabilities include reading design context, screenshots, variables/components, asset download, `create_new_file`, FigJam diagram generation, Code Connect, and supported write-to-canvas workflows. Remote OAuth authorization is required; supported clients, plan, seat, and beta status can limit availability.

Official docs:

- https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/

Best route when connected:

`prompt/reference image → Figma target selection → reuse variables/components → write/edit canvas → screenshot/visual QA → export`

## Adobe production routes

Use a currently exposed Adobe connector or relevant native bridge when the
requested deliverable needs it. Historical discovery hints include Illustrator
MCP/JSX, `hermes-photoshop-jsx`, and `hermes-indesign-jsx`; use them only when
available and applicable. Follow the proof and permission rule above. A past
absence of a Firefly connector does not establish its current availability.

## MCP compatibility gate

- Treat `2025-11-25` as the current stable MCP protocol revision unless official docs show a newer stable release.
- Draft features and extensions such as Tasks, Apps, Skills over MCP, or new server discovery should be capability-negotiated; do not assume every client/server supports them.
- Prefer stable primitives for production: tools, resources, prompts, sampling, roots, authorization, and explicit capability negotiation.
- Check schema version, auth method, read/write scope, data destination, and destructive actions before connecting a server.

Sources:

- https://modelcontextprotocol.io/specification
- https://modelcontextprotocol.io/development/roadmap

## Installation and authorization policy

- This automation may install only a clearly matching curated/official plugin after user approval.
- Do not modify unrelated text-provider or relay configuration during a visual task.
- Ask before authorizing external accounts or exposing private/client files.
- Start with the narrowest scopes and test with non-client assets.

## Decision matrix

| Goal | Best route | Gate |
|---|---|---|
| Visual concept image | current exposed image tool | inspect the actual standard-resolution result |
| Multi-reference edit | current edit tool + reference roles and preserve/change contract | actual target and preserved-region checks; add a focused capability check only on change or failure |
| Exact typography social cover | compose real copy with the image; local repair if needed | actual copy and supplied identity check; external authorization when required |
| Editable brand kit/templates | current applicable editable connector | intended account/file, required permissions, actual readback/export |
| Proposal deck | current `Presentations`/PDF skills + optional requested assets | inspect actual deck/export; preserve external authorization boundaries |
| Web/UI direction | Product Design + Figma + local prototype/browser QA | target file, prerequisite skills, and write permission |
| Trend research | web/browser + design-research-radar | source/date/rights check |
| Batch campaign system | requested variants/formats; editable template only for a requested editable system | brand locks + actual output checks |
