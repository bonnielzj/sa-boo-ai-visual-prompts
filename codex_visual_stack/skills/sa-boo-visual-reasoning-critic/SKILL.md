---
name: sa-boo-visual-reasoning-critic
description: Use when analyzing, comparing, or critiquing images, including color tone, grading, filters, lighting direction and quality, shadows, glow, atmospheric effects, reflections, refraction, and other optical treatments.
license: Private
metadata:
  hermes:
    tags: [visual-analysis, visual-reasoning, design-critique, image-comparison, uncertainty]
    related_skills: [sa-boo-visual-first-core, sa-boo-premium-reference-curator, multi-view-visual-consistency, raster-technical-drawing-analysis, bonnie-creative-backend-routing]
---

# SA&BOO Visual Reasoning Critic

## Overview

This is the general front door for **seeing, reasoning about, comparing, and critiquing visual material** across interiors, garments, products, photography, graphics, brands, renderings, moodboards, slides, and generated images.

It corrects a recurring failure: fluent visual prose without a defensible visual model. The required order is:

```text
pixel access
→ direct observations
→ entities and relations
→ intent and reference roles
→ bounded inference
→ design judgment
→ specific action
```

A polished paragraph is not evidence. OCR, color counts, saliency, SSIM, hashes, dimensions, or a generated annotation are not semantic understanding. If the actual pixels cannot be inspected through a verified semantic-vision route, stop at the evidence the available tools can support.

## When to use

Use for:

- “分析这张图 / 看看哪里不对 / 为什么不好看 / 有没有高级感”；
- comparing a reference, current version, approved master, and candidate;
- reading composition, hierarchy, material, construction, proportion, light, color, viewpoint, attachment, or visual artifacts;
- diagnosing tone, color grading, light sources, shadow behavior, atmosphere, glow/halo/bloom, caustics/refraction, dappled light, bokeh, and other optical effects;
- translating short user feedback into visual production constraints;
- checking a generated image before delivery;
- deciding what a reference contributes and what must not be copied;
- resolving disagreement between visual inspection and machine metrics.

Do not use alone for measurable CAD truth, raster construction drawings, reference licensing, garment edit execution, or software mutation. Pair with the domain owner after this analysis gate.

## Absolute authority order

```text
1. the user's explicit correction or circled/marked instruction
2. approved master / approved crop / exact authoritative asset
3. directly inspected current source pixels
4. directly inspected target crop at useful scale
5. domain-specific geometric or document evidence
6. model inference
7. machine metrics and generic conventions
```

A lower level never overrules a higher level. A rejected derivative is not an
approved master or positive evidence, but can remain the source of a specifically
requested repair. User rejection invalidates prior machine PASS status immediately.

## Stage 0 — Bind the question and image roles

State the exact decision in one sentence before analysis. Exclude irrelevant identity or story questions.

For multiple images, assign roles before looking for differences:

| Role | Meaning |
|---|---|
| `SOURCE_GEOMETRY` | authoritative silhouette, construction, angle, or layout |
| `SOURCE_MATERIAL` | authoritative texture, finish, thickness, edge behavior |
| `SOURCE_GRAPHIC` | exact logo, embroidery, print, ornament, or local asset |
| `REFERENCE_MOOD` | atmosphere, lighting, palette, camera, or emotion only |
| `APPROVED_MASTER` | last approved whole-image state |
| `USER_CORRECTION` | highest-priority markup or correction |
| `CANDIDATE` | result being judged |
| `GENERATED_HYPOTHESIS` | exploratory image; never factual proof |

Do not average all references. Approval of one visible feature does not approve a reference's total style, form, material, or composition.

## Stage 1 — Prove pixel access

1. Resolve the actual file or URL.
2. Record dimensions, orientation, crop status, compression/blur, and whether the relevant region is visible.
   - For a supplied GUI screenshot, treat it as static evidence only: quote visible prompt/control text, declare the original-image coordinate frame when bounds matter, and state when the target dialog is absent. Never convert the analysis into automated clicking or Computer Use.
3. Make one real semantic inspection call on the source. The result must mention known visible content grounded in the actual image.
4. If exact detail matters, inspect a target crop at useful scale.
5. Use the Apple Vision probe only for OCR, orientation, face/human counts, coarse classification, dominant colors, or saliency. Never present it as full semantic critique.
6. If semantic inspection is unavailable or contradictory, state which questions remain blocked. Do not guess from file names, common product types, or prior tasks.

A configured provider or successful text response is not proof that the image was understood.

## Stage 2 — Evidence ledger

Every important statement belongs to one class:

| Class | Rule | Example language |
|---|---|---|
| `VISIBLE_FACT` | directly visible in a named region | “画面下部可见三处……” |
| `RELATION` | visible relation between facts | “挂件连接在下摆边缘，而非铺在衣身表面” |
| `SUPPORTED_INFERENCE` | likely, with basis and alternatives | “反光弱且边缘绒毛扩散，较像短绒；不能确认纤维成分” |
| `UNKNOWN` | not shown, occluded, blurred, or too small | “背面未展示，无法确认” |
| `JUDGMENT` | effectiveness relative to stated intent | “多个同权重装饰分散帽型焦点” |
| `ACTION` | minimal change addressing the judgment | “保留三处装饰，降低尺度和对比，不新增重复元素” |

