# SA&BOO Codex Visual Stack Backup

Created: 2026-06-24T23:25:47

This folder is a GitHub-safe backup of Bonnie's visual/design-related Codex stack.
It includes real skill instructions and reference files, plus visual asset-chain examples, but **does not include real API keys, tokens, private relay URLs, account auth files, or large proprietary binaries**.

## Contents

- `skills/` — copied visual/design/CAD/SketchUp/render/prompt/Figma/presentation-related Codex skills.
- `manifests/visual_skills_manifest.json` — searchable manifest of copied skills and files.
- `mcp_templates/` — safe placeholder config for MCP servers, keys, and URLs.
- `visual_chains/` — existing repository visual asset chain/index examples.
- `project_examples/logicat_r16/` — real non-empty project QA visual chain sample from Logicat popup R16.

## Why this is not an empty shell

The package includes:

- full `SKILL.md` files;
- selected `references/` and `scripts/` from skills where safe;
- integrated production loop document;
- image-generation workflow document;
- CAD accuracy workflow document;
- MCP/key/url templates with placeholders;
- visual asset manifests and linked lists;
- one real project QA image and JSON chain.

## Security policy

Never commit:

- real `OPENAI_API_KEY`, `GITHUB_TOKEN`, `FIGMA_ACCESS_TOKEN`, relay tokens, or private URLs;
- `.codex/auth.json`, `accounts/`, `secrets.json`, relay state, or account snapshots;
- private client CAD/DWG/SKP unless explicitly cleared for sharing;
- supplier/client confidential files.

Use `${PLACEHOLDER}` values in templates, then fill them locally.

## Restore pattern

```bash
# Example only. Review before copying.
cp -R codex_visual_stack/skills/<skill-name> "$HOME/.codex/skills/"
cp codex_visual_stack/mcp_templates/codex_mcp_config.template.toml ./codex_mcp_config.local.toml
# Fill placeholders locally, never commit the filled file.
```
