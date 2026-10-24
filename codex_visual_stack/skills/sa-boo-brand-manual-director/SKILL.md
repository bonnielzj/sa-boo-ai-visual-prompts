---
name: sa-boo-brand-manual-director
description: "Use when building or releasing an editable brand manual. Separates source authority, brand-system gaps, editorial style, production, and QA; conditionally routes research, curation, social/IP, and spatial co-design without duplicating ownership."
metadata:
  hermes:
    tags: [brand-manual, identity-governance, editorial, production, qa]
    related_skills: [sa-boo-brand-director, sa-boo-visual-first-core, sa-boo-premium-reference-curator, sa-boo-design-research-radar, sa-boo-xiaohongshu-ip, sa-boo-co-design-interior-partner, sa-boo-visual-asset-index, sa-boo-case-publishing, sa-boo-presentation-director, figma-generate-library, sa-boo-print-production-preflight, bonnie-creative-backend-routing]
---

# SA&BOO Brand Manual Director

Build a brand manual through a fixed, auditable process while allowing the
visual style, page architecture, density, and editable production method to change
with each brand.

## Governing Principle

Separate four jobs that are often confused:

1. Diagnose the brand system.
2. Develop missing identity rules.
3. Design the editorial manual.
4. Produce and release the files.

A polished book cannot repair an unresolved brand system. A strong brand system
does not justify a generic manual layout.

## Manual eligibility gate

A request to discuss a theme, naming, cultural idea, campaign narrative, or merchandise concept is **not yet a brand-manual project**, even when this skill is invoked explicitly. Return the task to `sa-boo-brand-director` and keep it text-led until the brand decision is approved. Do not create manual pages, diagrams, abstract visual territories, palette boards, or editorial templates to simulate progress.

This skill may resume only when the user asks to govern, document, paginate, edit, or release approved/proposed brand rules in a manual. An invocation changes routing priority; it does not waive the entry gate.

## Companion Router

This skill remains the **orchestrator and gate owner** for the manual. Load a
companion only when its trigger is true; never activate the whole bundle by
default.

| Companion | Activate only when | Return to the manual project |
|---|---|---|
| `sa-boo-brand-director` | strategy or identity rules are missing and the route is not `manual-only` | proposed rules, status, evidence, decision request |
| `sa-boo-design-research-radar` | a page makes current, market, channel, trend, or capability claims | dated evidence brief, source links, uncertainty, usable claims |
| `sa-boo-premium-reference-curator` | Gate A is open or an application needs taste-led external precedents | accepted asset IDs, selection logic, rejection notes, rights status |
| `sa-boo-xiaohongshu-ip` | Xiaohongshu, Channels, short video, or personal IP is a named priority application | channel specification and application proofs based on upstream rules |
| `sa-boo-co-design-interior-partner` | interior/spatial application behavior needs shared design judgment | spatial proof, exceptions, decision requests, approved evidence paths |
| `sa-boo-visual-asset-index` | accepted visuals must be cached, cited, chained, or retrieved | canonical asset records and contact-sheet paths |
| `figma-generate-library` | approved digital token and variable handoff | Figma variables/components + structural readback and visual evidence |
| `sa-boo-case-publishing` | approved social/case proof | SVG/PNG + manifest/QA |
| `sa-boo-presentation-director` | explicit separate review deck | deck citing manual page/decision IDs |

Use `sa-boo-visual-first-core` as the visual doctrine, not as a second workflow.
Use `bonnie-creative-backend-routing` and its macOS native-automation contract only for an actual macOS Adobe launch.
Use `sa-boo-print-production-preflight` only for vendor-ready production art.
Use the Figma brand-system mode in `bonnie-creative-backend-routing` only after its account/data-access and live-backend gates pass; otherwise select an available editable document or presentation workflow. A disabled optional backend must not block the project.

**Single-owner rule:** research currency belongs to Radar; taste curation to the
Curator; persistent visual metadata to the Asset Index; upstream identity rules
to Brand Director and the decision register; social application behavior to
Xiaohongshu IP; spatial interaction to Co-design; page architecture, gates, and
release status stay here. Reuse the returned artifact path or ID instead of
repeating the work.

