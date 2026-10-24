---
name: sa-boo-presentation-director
description: Use for authoring or substantially redesigning an SA&BOO presentation/PPTX. Do not use for a one-line copy edit, one local slide correction, or final-delivery QA alone.
license: Private
metadata:
  hermes:
    tags: [presentation, pptx, deck-direction, slide-system]
    related_skills: [Presentations, ppt-super-workflow, presentation-delivery-qa, visual-board-to-slide-reframing]
---

# SA&BOO Presentation Director

Use this skill as the single routing and quality-control entry point for
presentation work. It directs the existing narrative, visual, authoring, and
QA skills; it does not replace them.

## Hard Rules

- Route every request to `quick preview`, `standard delivery`, or
  `deep editable rebuild` before authoring.
- Route by intended use, not verbs such as 'organize'. A portfolio intended
  for clients, partners, acquisition, or external circulation needs standard
  delivery unless the user explicitly asks only for a draft.
- Use named and supplied sources first. Recall prior work only to resolve a real
  ambiguity or preserve a specifically approved element. Research missing material
  when it is necessary to support the requested commercial story; do not invent
  evidence or expand into unrelated strategy.
- For a source over 250 MB, references over 100 pages, or output over 25
  slides, create a reduced working set and early draft before deeper work.
- For a full deck, plan its narrative and layout sequence before building it.
  For a quick preview, plan only the current sample before showing it.
- Derive each layout from the slide's rhetorical job. Layout archetypes are
  fallbacks, not a menu to fill mechanically.
- Run structural QA and visual QA. Passing overlap checks does not prove a
  slide is well designed.
- Deliver after the content and design meet the user's stated standard.
  Technical validity alone is not usability. A rejected design system requires
  a new representative proof, not repeated cosmetic revision of that system.

## 1. Route The Request

### Quick preview

Use for first-round thinking, rapid organization, or user review.

- Use only supplied sources.
- Sample representative pages or assets.
- Produce the smallest useful proof: slide plan, 3-6 slide draft, contact
  sheet, PDF, or PPTX.
- One build route and one targeted QA pass.
- Do not build indexes, ledgers, or exhaustive template maps unless required.

### Standard delivery

Use for a normal client-ready deck.

- Establish content, source evidence, typography, and the sequence together.
- Test representative pages before repeating the system across the deck.
- Review rendered pages against the actual references and stated use; fix
  material design defects before release. Avoid redundant checks after fixes pass.
- Reuse existing renders, template maps, and extracted assets.

### Deep editable rebuild

Use only when the user explicitly requests exact native editability, full
template reconstruction, exhaustive source review, or pixel-level matching.

- State the larger scope before execution.
- Preserve element ownership, editable structure, masters, and source
  traceability.
- Validate source-to-output fidelity and document remaining differences.

## 2. Define The Deck Contract

Before layout or tool selection, use the brief to establish the relevant contract.
Keep a quick preview's contract lightweight; do not turn supplied information into
a new questionnaire:

```text
Audience:
Decision or action the deck must produce:
One-sentence thesis:
Mode:
Output format:
Editability requirement:
Source/template authority:
Slide-count target:
Language:
```

For branding work, do not treat a direction board as a complete visual
identity. For retail or interior projects, do not let polished slides approve
unsupported design decisions.

## 3. Build The Narrative Spine

Read `references/proposal-deck-mode.md` when the deck needs proposal strategy,
client-facing narrative, recommendation logic, or slide copy.

For the slides being authored, define:

- `message`: the conclusion the audience should retain;
- `purpose`: introduce, diagnose, prove, compare, recommend, transition, or
  close;
- `evidence`: the source, image, diagram, plan, render, table, or metric that
  earns the slide;
- `speaker action`: what the presenter should explain or ask next.

For proposals, use supported conclusions when the page makes an argument.
For a case archive, concise descriptive bilingual titles can identify the
project, product or service directly. Do not turn every image page into a slogan.

## 4. Plan The Layout Sequence

Read `references/layout-and-qa.md` before creating a new deck, redesigning a
deck, or diagnosing weak layout.

For a premium portfolio, magazine-style case book, or feedback about typography,
hierarchy, rhythm, or shallow reference interpretation, also read
`references/editorial-direction.md`. Inspect the actual supplied reference images
before choosing fonts, crops, or page proportions; inspect earlier visual work
only when needed to resolve a gap or preserve an approved element.

For a quick preview, brief layout notes for the current sample are sufficient;
a complete deck JSON and plan checker are not prerequisites to the first proof.
Use a structured layout contract when it helps full-deck authoring or a material
layout risk requires it:

```json
{
  "number": 1,
  "title": "A decisive audience-facing title",
  "message": "The one conclusion this slide must land",
  "purpose": "prove",
  "silhouette": "image-led-asymmetric",
  "density": "open",
  "background": "light",
  "primary_asset": "asset-id-or-path",
  "body_words": 38,
  "source": "user file or URL"
}
```

