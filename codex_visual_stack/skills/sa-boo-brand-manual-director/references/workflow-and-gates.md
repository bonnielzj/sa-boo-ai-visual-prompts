# Workflow and Gates

## Decision Tree

### Existing governance

Use when the brand treats current artwork as fixed.

`source authority -> native-file audit -> measured evidence -> asset hierarchy
-> proposed governance -> production tests -> approval -> manual`

Do not redraw or improve the mark during governance.

### Brand refresh

Use when fixed assets exist but the surrounding language is incomplete.

`audit -> minimum strategy -> system gap map -> controlled visual territories
-> brand-system approval -> content relationships -> real-content editorial proofs
-> selected manual direction -> production`

Keep brand direction approval separate from manual editorial approval.

### New identity

Use when a new master is authorized.

`strategy -> identity territories -> selected master -> source freeze ->
governance -> applications -> manual`

Trademark and legal clearance remain separate professional responsibilities.

### Manual only

Use when identity rules are approved and the job is formatting, editing,
localization, extension, repair, or migration.

If an unresolved system gap appears, log it and request a scope decision. Do not
quietly redesign it inside the manual.

Mark the brand-system gate `NOT_APPLICABLE`. Run the manual-style gate only when
the editorial direction is open; skip it for fixed-style repair, migration, or
localization.

## Stage Outputs

### Stage 0 - Control

- project config;
- source and asset registers;
- decision register;
- companion workstream register;
- approval owner;
- output specification.

### Stage 1 - Audit

- source authority map;
- editability and provenance report;
- fixed/develop/verify/defer map;
- brand-system gap register;
- visual evidence index.

### Stage 2 - Brand System

- minimum strategy;
- master identity governance;
- color and typography architecture;
- grid and layout grammar;
- imagery and graphic rules where required;
- application proofs;
- unresolved decision list.

### Stage 3 - Content Relationships

- compact content sequence with opening, chapter bridges, and ending;
- each spread's reader takeaway, primary visual, and supported relationship;
- necessary bilingual copy and source-to-page mapping;
- source and rule status in the appropriate working location;
- Gate B content freeze, scaled to the current sample before full production.

### Stage 4 - Editorial Direction

- two equal-content compositions when direction is unresolved or rejected;
- one audited real-content sample when style is fixed;
- full-size spread proofs; contact sheet only when sequence needs review;
- selected typography, margin, alignment, image, and pacing behavior;
- Gate A decision with its exact scope.

### Stage 5 - Production

- audited template or new document;
- working source in the selected backend;
- project-specific build scripts when automation is justified;
- packaged links and fonts where permitted;
- required review, compatibility, and release exports.

### Stage 6 - QA and Release

- automated preflight report;
- rendered pages and contact sheets;
- visual QA note;
- release manifest with complete payload paths, sizes, and verified SHA-256;
- approval log;
- frozen release package.

## Status Integrity

Use one of these statuses on every rule and major visual:

| Status | Meaning |
|---|---|
| `OFFICIAL_SOURCE` | Supplied or explicitly approved master |
| `MEASURED_EVIDENCE` | Factual observation from a source |
| `WORKING_PROPOSAL` | Internal rule under development |
| `APPROVAL_REQUIRED` | Cannot be released as official |
| `APPROVED_STANDARD` | Decision owner, date, and version recorded |
| `DEFERRED` | Intentionally outside current scope |
| `SUPERSEDED` | Retained only for traceability |

Detected values, file presence, and visual similarity do not establish
approval.

## Gate Requirements

### Gate 0 - Source Authority

- authoritative sources named;
- originals protected;
- approver named or `TBD`;
- scope and route recorded.

### Gate 1 - Brand System

- required rules exist;
- proposals are visibly separated;
- brand-side decisions recorded;
- production risks identified.

### Gate A - Manual Style

- equal content used across tests when territories are required;
- selected territory fits brand and users;
- type, image, density, rhythm, and application behavior approved;
- anti-style criteria checked.

Use `NOT_APPLICABLE` when the editorial style is already fixed and the task does
not alter it.

### Gate B - Content Freeze

- page plan complete;
- page ownership and sources known;
- bilingual copy resolved or marked;
- unresolved rules visibly labeled.

### Gate C - Release

- no structural preflight failures;
- visual QA complete;
- exports open correctly;
- rights and licenses recorded;
- version and approval trail complete.
