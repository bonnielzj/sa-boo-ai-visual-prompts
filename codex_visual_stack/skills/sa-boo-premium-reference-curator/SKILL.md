---
name: sa-boo-premium-reference-curator
description: "Use when Bonnie asks to collect, shortlist, compare, or build a reusable set of high-quality visual references. Do not use when she already supplied a clear reference, when one direct visual edit is requested, or merely because a task involves design."
metadata:
  version: 1.3.0
  author: SA&BOO / Hermes
  hermes:
    tags: [visual-reference, curation, moodboard, provenance, aesthetic-qa]
    related_skills: [sa-boo-brand-manual-director, sa-boo-design-research-radar, sa-boo-visual-first-core, sa-boo-visual-reasoning-critic, sa-boo-visual-asset-index]
---

# SA&BOO Premium Reference Curator

## Core promise

Use this as Bonnie's high-quality reference collection and selection workflow when
the task actually needs external sourcing, a shortlist, or a reusable reference
library. It is not a default prerequisite for design execution. Quality remains
more important than padding a requested count with weak material.

Add a companion only when needed:
- `sa-boo-visual-reasoning-critic` for a disputed or explicit visual diagnosis.
- `sa-boo-visual-asset-index` only when the references must persist as a searchable library.
- The relevant domain owner only when the curation is part of a larger design decision.

## Ownership and brand-manual handoff

This skill owns **taste, source quality, decoding, selection, rejection, and
curatorial QA**. It does not own trend currency, the canonical asset schema,
brand approval, page architecture, or release status.

When called by `sa-boo-brand-manual-director`, activate it only for an open
manual-style gate or a named application that needs external precedents.
Consume the brand brief, anti-impressions, current stage, fixed assets, and the
exact design question. Return a compact shortlist manifest containing:

```text
reference_id / asset_id
selected_for
transferable_principle
reject_or_do_not_copy
source_url
rights_status
quality_note
```

Radar may supply dated candidates; the Curator decides visual fitness; the
Asset Index stores accepted records. Reuse one shortlist and one canonical
index rather than rebuilding a second moodboard library inside the manual.

## Project baselines to consult first

Choose references by the current category and design question. Reuse the user's
explicitly designated project library, relevant shortlist, and approval evidence
before starting a new search. A public skill package does not include a private
reference library or establish its approval status.

For props, retail, IP, illustration, merchandise, or graphics, use the applicable
project's sources. Do not transfer one category's visual language or scoped
feedback into a universal taste prescription. A supplied reference and clear
brief do not require another collection or visual chain.

## Aesthetic learning loop

For a substantial new direction, a real visual ambiguity, or meaningful positive
or negative feedback, use
[aesthetic-learning-loop.md](references/aesthetic-learning-loop.md). It treats an
explicitly accepted result as evidence and extracts a scoped, reusable mechanism.
Do not load aesthetic history for a clear local edit or a supplied-reference task;
make the inspectable result first. The loop never requires a new library, moodboard,
or report. Durable accepted methods should update the smallest useful persistent
layer—project record, relevant domain skill, or confirmed cross-project preference—
so comparable work does not restart from zero. An already loaded loop need not be
read again in the same turn.

## Corpus synthesis / 数量积累转化为规律

When Bonnie asks for aesthetic accumulation, or an existing library has gained a
meaningful labeled batch, read
[corpus-pattern-synthesis.md](references/corpus-pattern-synthesis.md). Usually
synthesize after roughly 8–10 new labeled items or in a weekly review; use judgment
when a smaller batch contains decisive feedback. The synthesis replaces that day's
normal poster/research exercise instead of adding a second workload.

Use deterministic measurements from `sa-boo-visual-asset-index` as evidence, then
inspect representative full images and combine them with the catalog's visible
mechanisms and Bonnie's scoped feedback. Produce a small set of candidate mechanisms,
counterexamples, and next experiments. Never promote a color cluster, OCR area,
embedding neighborhood, frequent tag, or majority style into an aesthetic rule by
itself. Frequency shows recurrence, not quality; one accepted result may be more
useful than twenty unlabeled references.

## Runtime and safe-execution preflight

Before running any bundled image/index script on Bonnie's macOS environment:

```bash
HERMES_ROOT="${HERMES_HOME:-$HOME/.hermes}"
PY="$HERMES_ROOT/hermes-agent/venv/bin/python"
if [ ! -x "$PY" ]; then PY="$(command -v python3.11)"; fi
"$PY" -c 'import numpy, PIL'
```

