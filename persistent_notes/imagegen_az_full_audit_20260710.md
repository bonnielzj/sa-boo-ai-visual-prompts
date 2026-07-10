# imagegen AZ full audit

Date: 2026-07-10

## Objective

Verify that all active image-generation touchpoints use the latest WE-AI AZ configuration, and remove or supersede stale routes that could still send image work to old domains, built-in image generation, or Responses API paths.

## Required Current Route

- Route label: `we-ai-az-full`
- `BASE_URL=https://asian-acc.we-token.cc`
- `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
- Generation endpoint: `/v1/images/generations`
- Edit endpoint: `/v1/images/edits`
- Model: `gpt-image-2`
- Image wire API: `images`
- Forbidden for image work: `responses`
- Active execution mode: CLI/API only via `scripts/image_gen.py`

## Active Touchpoints Audited

Checked and aligned:

- `/Users/bonnie/.codex/config.toml`
- `/Users/bonnie/.profile`
- `/Users/bonnie/.zshenv`
- `/Users/bonnie/.codex/AGENTS.md`
- `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md`
- `/Users/bonnie/Library/LaunchAgents/com.bonnie.codex.image-env.plist`
- `/Users/bonnie/Documents/乖乖成长日志/AGENTS.md`
- `/Users/bonnie/Documents/乖乖成长日志/source_skill_files/mcp-tool-routing.md`
- `/Users/bonnie/Documents/乖乖成长日志/codex_skills/sa-boo-visual-style-prompt-lab/references/mcp-tool-routing.md`
- `/Users/bonnie/Documents/乖乖成长日志/persistent_notes/imagegen_502_failure_handling_20260710.md`
- `/Users/bonnie/Documents/乖乖成长日志/persistent_notes/imagegen_newapi_global_route_20260710.md`
- `/Users/bonnie/Documents/乖乖成长日志/persistent_notes/imagegen_cli_only_policy_20260710.md`
- `/Users/bonnie/Documents/乖乖成长日志/persistent_notes/imagegen_weai_az_route_20260710.md`

## Problems Found

1. Workspace `AGENTS.md` still said quick previews should use built-in `image_gen`.
2. Reusable `mcp-tool-routing.md` files still routed concept-image work to built-in `image_gen`.
3. Historical persistent notes still looked current enough to mislead future work toward built-in-first or `ai.lzlquantdesign.com`.
4. `~/.zshenv` still had an older image-route block at the top.
5. `~/Library/LaunchAgents/com.bonnie.codex.image-env.plist` still injected:
   - `OPENAI_BASE_URL=https://ai.lzlquantdesign.com/v1`
   - old image key/env aliases

The launch agent issue was the most important runtime risk because GUI/session startup could still inherit the old image route even after later shell exports were corrected.

## Fixes Applied

1. Kept global policy as CLI/API-only for Bonnie image generation.
2. Updated workspace `AGENTS.md` to require WE-AI AZ CLI/API routing even for quick previews.
3. Updated both reusable `mcp-tool-routing.md` files to route image work through `scripts/image_gen.py`.
4. Marked the older persistent notes as historical/superseded instead of deleting them.
5. Removed stale old-route exports from `~/.zshenv`.
6. Rewrote `com.bonnie.codex.image-env.plist` to inject the AZ route:
   - `BASE_URL=https://asian-acc.we-token.cc`
   - `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
   - `CODEX_IMAGE_ROUTE=we-ai-az-full`
7. Reloaded the launch agent and confirmed the live `launchctl` environment matches the AZ route.

## Verification Evidence

### Shell environment

Confirmed:

- `BASE_URL=https://asian-acc.we-token.cc`
- `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
- `CODEX_IMAGE_ROUTE=we-ai-az-full`

### launchctl environment

Confirmed:

- `BASE_URL=https://asian-acc.we-token.cc`
- `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
- `CODEX_IMAGE_ROUTE=we-ai-az-full`
- `CODEX_IMAGE_GENERATE_ENDPOINT=/v1/images/generations`
- `CODEX_IMAGE_EDIT_ENDPOINT=/v1/images/edits`

### Codex config

Confirmed in `~/.codex/config.toml`:

- `base_url = "https://asian-acc.we-token.cc/v1"`
- `generate_endpoint = "/v1/images/generations"`
- `edit_endpoint = "/v1/images/edits"`
- `image_route = "we-ai-az-full"`
- `wire_api = "images"`
- `forbid_wire_api = "responses"`

### imagegen CLI dry-run

Confirmed:

- endpoint: `/v1/images/generations`
- model: `gpt-image-2`
- size: `1024x1024`

### Live smoke test

Prompt:

- `Final AZ audit smoke test: one red square centered on a light gray background, no text, no watermark, minimal composition.`

Parameters:

- model: `gpt-image-2`
- size: `1024x1024`
- quality: `low`

Result:

- success
- runtime: about `33.9s`
- output path: `/Users/bonnie/Documents/乖乖成长日志/codex_outputs/imagegen_audit_20260710/final_az_audit_smoke.png`
- file type: PNG
- image size: `1024 x 1024`

## Completion Status

As of this audit, all active image-generation touchpoints that can realistically steer current or future work are aligned to the latest WE-AI AZ CLI/API configuration.

Historical backups, old session logs, and archived output reports still contain old values, but they are not active configuration sources and were not treated as blockers to current completion.