Read [companion-skill-routing.md](references/companion-skill-routing.md) for the
stage map, handoff fields, fast paths, and duplicate-work firewall. Read
[digital-and-publishing-handoffs.md](references/digital-and-publishing-handoffs.md)
only when the scope names tokens, publish-ready application proofs, or a separate
review deck.

## Execution Preflight

For script, Adobe, PDF-render, release, or skill-maintenance work, read
[runtime-and-maintenance.md](references/runtime-and-maintenance.md) before
execution. It owns interpreter selection, backend proof, the native PDF fallback,
no-GUI rules, and maintainer tests. Skip it for purely conceptual/editorial work.

## Five-Question Startup

Inspect supplied files and prior decisions before asking anything. Prefill known
answers. Ask only unresolved, high-impact questions. Prefer zero questions when
the files are sufficient; otherwise batch the remaining blockers into one
compact confirmation. Five is the maximum number of unresolved fields, not five
required conversational turns.

1. What is the job: govern an existing identity, refresh an incomplete system,
   create a new identity, or only redesign/edit the manual book?
2. What is fixed, developable, approval-required, or deferred?
3. Who will use and approve the manual, and which applications matter first?
4. What should the brand feel like, and what must it never feel like?
5. What outputs, languages, format, template, deadline, and Adobe compatibility
   are required?

Accept references, adjectives, sliders, or examples as style answers. If the
user says to proceed, use conservative defaults and mark unresolved decisions
`TBD / VERIFY`; do not prolong intake.

Read [startup-qa-and-config.md](references/startup-qa-and-config.md) for the
question branches and project schema.

Initialize a reusable project:

```bash
"$PY" scripts/init_brand_manual_project.py \
  --root "/path/to/project" \
  --brand "Brand Name" \
  --mode "brand-refresh" \
  --languages "zh-CN,en" \
  --outputs "indd,idml,pdf" \
  --style-direction "open" \
  --fixed "logo,primary color" \
  --develop "typography,grid,graphic signals" \
  --verify "wordmark crop,color conversions" \
  --defer "photography,motion"

"$PY" scripts/register_local_assets.py \
  --root "/path/to/project" \
  --source "/path/to/client/assets" \
  --authority-status "MEASURED_EVIDENCE" \
  --rights-status "CLIENT_SUPPLIED_INTERNAL"
```

## Entry Decision

Choose one route:

- `existing-governance`: preserve approved masters, audit sources, propose
  governance, then manualize.
- `brand-refresh`: protect fixed assets, develop missing minimum rules, approve
  the system, then manualize.
- `new-identity`: complete strategy, concept, master-artwork approval, and
  governance before manual production.
- `manual-only`: use only when the brand system is already approved and the task
  is editorial redesign, update, localization, or file repair.

Never silently turn `manual-only` into a rebrand.

## Workflow

### 0. Intake and Source Authority

Create the project config, asset register, decision register, workstream
register, page plan, and QA ledger. Never overwrite client originals during
diagnosis.

Use `scripts/register_local_assets.py` to populate the asset ledger. By default
it copies each file into `01_SOURCE_OF_TRUTH`, records SHA-256 for original and
protected copy, and verifies the hashes match. Use `--snapshot-mode none` only
when a protected snapshot already exists and its path/hash will be recorded by
another controlled process. Assign authority conservatively; file presence does
not make an asset an approved standard.

### 1. Existing-System Audit

Inventory authoritative files, editability, logo versions, colors, fonts,
imagery, graphic devices, character/IP, applications, and known approvals.

Classify every rule:

- `OFFICIAL_SOURCE`
- `MEASURED_EVIDENCE`
- `WORKING_PROPOSAL`
- `APPROVAL_REQUIRED`
- `APPROVED_STANDARD`
- `DEFERRED`
- `SUPERSEDED`

For Illustrator sources, run `scripts/illustrator_identity_audit.jsx` on the
active document. Treat measurements as evidence, not a fictional construction
story.

### 2. Minimum Brand-System Completion

