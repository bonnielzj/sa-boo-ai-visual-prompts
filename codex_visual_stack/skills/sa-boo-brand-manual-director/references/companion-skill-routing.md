# Companion Skill Routing

## Purpose

Keep the brand-manual workflow modular without loading every SA&BOO skill or
repeating research, curation, indexing, strategy, and application work. The
Brand Manual Director owns orchestration, rule status, page architecture,
approval gates, and release. Companions return bounded evidence or application
proofs.

## Route by stage

| Manual stage | Default owner | Conditional companion | Trigger |
|---|---|---|---|
| 0 Control | Brand Manual Director | none | establish one project config and ledgers first |
| 1 Source audit | Brand Manual Director | Visual Asset Index | accepted source visuals need canonical records |
| 2 Brand system | Brand Manual Director | Brand Director | a required strategy or identity rule is missing and scope permits development |
| 3 Content/application | Brand Manual Director | Xiaohongshu IP | social/personal-IP is a named priority application |
| 3 Content/application | Brand Manual Director | Co-design Interior Partner | a spatial/interior application needs shared design judgment |
| 3 Content/application | Brand Manual Director | `figma-generate-library` | approved rules need a machine-readable digital token appendix or editable variable library |
| 3 Content/application | Brand Manual Director | Case Publishing | approved rules need publish-ready social/case proofs |
| 3 Content/application | Brand Manual Director | Presentation Director | reviewers explicitly need a separate approval deck |
| 4 Editorial direction | Brand Manual Director | Premium Reference Curator | editorial direction is open or a style comparison needs external precedents |
| 4 Editorial direction | Brand Manual Director | Design Research Radar | the style rationale makes a current market/category/channel claim |
| 5 Production | selected backend | macOS/Adobe or document production skill | a real editable backend has been selected |
| 6 QA/release | Brand Manual Director | production preflight | vendor-ready production requirements exist |

Do not use Radar merely to find attractive images. Do not use the Curator to
prove that a trend is current. Do not use Xiaohongshu IP or Co-design to approve
upstream identity rules. Do not let any companion change a manual gate directly.

## One owner per artifact

| Artifact | Canonical owner |
|---|---|
| current claim and evidence date | Design Research Radar |
| taste shortlist and reject/do-not-copy notes | Premium Reference Curator |
| cached visual metadata, rights, hashes, thumbnails, chains | Visual Asset Index |
| identity proposal and approval request | Brand Director + decision register |
| social/channel application specification | Xiaohongshu IP |
| spatial application proof and exceptions | Co-design Interior Partner |
| machine-readable digital token contract | `figma-generate-library` + decision register |
| publish-ready social/case proof | Case Publishing |
| separate reviewer presentation | Presentation Director |
| page plan, gate state, manual status, release manifest | Brand Manual Director |

Reference canonical IDs and paths. Never paste the same data into a second
parallel register unless the release format requires a frozen export.

## Handoff register

Use `00_PROJECT_CONTROL/workstream_register.csv` for every activated companion:

```text
workstream_id
skill
trigger
stage
input_refs
output_refs
status
gate_dependency
owner
updated_at
notes
```

Allowed status values:

```text
PLANNED / ACTIVE / BLOCKED / COMPLETE / NOT_APPLICABLE / SUPERSEDED
```

- `input_refs` and `output_refs` contain semicolon-separated project-relative
  paths, decision IDs, claim IDs, or asset IDs—not copied payloads.
- A workstream is `COMPLETE` only when its bounded return artifact exists and is
  linked from the register.
- `BLOCKED` must name the missing decision or evidence.
- On release, no routed workstream may remain `PLANNED`, `ACTIVE`, or `BLOCKED`.

## Fast paths

1. **Manual-only + fixed editorial style** — skip Radar, Curator, Xiaohongshu,
   and Co-design unless a named page truly needs one. Audit, edit, preflight,
   render, and release.
2. **Open editorial style without current claims** — use Curator; do not invoke
   Radar merely to decorate the territory rationale.
3. **Current benchmark without visual selection** — use Radar only; remain
   text/evidence led.
4. **Social application module** — wait for usable upstream brand rules, then
   use Xiaohongshu IP once and return the platform proof to the page plan.
5. **Spatial application module** — wait for the relevant brand-system gate,
   then use Co-design for one focused proof; do not launch a full interior
   project unless separately scoped.
6. **Existing valid artifact** — reuse it. Refresh only if authority changed,
   the question changed, the asset failed QA, or a time-sensitive claim is stale.
7. **Digital token appendix** — only after relevant rules are approved; use
   `figma-generate-library`, validate any exported token files, and link every
   token group to decision/page IDs.
8. **Social/case application proof** — use Case Publishing only after upstream
   identity rules are usable; return SVG/PNG/manifest/QA as a bounded proof.
9. **Separate approval deck** — use Presentation Director only when reviewers
   request it; the manual and decision register remain the source of truth.

## Completion check

A companion route is complete when:

- the trigger and stage are recorded;
- inputs refer to authoritative project artifacts;
- one bounded output exists at a stable path or ID;
- rule/claim/asset status and rights are visible where relevant;
- the manual page plan links the output it actually uses;
- no parallel research, moodboard, asset index, or approval register was created.
