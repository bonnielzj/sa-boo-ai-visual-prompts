# Digital, Publishing, and Review Handoffs

Read this reference only when the manual scope explicitly includes a
machine-readable digital contract, publish-ready social/case proofs, or a
separate approval presentation. The manual remains the orchestrator and source
of release status.

## `figma-generate-library` — Machine-Readable Digital Appendix

Trigger only when websites, apps, coding agents, or multiple digital products
need approved tokens or an editable variable/component library. Consume
`APPROVED_STANDARD` color, typography, spacing, layout, and component-state
rules plus decision IDs. Return:

```text
editable Figma variables/components
optional DESIGN.md
optional Tailwind export
optional W3C DTCG tokens.json
lint/WCAG report
manual page IDs and decision IDs used as sources
```

Do not infer official tokens from a rendered PDF or sampled artwork. Illustrator
MCP token extraction is measured evidence until approved. Do not force
photography, material, motion, spatial, or print-production rules into the
DESIGN.md schema. The token appendix must carry the same version/status as the
manual release that authorizes it.

## `sa-boo-case-publishing` — Application Proof

Trigger only when the page plan names a social/case-publishing application and
upstream rules are usable. Consume approved identity rules, source images,
platform sizes, project facts, and honest project status. Return SVG/PNG,
manifest, contact sheet, machine QA, and `REVIEW_REQUIRED` visual status.

The application proof may reveal a rule gap. Record that gap in the decision
register; do not let the publishing skill redefine or approve the identity.
Never treat generated files as authorization to publish externally.

## `sa-boo-presentation-director` — Separate Review Deck

Trigger only when reviewers need a presentation in addition to the manual.
Consume frozen manual pages or approved review exports, not a second copy of the
brand system. Default early review to `quick preview`; use standard/deep editable
routes only when requested. The deck may summarize gates and decisions but may
not become a parallel approval register or substitute for the editable manual.

## Workstream Completion

Record each activated handoff once in `workstream_register.csv`. Completion
requires one stable output path, its source IDs, version/status, and the manual
page or gate that uses it. No digital token file, social pack, or review deck is
a default deliverable.
