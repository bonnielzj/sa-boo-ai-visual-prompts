# Editable Master Layer Contract

Read this before assembling a poster/KV in Figma or another editable production
surface, and before handing the master to another designer or vendor.

## Principle

Separate what must remain exact and editable from what may be raster or generated.
The editable file is a production contract, not a stack of unnamed visual remnants.

## Minimum layer architecture

Use the production surface's native grouping model, but preserve these roles:

```text
00_GUIDES_NOT_EXPORTING
  format / bleed / crop / platform-safe / semantic-safe
01_BACKGROUND_FIELD
  base color / photo / spatial field
02_HERO_ART
  approved raster or vector hero / masks / image treatment
03_STRUCTURAL_GRAPHICS
  court lines / paths / frames / approved VI devices
04_HEADLINE_LIVE
  Chinese core / English echo / controlled effects
05_INFORMATION_LIVE
  date / time / course / venue / CTA / legal
06_IDENTITY_VERIFIED
  wordmark / crest / approved variants / clear-space guide
07_SURFACE_TREATMENT
  grain / halftone / overprint / glow / distress with masks and opacity
08_PRODUCTION_NOTES_NOT_EXPORTING
  fonts / color / asset IDs / linked files / approval / export notes
```

Naming may adapt to the tool, but role separation may not collapse.

## Live and exact

Keep these editable whenever the tool supports it:

- all Chinese and English copy;
- date, time, price, age group, venue, contact, legal, and CTA information;
- verified logo and crest as linked or placed official assets;
- rules, masks, color fields, and crop boundaries;
- format-specific safe zones and production guides.

Do not rely on image generation for exact typography, logo, dates, numbers, or legal
copy. If a generated image contains placeholder text or mark-like forms, remove or
cover them before assembly.

## Hero-art integrity

For raster or generated hero art, record:

```text
source path or asset ID
approval status and selected preview
original dimensions and color profile when known
crop and focal-point contract
generation/edit parameters when relevant
allowed edits and prohibited changes
```

Keep the selected standard-resolution proof until the user approves any 2K/4K
upgrade. Do not replace it silently with a regenerated lookalike.

## Typography contract

Record family, style/weight, source or local file, licensing status, fallback, and any
intentional outline conversion. Keep a live-text version before converting type to
paths. Verify Chinese glyphs and punctuation after handoff or tool substitution.

Do not download or distribute fonts whose license or source cannot be verified.

## Color and effects

- Record named color roles, not just sampled hex values.
- Keep field, counterforce, neutral, and signal colors separately editable.
- Use non-destructive masks and effect controls when practical.
- Keep surface treatments separate from text and identity.
- Prevent a global texture from contaminating small copy or logo edges unless the
  approved medium explicitly requires it.

## Master and variants

Maintain one clearly named master and one frame/artboard per requested adaptation.
Use shared components/styles only when they preserve the dominant event. Do not turn
the poster into a generic component library before the creative is approved.

## Handoff manifest

Return:

```yaml
master_file: ...
master_frame: ...
approval_status: ...
formats:
  - name: ...
    dimensions: ...
    export: ...
fonts:
  - role: ...
    family_style: ...
    source_or_file: ...
    license_status: ...
assets:
  - role: ...
    path_or_id: ...
    approval_status: ...
color_roles: ...
linked_or_missing: ...
outstanding_risks: ...
```

## File QA

Before handoff, verify:

- no missing fonts, broken links, hidden placeholder text, or duplicate logos;
- no exporting guides or annotation layers;
- exact copy matches the approved source;
- artboards have correct dimensions and no unintended overflow;
- transparency, masks, effects, and image crops render as expected;
- exports use the named profile, size, and format;
- the editable source and rendered proof show the same composition.