Create a gap map across strategy, logo governance, color, typography, grid,
image language, graphic signals, wordmark behavior, character/IP, materials,
applications, motion, accessibility, and production.

Develop only what the manual and priority applications require. Photography,
motion, campaign, character bible, or full packaging systems may be deferred
when outside scope.

Do not call proposals official until the named approver records a decision.

### 3. Content Architecture and Relationships

Build the content sequence before choosing page compositions. Reuse the existing
project sources and decisions. Establish the book's opening, chapter transitions,
evidence sequence, and closing; an assortment or product card is not automatically
a conclusion.

For each spread identify one reader takeaway, its supported source, its primary
visual, and the relationship to the preceding and following spread. Related sources
may need separate pages or an explanatory bridge rather than a forced pairing.
Retain the minimum words needed for orientation and connection; image-led does
not mean context-free.

Include only relevant modules:

- source authority and status in the appropriate working or technical location;
- brand premise and recognition;
- master identity and lockups;
- clear space, minimum size, color, and misuse;
- typography and information hierarchy;
- grid and layout behavior;
- image language and evolving creative or character worlds;
- priority packaging, digital, retail, spatial, or campaign applications;
- production specifications when available;
- a closing that makes the system's use and continuation legible.

Verify official usage before granting a work an official chapter or caption.
A proposal bearing an event name is not proof that it was used for that event.
Remove contradicted claims and affected layouts immediately.

Assign each spread a purpose, source assets, rule status, density, and material
risk. Keep these working fields outside the audience-facing page unless needed.
Freeze the current sample's content before intensive pagination; do not require
an entire book freeze before producing the first inspectable proof.

### 4. Editorial Direction on Real Content

Translate the actual content sequence and brand needs into an editorial system.
Do not select a template, palette, or typography and then fill it with assets.

Establish margins, columns, baseline relationships, type roles, caption spacing,
and navigation on the current real content. Choose one visual focal event per
spread; make supporting type and imagery deliberate in scale and placement.
Chinese and Latin type must be tested as complete strings with optical alignment,
line breaks, weight, and space around them. A short heading is still a composition.
In a bilingual book, preserve necessary introductions and explanatory bridges in
each language's intended reading role. Give English meaningful content and a
compositional counterweight when the brief supports it; tiny navigation labels
alone do not constitute bilingual design.

When direction is unresolved or rejected, compare two genuinely different
compositions on representative real content before repeating the system. A useful
sample may contain a cover, an identity/rule spread, a chapter bridge, and a product
or creative-world spread. Do not increase page count to simulate completeness.
Select a direction at `GATE A - MANUAL STYLE APPROVAL`; previous acceptance of one
visual dimension does not approve the content architecture or entire identity.

When style is already approved, localization is the task, or the engagement is
a narrow repair/update, skip territory generation. Audit one representative
sample and mark Gate A `NOT_APPLICABLE` or verify the existing approval.

Read [style-adaptation.md](references/style-adaptation.md).

### 5. Template and Production

Select the editable backend from the required deliverables and the team's real
working environment. Use InDesign/Illustrator, Figma, PPTX, DOCX, HTML, Affinity,
or another suitable source; do not convert every manual into an Adobe project.

When using a supplied InDesign template, audit it before adapting it. Decide:

- `REUSE`: structure already fits the brand.
- `HYBRID`: retain useful masters or rhythm; rebuild style and content frames.
- `REBUILD`: template conflicts with the brand or production requirements.

Do not bundle or redistribute a user-supplied template unless rights permit it.
Do not force a fixed page count, US Letter size, fashion-magazine style, font,
palette, or Adobe version.

For Adobe production, run:

- `scripts/indesign_template_audit.jsx` before adaptation.
- A project-specific `build_[brand]_manual.jsx` for deterministic content and
  image placement when repetition justifies automation.
- `scripts/indesign_preflight_report.jsx` after each meaningful build.

Keep Adobe ExtendScript project-specific where frame IDs, page counts, fonts,
or asset paths vary. Use AppleScript only as a thin launcher. For other
backends, apply equivalent source, export, and preflight checks.