- Do not use bare `/usr/bin/python3` unless the import probe passes. It may resolve to macOS Python 3.9 while `PYTHONPATH` exposes Hermes 3.11 packages, producing NumPy `_multiarray_umath` or Pillow `_imaging` import failures.
- Treat `_scripts/` inside an approved reference library as historical production evidence, not safe reusable entry points. Older collectors can hard-code `BASE`, archive the current library, and clear `images/`, `thumbs/`, or `index/` before rebuilding. Never run them in place; copy and parameterize them inside the new task's independent folder.
- If Google/Bing/Pinterest image surfaces return a challenge or blank page, switch to source-native search (for example Designboom, ArchDaily, a studio, brand, or media archive), extract the direct project URL, then capture that source page. A 403 on one host is a source-level failure, not permission to lower the quality bar.
- The generic Asset Index capture scripts create a staging layout (`originals/`, `thumbs/`, root index files). Do not deliver that staging layout as the final `<主题 参考图>` library. After curatorial acceptance, normalize selected assets into `images/`, `thumbs/`, and `index/`, add explicit `quality_notes`, build a contact sheet, and run `audit_reference_library.py`.

## Domain coverage

Apply this logic across:

- **Product design**: objects, devices, jewelry, accessories, packaging structures, material/form/CMF, product display, technical concept boards.
- **Brand design**: logo/core symbol, visual identity, typography, grid, auxiliary graphics, image style, packaging, campaign/KV, social templates.
- **Spatial design**: retail, pop-up, commercial, residential, office, exhibition, furniture, props, signage, wayfinding, material and lighting references.
- **AI creative production**: prompt references, style systems, generated-image QA, Figma/Canva/deck visual systems.

The standard is transferable: original/stable source → high taste filter → local cache/index → contact-sheet visual QA → design translation.

## Aesthetic filter

Judge quality relative to the brief, audience, medium, and category. High taste
does not mean luxury styling, photorealism, chrome, minimalism, or high finish
in every project. Prioritize:

- category-relevant authored work; for IP/merch this may include character art,
  illustration, comics, publishing, toy sculpture, cultural collections, and
  documented crafts, not just fashion and spatial design;
- high-fashion, luxury, concept-store, boutique, gallery-like, installation-level references when relevant to the brief;
- brand/studio/design-media anchored projects, not anonymous dumps;
- colorful high-saturation, pastel, chrome, mirror, acrylic, glass, metal, soft sculpture, organic/inflated forms, or futuristic retail language only when the current project supports them;
- strong material truth, lighting, proportion, spatial narrative, craft, and clear photographic/readable quality;
- references that can teach a design move: circulation, display hierarchy, prop silhouette, furniture/object form, material combination, lighting, threshold, window, focal node, or brand atmosphere.

Reject:

- low-resolution, blurry, over-compressed, watermarked beyond usefulness, unattributed, or visually weak images;
- generic supplier/e-commerce/factory/wholesale imagery as automatic aesthetic
  direction; separately retain relevant construction, process, price, or material
  evidence without promoting it to a style benchmark;
- stock/mockup/freepik/shutterstock/AI-generated images unless explicitly requested for concept-only analysis;
- generic retail shelves, trade-show booths, supermarket/warehouse/grocery, ordinary restaurants/cafes/offices/residential images unless the brief specifically asks for them;
- runway/showspace/fashion-show images when they do not translate into retail/interior/installation design.

宁缺毋滥。If the count target conflicts with quality, explain and continue sourcing rather than filling with weak assets.

## Reference decoding protocol

Client references are rarely a coherent style brief. Treat the set as a collection of partial signals: one image may represent scale, another interaction, another material, another photographic behavior, and another only an emotional response.

Before moodboarding or designing, decode every important reference with:

```text
reference_id
likely desired point
visual evidence
transferable design principle
project compatibility
elements to reject
original translation opportunity
```

Mandatory interpretation rules:

- State what the client may like about the reference; do not assume they endorse the whole image.
- Distinguish **appearance** from **effect**. "Orange sci-fi shop" is appearance; "immediate distant recognition and a complete IP world" is effect.
- Extract behavioral and commercial requirements first: stopping power, photo composition, dwell time, throughput, participation, product visibility, conversion, and shareability.
- Test each extracted principle against brand identity, audience, site dimensions, circulation, safety, operations, budget, and construction.
- When references conflict, identify the deeper shared demand instead of visually averaging them.
- Translate references into original actions, proportions, systems, materials, and narrative relationships. Do not reproduce recognizable compositions or signature objects.

Forbidden:

- treating all supplied images as one unified aesthetic;
- copying the most visually obvious image because the client sent it;
- combining every liked motif into one design;
- using color or decoration to hide missing spatial and commercial logic;
- presenting imitation as "following the client's preference."

The designer's responsibility is to retain the client's valid intention while improving taste, coherence, originality, feasibility, and commercial performance.

## Live retail-project boundary / 真实零售项目边界

For a live retail or branded-commercial project, consult
`sa-boo-retail-design-partner` before building a moodboard or proposing a visual
territory. Select references by the current design question, not visual
similarity alone, and include both supporting and contrasting cases when the
comparison affects project judgment.

Separate two different collections:

1. **Aesthetic reference / 审美参考**  
   Apply the premium taste filter and reject weak visual precedents.
2. **Operating evidence / 运营依据**  
   Ordinary stores, planograms, stockrooms, service counters, queues, supplier
   diagrams, or maintenance details may be valid when they prove a specific
   behavior, capacity, construction, or operating question. Do not present
   them as aesthetic direction.

