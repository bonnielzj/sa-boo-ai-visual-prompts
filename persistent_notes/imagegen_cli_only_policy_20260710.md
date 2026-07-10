# imagegen CLI-only policy

Date: 2026-07-10

## Context

Bonnie explicitly rejected the built-in `image_gen` route and required using only the second route, meaning the CLI/API image-generation path.

## Decision

For Bonnie's environment:

1. Do not use the built-in `image_gen` route for normal image work.
2. Use only the bundled `scripts/image_gen.py` CLI/API workflow.
3. Route image generation through the configured WE-AI AZ full image route.
4. Keep using:
   - `BASE_URL=https://asian-acc.we-token.cc`
   - `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
   - `POST /v1/images/generations`
   - `POST /v1/images/edits`
5. Do not use the Responses API for image generation.

## Files Updated

- `/Users/bonnie/.codex/AGENTS.md`
- `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md`

## Effect

Future `imagegen` routing for Bonnie should treat the CLI/API path as the active path, not as a fallback path.
