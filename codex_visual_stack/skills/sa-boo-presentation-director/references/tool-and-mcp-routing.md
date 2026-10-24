# Tool And MCP Routing

## Contents

1. Current preferred stack
2. Optional routes
3. Research candidates
4. Installation gates
5. Verified local installation

## 1. Current Preferred Stack

### OpenAI Presentations

Use as the default local PPTX route.

Strengths:

- native editable PPTX authoring;
- artifact-tool composition;
- bundled layout library;
- template inspection and inheritance;
- rendering, montage, and overflow checks;
- explicit Google Slides import route.

Limit:

- a layout library and a file engine do not replace deck-level design
  judgment. Apply this director's selected preview/delivery mode. A quick sample
  uses brief layout notes and a targeted visual check; full contracts and a scored
  rubric are not prerequisites to its first proof. Use supplied suitable visual
  assets first; source more only for an actual visual/content gap.

### Narrative Direction

This presentation director owns proposal thesis, client decision logic,
narrative spine and copy; the current Presentations skill executes the PPTX.
Do not search for a retired second proposal-deck owner.

### PPT Super Workflow

Use for explicitly image-first, cinematic, or reconstruction work. It is not
the default for ordinary presentation requests and must obey the selected speed
mode.

## 2. Optional Routes

### Figma Slides plugin

Best optional visual-design route.

Use when:

- brand matching and layout iteration are more important than immediate PPTX;
- the user wants Figma Slides;
- multiple visual reviews are expected;
- auto-layout, theme variables, and collaborative design are useful.

Required gate:

- plugin installed and authorized;
- user accepts Figma as the working surface;
- select Figma or PPTX as the primary route, not both.

Strong patterns to retain even when not using Figma:

- plan the authored sample, or the whole sequence for a full deck;
- choose batch size for the requested count and active tool; a three-page preview is three pages total;
- inspect overlap, clipping and bounds on changed slides;
- reuse valid renders; inspect the first representative proof and directly affected final pages;
- inherit a supplied deck's design language rather than inventing a new one.

### Live PowerPoint Office.js MCP

Best optional final-editing route for a deck already open in PowerPoint.

Use when:

- exact live shape editing, screenshots, OOXML, charts, or template layouts are
  valuable;
- the local PowerPoint version supports the required Office.js APIs;
- the local bridge's security model is acceptable.

Do not use as the first layout-thinking engine. It is an execution and
inspection surface.

### iWork/Keynote MCP

Useful Mac-native route for Keynote-first work, live presentation control, or
export to PDF/PPTX.

Use when:

- Keynote is the intended source of truth;
- the installed Keynote version meets the server requirement;
- conversion to PowerPoint is a handoff, not an expectation of exact PPTX
  fidelity.

### Canva plugin

Use only for fast branded cloud candidates when the account and brand kit are
authorized. It is useful for option generation, not for exact native PowerPoint
control.

## 3. Research Candidates

### PPTAgent / DeepPresenter

Adopt ideas, not the full runtime first.

Useful concepts:

- retrieval and selection of layouts based on content fit;
- reflective generation loop;
- separate content, style, and coherence evaluation;
- benchmarkable slide-generation tasks.

Why not default:

- substantial Docker/model/runtime dependencies;
- overlaps with the existing OpenAI authoring stack;
- likely to create a second end-to-end pipeline.

### SlidesGen-Bench

Use as a benchmark reference.

Useful concepts:

- evaluate content, aesthetics, and editability separately;
- render all outputs to images for cross-tool comparison;
- use contrast, color harmony, colorfulness, and visual-complexity metrics;
- include human preference or pairwise review for final calibration.

Do not install the full benchmark for ordinary decks. Create a smaller local
evaluation fixture first.

### PptxGenJS

Useful reference or fallback library for editable OOXML slides, charts,
tables, SVG, and masters. The OpenAI Presentations skill currently mandates
artifact-tool, so PptxGenJS should not silently replace the primary engine.

### pptx-automizer

Useful only for a future named-template library where existing PowerPoint
slides and individual objects become data-driven templates. It has limitations
around animations, complex layouts, and element-level modification.

### Image-to-editable PPT skills

Keep as explicit deep-rebuild tools only. They are valuable after a visual deck
is approved, but expensive and unnecessary for normal PPT requests.

## 4. Installation Gates

Before adding any MCP or presentation runtime:

1. Confirm it adds a missing capability rather than duplicating artifact-tool.
2. Confirm macOS and local application version compatibility.
3. Check maintenance status, license, open issues, and security posture.
4. Install in a reversible location.
5. Run one real smoke test against a disposable deck.
6. Verify output by opening, rendering, and checking at least one edited slide.
7. Record the verified version and rollback path.

Never claim a presentation MCP works because configuration succeeded. A real
create/read/edit/verify call must succeed.

## 5. Verified Local Installation

Historical status updated on 2026-07-27, with dated later notes. These rows are
discovery hints, not current routing gates or permanent availability:

| Capability | Installed path | Verification |
| --- | --- | --- |
| `Presentations` skill | Current editable PPTX workflow | Installed and enabled |
| Figma plugin | historical authenticated connector | Verified operations on 2026-08-29; reuse current valid account/file context and check only changed or unresolved capabilities |
| Live presentation document control | current session tooling | Optional; use only after a live session and supported commands are read back |
| PPTAgent / DeepPresenter | `~/.local/share/uv/tools/pptagent` | CLI 1.1.37 and MCP entry point start; model/API config intentionally unset |
| SlidesGen-Bench | Migration archive only | Not an active Hermes dependency |
| PptxGenJS | current `Presentations` skill runtime | Use only through the loaded skill and its current dependency checks |
| pptx-automizer | current `Presentations` skill runtime | Use only through the loaded skill and its current dependency checks |

Evidence:

Historical installation evidence is archived. Select the current exposed route;
the actual authorized task call, readback and output inspection provide scoped
execution evidence. A separate probe is needed only for unresolved connection,
account, target, permissions or function. Do not run a fresh Hermes smoke test
for each Codex task or switch runtimes just to reproduce an old proof.

The Figma route is available after the task-specific prerequisite skills and
identity check succeed. Do not describe live presentation document control as
operational until its session performs a real read or edit call.
