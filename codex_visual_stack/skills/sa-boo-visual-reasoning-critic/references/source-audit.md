# External Skill Source Audit

Audit date: 2026-07-28. The local skill is an original Hermes/SA&BOO synthesis. External material was reviewed for methods and failure modes; no external runtime, provider, CLI, or credential was installed.

## Adopted as ideas, rewritten for Hermes

### Designers Eye / design critique

- Source: `LeoYeAI/openclaw-master-skills/skills/design-critique/SKILL.md`
- Reviewed commit URL: https://github.com/LeoYeAI/openclaw-master-skills/blob/e5199b56ae1ff72e141586c17695563486c46702/skills/design-critique/SKILL.md
- Repository license: MIT.
- Useful: broad formal lenses (Gestalt, hierarchy, composition, color, typography), located findings, severity and specific fixes.
- Not adopted: UI-first universal formulas such as always requiring one focal point, fixed type ratios, or platform rules for every visual domain.

### Design critique / user-goal prioritization

- Source: `mohitagw15856/pm-claude-skills/skills/design-critique/SKILL.md`
- Reviewed commit URL: https://github.com/mohitagw15856/pm-claude-skills/blob/e4def4c7c9cfcc98e2b21af54169ccfea152fb10/skills/design-critique/SKILL.md
- Repository license: MIT.
- Useful: connect each issue to user goal; include only heuristics visible in scope; genuine strengths rather than manufactured praise; stage-appropriate recommendations.
- Not adopted: mandatory Nielsen/JTBD tables for non-interactive visual work.

### Intentionality and optical review

- Source: `majiayu000/claude-skill-registry/skills/design/design-critique/SKILL.md`
- Reviewed commit URL: https://github.com/majiayu000/claude-skill-registry/blob/ef926663574f5f7a0c19b0429b2540373279ed45/skills/design/design-critique/SKILL.md
- Repository license: MIT; upstream provenance inside this registry was not sufficiently clear for direct installation.
- Useful: interrogate intent, squint/grayscale/near/far review, optical rather than purely mathematical alignment, anti-generic-AI review, extract principles rather than copying references.
- Adoption: paraphrased concepts only; no registry dependency.

### Survey → measure → verify loop

- Source: `majiayu000/claude-skill-registry/skills/design/agentic-vision/SKILL.md`
- Reviewed commit URL: https://github.com/majiayu000/claude-skill-registry/blob/ef926663574f5f7a0c19b0429b2540373279ed45/skills/design/agentic-vision/SKILL.md
- Repository license: MIT; source is service-specific and aggregator provenance is uncertain.
- Useful: Think → Act → Observe; inspect whole image, crop/measure unresolved regions, then verify result.
- Not adopted: Gemini API, code-execution sandbox, claimed pixel-perfect percentages, SSIM verdict thresholds, or external uploads.

### Local pair alignment discipline

- Source: `sergekostenchuk/ui-ux-agent-skill-system/core/skills/image-layer-alignment-validator/SKILL.md`
- Reviewed commit URL: https://github.com/sergekostenchuk/ui-ux-agent-skill-system/blob/ddaedd712a37d7523f0ce99f556abe68ded7a315/core/skills/image-layer-alignment-validator/SKILL.md
- License: Apache-2.0.
- Useful: local-first image processing, normalized measurements, separate primary-subject drift from background changes, accept `inconclusive`, visually override a wrong foreground heuristic.
- Adoption: principles only; existing `multi-view-visual-consistency` remains the execution owner.

### Evaluative critique

- Source: `yamatakeru/art-critique-skills/skills/art-critique/SKILL.md`
- Reviewed commit URL: https://github.com/yamatakeru/art-critique-skills/blob/b5e74516b9110306c45022d06589a10df5d6c03b/skills/art-critique/SKILL.md
- Repository license: MIT.
- Useful: critique should evaluate whether a work achieves its intended purpose, not only classify or describe it; frameworks inform judgment but do not replace it.
- No code or runtime was imported.

## Rejected for direct installation

### `nyldn/claude-octopus` UI skills

- `skills/octopus-ui-ux-design/SKILL.md` hardcodes Codex, Gemini, Claude, provider checks, a separate plugin tree, mandatory BM25 calls, external multi-provider orchestration, and `.claude-octopus` persistence.
- `skills/skill-visual-feedback/SKILL.md` is a UI code-fix workflow, not general semantic image reasoning, and declares a Codex host adaptation.
- Decision: reject. It conflicts with Hermes isolation and the user's no-Computer-Use/no-Codex workflow.

### Gemini Vision skill

- Source reviewed: https://github.com/einverne/dotfiles/blob/f6f8877aaace42352ba2bd21410679463f88bd71/claude/skills/gemini-vision/SKILL.md
- Requires a new Gemini API key and sends user images to a third-party service.
- Decision: not installed. the user's general authorization does not cover new image uploads or credentials.

### Wayland art critic

- Source: `FerroxLabs/wayland/.../art-critic/SKILL.md`.
- Repository reports AGPL-3.0 while the mirrored skill frontmatter reports Apache-2.0; the content is largely art-history education and museum guidance.
- Decision: no copy and no installation. Generic description → analysis → interpretation → judgment logic was independently written from established art-education practice.

### Registry visual-analysis

- `majiayu000/claude-skill-registry/skills/analysis/visual-analysis/SKILL.md` is a shallow prompt template and asks the model to infer exact hex colors, fonts, spacing, and implementation structure without requiring measurement or uncertainty.
- Decision: reject as likely to reinforce confident hallucination.

### Designers Eye as a standalone local front door

- Despite useful formal vocabulary, it is dominated by web/mobile usability and fixed numerical conventions.
- Decision: do not install separately; absorb only the cross-domain lenses into this SA&BOO front door.

## User-supplied review and typography workflows — 2026-10-24

- Reviewed the pasted `design-review` and `Font Pairings` texts supplied in this
  chat. The first text attributes itself to `crit.officialjp.com`; original
  authorship, upstream revision, and licensing were not established. Neither
  attachment was installed or copied as a standalone skill.
- Reinforced the existing critique protocol with brief-ranked findings, located
  evidence, useful specificity, strengths to preserve, and the first effective
  change. Fixed numerical design recipes and mandatory checklist/report quotas
  were not adopted. Editing follows the actual authorized scope.
- Independently rewrote font comparison guidance in the graphic director's
  `references/font-pairing-comparison.md`, shared conditionally with presentation
  and UI work. It uses real copy, role-based mapping, Chinese/bilingual checks,
  protected originals, and inspected renders. Fixed five-option duplication,
  English joke labels, family-only role mapping, and guaranteed layout preservation
  were not adopted. Named Figma APIs are implementation guidance, not proof of
  live tool access or completed font tests.

## Security result

- No new API keys, tokens, accounts, payments, or macOS permissions.
- No user images uploaded to a new service.
- No shell installer, package manager, telemetry, or daemon introduced.
- No Computer Use, screenshot-driven clicking, mouse/keyboard automation, Codex CLI, or Gemini CLI.
- Local crop script uses Pillow only and never overwrites the source.
