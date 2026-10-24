# Source Authority and Brand Role Contract

Read this when the poster uses an existing identity, supplied brand assets, generated
references, mixed approval states, or a project-specific visual atlas.

## Authority classes

Classify inputs before design:

| Class | Meaning | Permitted use |
|---|---|---|
| `OFFICIAL_MASTER` | verified logo, wordmark, crest, color, or type rule | use without reconstructing; preserve variants and constraints |
| `APPROVED_CAMPAIGN_RULE` | selected territory, slogan, visual anchor, hierarchy | develop craft within it; do not reopen silently |
| `APPROVED_APPLICATION` | accepted prior proof for one use | evidence of preference, not automatically a universal rule |
| `USER_REFERENCE` | image supplied for attraction, mood, or mechanism | decode and translate; do not imitate recognizable expression |
| `EXTERNAL_PRECEDENT` | traceable cultural or design reference | study with source and rights fields; not a production asset by default |
| `GENERATED_HYPOTHESIS` | exploratory image or variation | composition/mood evidence only; not factual or identity authority |
| `WORKING_PROPOSAL` | current study | keep visibly unapproved |
| `DEFERRED` | intentionally outside current scope | do not solve or imply approval |
| `REJECTED` | explicitly failed candidate | retain only when needed for audit; never use as the next master |

File existence, placement in Figma, render quality, or similarity to an approved
piece does not promote an asset's authority.

## Brand roles inside a poster

An existing identity normally contributes several different roles. Do not give all
of them equal size.

| Role | Typical behavior |
|---|---|
| primary identifier | one dominant verified wordmark or core mark when recognition is required |
| certification | compact crest, registration line, season, club detail, or legal signature |
| structural VI | approved color roles, type family, court/line/orbit/shape language |
| campaign variable | headline behavior, image treatment, surface, crop, tempo |
| information | date, venue, group, course, call to action, legal copy |

Use one dominant mark per canvas unless an approved application explicitly requires
another system. A crest should not compete with the wordmark, and a logo should not
be converted into a contrast patch.

## No logo reconstruction or patching

- Use the verified transparent or vector master.
- Do not redraw, autocomplete, “improve,” or regenerate the logo inside hero art.
- Do not place the logo in a white card, outlined box, floating capsule, badge, or
  framed corner merely to obtain contrast.
- Solve integration through the underlying field, local value control, placement,
  negative space, masking allowed by the VI, or an approved reverse variant.
- Keep minimum size, clear space, and color variants traceable to the brand owner.

When the official mark cannot work in the selected composition, change the
composition or return a bounded identity-variant question to `sa-boo-brand-director`.

## Reference rights and traceability

For any external or supplied reference that enters a durable atlas, record when
available:

```text
source URL or local source path
creator / studio / publisher
work title and year
access date
rights status
usage allowed
project role
attraction / effect / mechanism / do-not-copy
```

Private-study, editorial, archive, or generated images are not automatically licensed
for publication. Do not pass reference pixels into final art unless the user owns the
asset or the usage right is verified.

## Project-specific reference libraries

When the active project has an authorized reference library, bind its current
index, rights fields and scoped approval labels. Keep its assets in that project;
this skill does not bundle a client image library or authorize republication.
Inspect the selected sources instead of describing them from memory.

A project's reference selection establishes only its recorded scope. Do not infer
a user-wide taste profile or another brand's identity from it. General research
methods, analytical lenses and production knowledge can transfer; protected
expression and project-specific decisions need their own authority.

## Handoff record

Before craft execution, return or internally bind:

```yaml
brand_owner: sa-boo-brand-director
campaign_owner: sa-boo-campaign-creative-director
selected_territory: ...
official_assets:
  - id_or_path: ...
    role: primary_identifier | certification | structural_vi
campaign_variables:
  - ...
references:
  - id_or_path: ...
    role: attraction | mechanism | mood | material
prohibited:
  - ...
approval_status: working | selected | approved
```

This record prevents a graphic craft decision from silently becoming a new brand or
campaign decision.
