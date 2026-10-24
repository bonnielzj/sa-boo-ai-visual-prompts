# Identity Tool Handoffs

Read this reference only after the task names a machine-readable token handoff,
a publish-ready application proof, a separate direction deck, or a live
Illustrator source audit. These are bounded outputs, not default companions.

## Machine-Readable Brand Contract — `figma-generate-library`

Activate when an approved identity must be consumed by websites, apps, coding
agents, or multiple digital products. Do not activate for a print-only manual or
before color/type/layout decisions are approved.

**Consume:** approved color roles, typography roles, spacing/layout values,
component states, accessibility requirements, decision IDs, and version.

**Return:** an editable Figma variables/component library plus, when requested,
`DESIGN.md`, Tailwind, or W3C DTCG exports; lint results; WCAG findings; source
decision IDs. Keep material, photography, motion, spatial, and print-only rules
in prose or their native specifications rather than forcing them into
unsupported token fields.

Run `npx -y @google/design.md lint DESIGN.md` before handoff. Extracted values
remain `MEASURED_EVIDENCE` until the brand decision owner approves them.

## Illustrator MCP Identity Audit

Use only with an open, verified source document. Start with one
`get_document_info` call. If no document is open or the server is unavailable,
stop or use the approved external JSX fallback; never switch to GUI automation.
Do not fan out several Illustrator MCP calls concurrently—the live application
bridge should be inspected in a bounded sequence.

Recommended read sequence, only as needed:

1. `get_document_info`, `get_artboards`, `get_layers`, `get_groups`.
2. `get_path_items`, `list_text_frames`, `get_images`, `get_colors`.
3. `extract_design_tokens` for a requested digital handoff.
4. `check_contrast` for named foreground/background pairs or bounded auto-check.
5. `get_overprint_info`, `get_separation_info`, and `preflight_check` for release.

Use read results as evidence, not automatic standards. Mutating tools such as
`replace_color`, `modify_object`, outline conversion, relinking, or export run
only after source authority, working-copy location, and the applicable approval
gate are explicit.

## Publish-Ready Application Proof — `sa-boo-case-publishing`

Activate only after the relevant identity/application rules are approved and
the user requests real social/case layouts. Consume approved logo, type, color,
grid, image rules, platform, source images, and honest project status. Return
editable SVG, publish PNG, manifest, contact sheet, machine QA, and
`REVIEW_REQUIRED` visual status. It may prove application behavior but cannot
redesign or approve the identity and never auto-publishes.

## Direction or Approval Deck — `sa-boo-presentation-director`

Activate only when the user explicitly requests a presentation. Pass the brand
thesis, evidence IDs, rule status, comparison decision, and approved/proposed
visuals. Use `quick preview` for first-round direction review unless a complete
editable deck is requested. The deck communicates decisions; it is not the
source of truth and cannot silently expand into a manual or rebrand.