When using a structured slide plan, run:

```bash
python3 scripts/check_slide_plan.py slide-plan.json --out slide-plan-check.json
```

Resolve relevant errors before authoring those slides. Treat warnings as
design-review prompts, not automatic failures.

Deck rhythm requirements:

- Do not repeat the same silhouette for more than two consecutive slides.
- Alternate dense evidence slides with open emphasis or transition slides.
- Keep recognizable editorial constants such as type roles, margins, alignment,
  and navigation. Use a recurring graphic only when the content and brand justify
  it; artist works and creative worlds may retain their own visual language.
- Let evidence determine proportions. Full-bleed, near-full-page, detail crops,
  paired images, and dense specimen pages have different jobs; no fixed split
  or sidebar is the default visual identity.
- Do not box every content item. Use containers only when grouping has meaning.
- Use one primary idea per slide. Split content before shrinking type.
- Do not reuse the same non-background image across multiple slides by default.

For repeated page types, create one representative prototype first. In quick
preview mode, show the prototype or a small deck sample before replication.

Concise copy must still establish why the audience is seeing a chapter, how related
assets connect, and what the ending means. A title is not a substitute for a bridge.
Choose the visual focal point, typographic treatment, and spacing before building
text boxes. Test complete Chinese and Latin strings and the full composition;
scattered short labels or a mathematically valid grid do not establish editorial
craft. Preserve essential context while removing repetition and decorative copy.

When typography alternatives are requested or a deck's font choice is genuinely
unresolved, use the shared
[font comparison method](../sa-boo-poster-graphic-design-director/references/font-pairing-comparison.md)
on representative slides before deck-wide replacement. Keep approved template
typography fixed unless its revision is in scope. This does not change the deck's
authoring route or require a Figma file, specimen board, or additional approval
step for an already authorized change.

## 5. Select One Authoring Route

Read `references/tool-and-mcp-routing.md` when choosing tools or evaluating an
MCP installation.

Use exactly one primary route per deck:

1. **Local PPTX, editable, or template-led**:
   use the current `Presentations` skill and its editable PPTX/template workflow.
2. **Figma-first visual design or iterative brand review**:
   load `bonnie-creative-backend-routing` and follow its Figma native-backend reserve; use Figma Slides only after that reserve's live-backend gate passes and Bonnie accepts Figma Slides as the working surface.
3. **Image-first cinematic deck**:
   use `ppt-super-workflow` only when visual impact is explicitly more
   important than native editability, or after the user selects that route.
4. **Live open PowerPoint editing**:
   use current document-control tooling only when a real presentation session
   is listed, supported commands are known, and exact live object editing is valuable.
5. **Keynote-native work**:
   use a verified iWork/Keynote MCP only when Keynote is the intended working
   surface or PowerPoint is not required as the source of truth.

Do not switch authoring engines after a usable result exists. One failed route
may use one fallback while reusing completed artifacts.

## 6. Visual Asset Rule

For image-led design work:

- use `sa-boo-visual-first-core`;
- use `sa-boo-visual-asset-index` when assets need provenance or reuse;
- use project-owned images first;
- reject blurry, generic, irrelevant, or unattributed reference imagery;
- treat generated slide images as reference-only unless rights and source
  status are clear.

Follow the project image routing rules for all image generation and editing.

## 7. Quality Gates

For a quick preview, apply one targeted check to the current sample. For a revision,
check the changed slides and any directly affected sequence. Use the full gates for
a full deck; reuse valid renders and checks rather than repeating them at release.

### Structural gate

Check:

- slide bounds;
- unintended overlaps;
- text clipping and unexpected wrapping;
- unused placeholders;
- incorrect aspect ratio;
- missing fonts or substituted fonts;
- image resolution and crop;
- chart/table values;
- source and citation traceability.

### Visual gate

Render the deck and review representative slides at full size. Check:

- hierarchy is obvious within three seconds;
- alignment and spacing create intentional groups;
- text and image carry complementary roles;
- contrast is adequate;
- the deck has layout variety without stylistic conflict;
- dense slides are followed by breathing room;
- the recurring motif is present but not repetitive;
- no slide looks like a dashboard or card grid unless the content requires it;
- the final sequence feels like one authored story.

### Narrative gate

Check:

- the deck has one thesis;
- every slide moves one audience decision;
- transitions are logical;
- recommendations are visible;
- evidence supports claims;
- the final next step is explicit.

## 8. Completion Standard

For a client-ready or final release, load `presentation-delivery-qa`. Do not load
it for a source-only draft, early preview, representative pages, or an ordinary
revision; use one targeted internal check instead.

Deliver the usable deck or preview first. Report:

- selected mode and authoring route;
- final file or review link;
- blocking limitations, if any;
- the small number of decisions still requiring user approval.

Do not attach scratch files or long process logs unless the user asks.