Use this grammar:

```text
[region] + [entity] + [observable property] + [relation] + [visual effect] + [confidence/limit]
```

Replace vague terms such as “高级、梦幻、有设计感、不协调” with visible properties, causal effects, and concrete constraints.

## Stage 3 — Scene graph

For complex images, model before prose:

```yaml
entities:
  - id: object-or-region
    type: component | surface | person | graphic | light | text | background
    region: normalized_bbox_or_named_area
    visible_attributes:
      color: ...
      material_cues: ...
      shape: ...
      scale: ...
      state: ...
    occlusion: none | partial | heavy
relations:
  - subject: ...
    relation: left_of | right_of | above | below | inside | attached_to | overlaps | occludes | repeats | aligned_with | connected_to | separated_from
    object: ...
view:
  angle: front | back | side | top | oblique | unknown
  camera: close | medium | wide | high | low | eye_level | unknown
unknowns: [...]
```

Counts, positions, density, and scale are independent fields. “下摆约 1/3 处” describes location, not permission to fill the area. If quantity is not specified, use the minimum sufficient set and ask only when the decision materially changes.

## Stage 4 — Agentic seeing loop

Do not rely on one global glance:

```text
overview survey
→ list unresolved visual questions
→ crop / zoom / measure relevant regions
→ re-inspect those regions semantically
→ reconcile crops with the whole image
→ stop when the decision is supported
```

Use `scripts/crop_visual_regions.py` for deterministic local crops. Crops answer boundary, count, attachment, OCR, material, or artifact questions but do not replace whole-image composition.

Bound the loop: one overview pass, up to two targeted evidence passes per unresolved decision, one independent comparison method when useful, then return grounded findings and explicit unknowns. Repeating the same vague vision prompt is not deeper reasoning.

### Conflict reconciliation

When overview and crop analyses disagree, do not present both as parallel truths. Build a short reconciliation ledger:

```text
question | overview claim | crop evidence | authority | final status
```

- A useful-scale crop outranks a global glance for the identity, boundary, count, or attachment inside that crop.
- The whole image still controls composition, proportion, and relation to the rest of the scene.
- Downgrade a claim to `UNKNOWN` or `SUPPORTED_INFERENCE` when the crop fails to confirm it.
- Never preserve a stronger overview claim merely because it sounds more complete.
- Return only the reconciled result, not three repeated analysis transcripts.

## Stage 5 — Relevant lenses only

Read `references/visual-language-ontology.md` when vocabulary is weak. Do not mechanically score every lens.

Select criteria for the actual medium, brief, and stage. Type scales, spacing
increments, palette restraint, focal-point counts, and motion timings are design
heuristics, not universal pass/fail rules. Measure a relevant value when evidence
allows it; do not invent exact values from appearance or mistake numerical
conformity for a successful design.

When the image or brief uses tone, filter, lighting, or optical-effect labels, pair with `sa-boo-visual-style-prompt-lab` and read its `references/bilingual-tone-lighting-ontology.md`. Treat that reference as a translation and mechanism guide, not as proof of what is visible in the current pixels.

- **Structure and geometry:** silhouette, massing, proportion, axis, contour, thickness, seams, openings, junctions, attachment, construction order, perspective.
- **Composition and hierarchy:** entry point, reading path, focal competition, figure/ground, grouping, rhythm, density, negative space, cropping, visual weight.
- **Material and craft:** substrate, pile/nap, roughness, sheen, translucency, thickness, drape, compression, edge finish, stitch/appliqué/print behavior, contact shadow.
- **Light and color:** direction, softness, falloff, key/fill/rim separation, haze, temperature, local/global grading, value and saturation hierarchy.
- **Function and behavior:** how a person uses, reaches, wears, enters, sees, moves, rests, buys, or maintains—only with visible geometry or stated use.
- **Narrative and brand:** emotional signal, brief fit, cliché, recognizability, and originality.
- **Artifact and integrity:** duplication, ghosting, double contours, melted seams, floating objects, warped geometry, blur, texture drift, shadow/perspective breaks, boundary halos.

### Tone and lighting diagnosis gate

Do not describe a light effect as a free-floating mood. Resolve it through this order:

```text
global grade
→ source and direction
→ shadow hardness and density
→ atmosphere / participating medium
→ optical effect
→ material response
→ camera/filter
```

For each claim, state whether it is a visible fact, supported inference, or unknown. Check source plausibility, direction consistency, value hierarchy, colored-light spill, surface response, and edge integrity. Require water/glass for caustics, mist/dust/rain for volumetric shafts, an occluder for dappled light, and a physical or optical cause for bokeh. Treat dreamlike, mysterious, premium, and similar adjectives as judgments that must be decomposed into observable light behavior.

