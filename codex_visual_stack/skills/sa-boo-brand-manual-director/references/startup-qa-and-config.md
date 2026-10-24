# Startup Q&A and Project Config

## Purpose

Reduce conversation while preserving the decisions that materially change the
manual. Inspect local files and prior dialogue first. Ask only for information
that cannot be inferred safely.

## Five Questions

### Q1 - Job

Ask:

> Which job are we doing: govern an existing identity, refresh missing brand
> rules, create a new identity, or redesign/edit an already approved manual?

Record:

- brand and project name;
- project root;
- mode: `existing-governance`, `brand-refresh`, `new-identity`, or
  `manual-only`;
- current stage and deadline.

### Q2 - Authority

Ask:

> Which assets or rules are fixed, which may change, and which need brand-side
> approval?

Classify items under:

- `fixed`;
- `develop`;
- `verify`;
- `defer`.

Never assume that files found together have equal authority.

### Q3 - Use and Approval

Ask:

> Who will use and approve the manual, and which real applications must it
> support first?

Record:

- approver and reviewers;
- internal, client, vendor, franchise, partner, or public audience;
- priority applications;
- production constraints.

### Q4 - Style

Ask:

> Give me three qualities the brand should express and two qualities it must
> avoid. References are welcome.

If the answer is vague, offer these adjustable dimensions:

- authority;
- experimentation;
- warmth;
- play;
- information density;
- image dominance;
- tactility;
- motion.

Use a `0-5` value only when it helps comparison. Adjectives remain valid input.

### Q5 - Output

Ask:

> What must we deliver: InDesign, IDML, Illustrator, PDF, packaged links, which
> languages/page size, and should we adapt a supplied template?

Record:

- required formats;
- page format and orientation;
- languages;
- Adobe version compatibility;
- print/digital use;
- template path and rights status.

## Conversation Rules

- Use a zero-question path when files and dialogue answer the five fields.
- Otherwise batch unresolved fields into one compact numbered confirmation.
- Ask one short follow-up only when a single answer remains a true blocker.
- Do not repeat answers already present in files or dialogue.
- Offer a default when the user does not care.
- Permit `start with defaults`.
- Mark uncertain values `TBD / VERIFY`.
- Five is a field cap, not a required five-turn sequence.
- Summarize the resolved brief in no more than 12 lines and start work.

## Project Config Shape

`00_PROJECT_CONTROL/brand_manual_project.json`:

```json
{
  "schema_version": "1.1",
  "brand": "Example Brand",
  "mode": "brand-refresh",
  "status": "INTAKE",
  "languages": ["zh-CN", "en"],
  "outputs": ["indd", "idml", "pdf"],
  "style_direction": "open",
  "template": {
    "path": "",
    "rights_status": "VERIFY",
    "adaptation": "TBD"
  },
  "authority": {
    "fixed": [],
    "develop": [],
    "verify": [],
    "defer": []
  },
  "approver": "TBD",
  "priority_applications": [],
  "style": {
    "qualities": [],
    "avoid": [],
    "variables": {
      "authority": null,
      "experimentation": null,
      "warmth": null,
      "play": null,
      "density": null,
      "image_dominance": null,
      "tactility": null,
      "motion": null
    }
  }
}
```

Keep project-specific content in this config and the project ledgers, not in
the reusable Skill.

Pass known authority decisions into project initialization with `--fixed`,
`--develop`, `--verify`, and `--defer`. Run
`scripts/register_local_assets.py` so the asset register does not remain an
empty template. Its default `--snapshot-mode copy` copies each source into
`01_SOURCE_OF_TRUTH` and records matching original/protected SHA-256 values.
Use `--snapshot-mode none` only when another controlled process already created
and records the protected snapshot.

The asset register includes `source_sha256`, `protected_copy_path`, and
`protected_copy_sha256`. A source changing after registration is a warning; a
missing protected copy or protected-copy hash mismatch is a validation error.

Do not re-run the initializer on a live project casually. Without `--force` it
refuses an initialized root. With `--force` it first copies every control file
and the page plan to a timestamped folder under `99_SUPERSEDED`, then replaces
the templates; verify the reported `control_backup` path before continuing.

The initializer also creates `00_PROJECT_CONTROL/workstream_register.csv`.
Record only companions whose trigger is true, and link their inputs/outputs by
path or ID rather than copying research, moodboard, or asset payloads into a
second ledger. See `companion-skill-routing.md`.