Generated imagery and staged photography remain references or hypotheses; they
are not proof of conversion, staffing, replenishment, or post-opening success.

## Source hierarchy

1. **P0 final-cache sources** — official brand/project pages, studio pages, design media, architecture/interior media, project galleries.
2. **P1 high-quality discovery/final sources** — Behance project pages with clear authorship and project depth.
3. **P2 discovery-only sources** — Pinterest, Instagram, 公众号, DINZD/Designwire mirrors, social collections. Use them to discover project names and source leads; final cached assets should prefer the original/stable source when possible.

Strong anchors include: Jacquemus, Miu Miu, Prada, Loewe, Bottega Veneta, Balenciaga, Gentle Monster, Glossier, SKIMS, Fenty, Mugler, Aesop, Burberry, Nike/Jacquemus, Louis Vuitton, Dior, Dover Street Market, Crosby Studios, Random Studio, Snarkitecture, OMA/AMO, Masquespacio, India Mahdavi, Yinka Ilori, Frame, Superfuture, Dezeen, Designboom, Retail Design Blog, Yellowtrace, Wallpaper, gooood, ArchDaily, Design Milk, The Spaces.

## Collection workflow

1. **Inspect the user's sample folder**
   - Build/open a contact sheet if needed.
   - Name the aesthetic in concrete terms before searching.

2. **Create the output folder**
   - Follow `<主题 参考图>` naming.
   - Keep a generated subfolder for the new collection when the parent contains user samples.

3. **Gather candidates broadly, finalize narrowly**
   - Search across the requested platforms and source anchors.
   - Use social/Pinterest only as leads when quality or attribution is weak.
   - Prefer original project pages and high-resolution image URLs.
   - Apply source-level early stop: after repeated empty, blocked, generic, or rejected results, record the failure and move to another verified source instead of looping.
   - Interleave/round-robin source pools before global scoring so an early target count cannot fill from the first source and create false diversity.
   - Treat any per-project image cap as a hard release gate; add more source projects rather than silently raising the cap.
   - Persist manual rejection decisions by normalized original-image URL and verify the final selected set has zero overlap with the cumulative reject list.
   - If automated fallback repeatedly proposes generic interiors or weak matches, stop automation, replace from verified project pages, then rerun image-level QA and contact-sheet review.
   - Serialize and validate a usable first batch to the requested target early; do not spend the full tool/delegation budget browsing and leave the promised file unwritten. Delegated workers should return small verified artifacts, not only long transcripts or `/tmp` evidence.

4. **Hand the accepted shortlist to the canonical index**
   - Use `sa-boo-visual-asset-index` and its schema/scripts for cache, metadata,
     hashes, thumbnails, chains, and retrieval.
   - Do not create a parallel asset schema inside this skill or downstream
     projects. The Curator adds selection/rejection and translation notes to the
     canonical records.

   For an existing collection that needs pattern learning rather than more sourcing,
   keep the current library and run the Asset Index corpus measurement route. Do not
   collect another batch until synthesis identifies a real coverage gap.

5. **Generate and inspect visual QA artifacts**
   - Build total and paginated contact sheets with the Curator or Asset Index
     scripts, then open the overview before finalizing.
   - Visually reject weak, 土, ordinary, repetitive, legally unsafe, or
     irrelevant clusters. Replace them rather than padding the count.

6. **Promote an approved baseline only after Bonnie approves it**
   - Capture scoped project feedback through the aesthetic learning loop. Do not
     infer a global taste rule from project approval, rejection, or silence.
   - Update the user-designated long-term reference standard only when the user
     explicitly authorizes that cross-project change.
   - Preserve useful collection scripts in `_scripts/`; do not treat temporary
     project progress as durable memory.

## Downstream design integration

When the work is not just collecting images but designing in any field:

- Consult approved local collections or build a new curated visual chain only when
  missing precedent would materially change the proposal.
- Pass client references through the reference decoding protocol before using them as design evidence.
- Translate references into design actions: product form, CMF/material, construction, logo/symbol logic, typography/grid, packaging structure, KV composition, spatial proportion, lighting, display hierarchy, circulation, CAD/SU/Figma component strategy, render prompt, or proposal story.
- Never copy a reference blindly. Use it as private study memory and cite rights as `reference-only` unless licensed.
- For future design MCPs, require tools to pass through local visual asset fields instead of vague prompts: asset IDs, thumbnails, source URLs, tags, quality notes, and rights status.

## Output pattern

```text
视觉资产库：folder path
已完成数量：N images / N thumbs / N indexed rows
总览图：absolute path
索引：visual_assets.jsonl + sources.csv
审美判断：why it matches / what was rejected
版权：reference-only, private study/internal reference
下一步：how to use this library in design work
```

For long collections, give progress updates only when quality direction changes, a source fails, or visual QA reveals a problem.

## Optional reference

Read `references/baseline-source-map.md` when you need the longer baseline/source/rejection checklist or a reminder of the accepted 2026 retail/pop-up and props collections.