## Stage 6 — Causal critique

Each finding must have:

```text
intent
→ located visual evidence
→ perceptual/functional effect
→ verdict
→ smallest effective change
```

Report the few findings that change the next decision, ranked by their effect on
the brief and current stage. Condense each to **located evidence → why it matters
→ specific fix**. Give exact values when measured and useful; otherwise describe
the visual relationship to change. Do not manufacture a number to sound precise.

Severity follows the user's decision:

- `BLOCKER`: wrong identity, count, geometry, reference role, approved asset, or production fact;
- `MAJOR`: damages hierarchy, material credibility, function, brand fit, or cross-view consistency;
- `MINOR`: polish that does not alter the core decision.

Name genuine strengths specifically. Do not manufacture praise or force a sandwich critique.

For a requested critique, identify the highest-impact next change when one is
warranted. A review alone does not authorize edits. When edits are requested,
apply changes within that scope, preserve approved assets and unaffected areas,
and inspect the result. A numerical adjustment is not automatically safe, and an
expressly requested aesthetic change does not need a second confirmation merely
because it involves judgment.

For creative work, distinguish a locally correct relationship from the complete
work's success. Separately judge its actual project purpose, first-glance event,
reading rhythm, emotional or cultural expression, and the specificity of its
image-making. Physical contact, readable copy, or plausible material supports only
that observed dimension. A literal illustration of the title can still be generic.
Judge abstract or typographic studies against their declared visual purpose; do
not impose a story, photograph, logo, or production package on every artwork.

For a requested batch critique or practice-learning review, read
[batch-critique-and-practice-learning.md](references/batch-critique-and-practice-learning.md).
Use it to connect actual versions and scoped feedback to a few actionable method
changes. It is not a prerequisite for an ordinary single-image correction.

## Multi-image and revision reasoning

1. normalize roles and likely view order;
2. identify stable identity anchors;
3. compare entity-by-entity, not image-by-image prose;
4. split differences into requested, collateral, and uncertain;
5. verify count, attachment, scale, material, and boundary separately;
6. use machine metrics only to localize differences;
7. inspect the whole image and relevant crops against the actual brief, keeping
   internal judgment separate from user acceptance;
8. on rejection, bind the user-named source and requested change; return to the
   last approved state when the premise/source was wrong, while preserving a
   selected direction when the user explicitly wants it developed.

Never accept high SSIM or unchanged-pixel scores when the visible object is wrong.

## Reference interpretation

Decode each reference through:

```text
attraction
→ transferable principle
→ project fit
→ rejection / non-transferable elements
→ original translation
```

State authority narrowly. A mood image may authorize lighting but not structure. A logo crop may authorize graphics but not material. A front view cannot prove a back detail.

## Default output

Use concise natural Chinese. Unless the user requests a report, synthesize the resolved result into no more than eight substantive bullets; do not paste the overview and crop analyses back to the user.

Lead with the verdict on the actual brief, then the ranked findings with evidence,
effect, and fix. Include strengths worth preserving, the first useful change, and
material unknowns only when relevant. The evidence ledger, scene graph, and lens
list are reasoning aids, not compulsory report headings. Do not invent defects or
praise to fill a quota; for a local correction, show the result with only a needed
note.

For production, end with:

```text
KEEP       approved facts that must remain
CHANGE     exact target changes
DO NOT     prohibited additions, substitutions, or global drift
VERIFY     full-frame and crop checks before release
```

## Failure firewall

Stop or revise when:

- mood/style appears before object identity and relations;
- location becomes quantity or density;
- a common convention is stated as a fact in this image;
- unseen back/interior/paired items are invented;
- exact materials are named without visual cues or documentation;
- color prose replaces geometry, attachment, scale, and construction;
- all references are treated as equally authoritative;
- machine PASS defends a visually rejected result;
- the fix says only “more premium / cleaner / better composition”;
- uncertainty is hidden in long fluent prose;
- a new third-party vision service receives user images without explicit approval;
- Computer Use, screenshot-driven clicking, or GUI automation is proposed.

## Routing and completion gate

- [ ] actual pixels were semantically inspected or the limitation is stated;
- [ ] image roles and decision question are explicit;
- [ ] visible facts are separated from inference and judgment;
- [ ] count, position, scale, attachment, viewpoint, and material cues are addressed when relevant;
- [ ] unknowns are local and specific;
- [ ] each major critique has evidence, effect, and a concrete fix;
- [ ] user corrections and approved assets outrank automation;
- [ ] whole image and target crops were checked;
- [ ] no external upload or unsafe GUI route was silently introduced;
- [ ] final language is concise enough to guide the next visual action.

Read `references/evidence-and-critique-examples.md` for domain examples, `references/visual-reasoning-benchmarks.md` for regression cases, and `references/source-audit.md` for reviewed external skills and adoption decisions.