Read [adobe-production.md](references/adobe-production.md).

### 6. Visual QA and Release

Automated preflight is necessary but insufficient. Export the actual deliverable,
render every page, and inspect every spread at normal viewing scale. Use a contact
sheet for sequence and repetition, not as a substitute for page-level inspection.
Inspect hero photographs at 100% for edges, joins, artwork, texture, and lighting.
Background removal alone cannot qualify a twisted, collapsed, shredded, or poorly
lit product photograph as a hero. Repair the photographed presentation faithfully,
use a better supplied view, or defer that application; do not hide it with layout.

Inspect:

- cover and contents;
- densest rule page;
- smallest bilingual type;
- full-bleed and dark pages;
- logo clear space and crops;
- status labels and approval language;
- image quality and legal provenance;
- page rhythm and blank-page intent.

Use:

```bash
"$PY" scripts/render_manual_review.py \
  --pdf "/path/to/manual.pdf" \
  --output "/path/to/review"

"$PY" scripts/build_release_manifest.py \
  --root "/path/to/project" \
  --status "CLIENT_REVIEW"

"$PY" scripts/validate_brand_manual_project.py \
  --root "/path/to/project" \
  --release
```

Build the manifest only after the release payload is frozen; any later file
change must invalidate validation until the manifest is rebuilt. Release
validation requires all configured output formats, complete control ledgers,
resolved gate summaries, approval/QA rows, and matching SHA-256 records.

Read [qa-and-release.md](references/qa-and-release.md).

## Approval Gates

- `GATE 0 - SOURCE AUTHORITY`: masters and decision owners confirmed.
- `GATE 1 - BRAND SYSTEM`: required for new identity, refresh, and governance
  work; `NOT_APPLICABLE` for a true manual-only engagement.
- `GATE A - MANUAL STYLE`: one editorial territory approved.
- `GATE B - CONTENT FREEZE`: page plan, wording, and source assets approved.
- `GATE C - RELEASE`: automated preflight, visual QA, production checks, and
  approval record complete.

Mark Gate A `NOT_APPLICABLE` when an existing manual style is fixed and the task
is repair, migration, or localization.

An internal working manual may proceed before brand-system freeze only when
every unresolved rule is visibly labeled. It must not masquerade as an official
guideline.

## Required Deliverables

Keep the package proportional to scope:

```text
00_PROJECT_CONTROL
01_SOURCE_OF_TRUTH
02_SOURCE_AUDIT
03_BRAND_SYSTEM
04_STYLE_TERRITORIES
05_CONTENT_ARCHITECTURE
06_WORKING_SOURCE
07_REVIEW_EXPORTS
08_RELEASE_PACKAGE
99_SUPERSEDED
```

Release editable source, IDML when relevant, review/print PDF, linked assets or
package, font/license notes, decision register, QA report, and a clear status.
Add DESIGN.md/tokens, a case-publishing proof pack, or a separate review deck only
when each is explicitly scoped and linked to approved manual rules.

## Hard Rules

- Never use one template style for every brand.
- Never let a beautiful layout hide unresolved identity decisions.
- Never reconstruct an approved logo without redesign authorization.
- Never treat detected color values or source groups as approved standards.
- Never mix several style territories before selecting a direction.
- Never release with overset text, bad links, missing fonts, accidental blank
  pages, missing-glyph/tofu boxes, unintended title hyphenation, hidden status
  ambiguity, or unverified asset rights.
- Never use automated font shrinking as the final cure for overset. Treat it as
  a build warning, then correct the copy, frame, style, or page architecture.
- Never run all companion skills by default or create parallel research,
  moodboard, asset, or approval ledgers; route only a true trigger and reuse the
  returned path or ID.
- Never claim any production backend succeeded until the real editable file
  opens, saves, exports, and passes the appropriate preflight.
- Use creative-software MCPs only for a real connected application/backend;
  do not move judgment, gates, or project records into an MCP merely to store
  this workflow. A DAM, approval database, or cloud template service may justify
  a persistent external MCP when the project actually uses it.
