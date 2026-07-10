# imagegen NewAPI global route

Date: 2026-07-10

## Context

Bonnie asked Codex global image generation to use the NewAPI-compatible image channel at:

- Base URL: `https://ai.lzlquantdesign.com/v1`
- Generate endpoint: `/v1/images/generations`
- Edit endpoint: `/v1/images/edits`
- Wire API for image work: `images`
- Forbidden wire API for image work: `responses`

The user-provided raw API key must not be written into project files, notes, final replies, or shared documentation.

## Local Private Files Updated

These local private files were updated:

- `/Users/bonnie/.codex/config.toml`
- `/Users/bonnie/.profile`
- `/Users/bonnie/.codex/AGENTS.md`
- `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md`

The actual key is stored only in local private environment/config files, not in this repository note.

## Active Environment Variables

Image CLI/API fallback should use:

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL=https://ai.lzlquantdesign.com/v1`
- `LZLQUANTDESIGN_IMAGE_API_KEY`
- `LZLQUANTDESIGN_IMAGE_BASE_URL=https://ai.lzlquantdesign.com/v1`

## Required Behavior

For global image generation:

1. Use `client.images.generate(...)` or equivalent Images API calls.
2. Use `/v1/images/generations` for generation.
3. Use `/v1/images/edits` for edits.
4. Do not use the Responses API for image generation or image editing.
5. Do not configure `wire_api = "responses"` for image work.
6. Do not print or persist raw API keys in project files.

## Verification

The bundled `imagegen` CLI dry-run reported:

- endpoint: `/v1/images/generations`
- model: `gpt-image-2`
- output format: `png`
- `OPENAI_API_KEY` detected

This verifies CLI routing shape without making a paid/live image API request.

## Security Note

Because the raw key was pasted into a Codex chat, rotate it if this thread or logs may be shared outside the local machine.
