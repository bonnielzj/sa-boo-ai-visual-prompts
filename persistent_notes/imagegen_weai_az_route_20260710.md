# imagegen WE-AI AZ full route

Date: 2026-07-10

## Context

Bonnie asked to configure global image generation to use the WE-AI AZ full image route.

The raw API key is stored only in local private environment/config files. Do not copy it into project notes, shared docs, final replies, screenshots, or GitHub.

## Active Route

- Route label: `we-ai-az-full`
- Direct HTTP `BASE_URL`: `https://asian-acc.we-token.cc`
- OpenAI-compatible SDK `OPENAI_BASE_URL`: `https://asian-acc.we-token.cc/v1`
- Generation endpoint: `/v1/images/generations`
- Edit endpoint: `/v1/images/edits`
- Wire API for image work: `images`
- Forbidden wire API for image work: `responses`
- Default model: `gpt-image-2`

## Local Private Files Updated

- `/Users/bonnie/.codex/config.toml`
- `/Users/bonnie/.profile`
- `/Users/bonnie/.zshenv`
- `/Users/bonnie/.codex/AGENTS.md`
- `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md`

Backups were created with suffix:

- `.bak-az-image-route-20260710_*`

## Required Behavior

1. For text-to-image, call `POST ${BASE_URL}/v1/images/generations`.
2. For image editing / image-to-image, call `POST ${BASE_URL}/v1/images/edits` with `multipart/form-data`.
3. Use `Authorization: Bearer ${API_KEY}`.
4. Use `model=gpt-image-2` by default.
5. Decode `data[0].b64_json` and save it as a local image file.
6. Do not use `/v1/responses` or `/v1/chat/completions` for image work.
7. Do not use the built-in `image_gen` path when Bonnie explicitly requires this custom global route, because the built-in tool does not expose custom base URL/key controls. Use the bundled `scripts/image_gen.py` CLI/API path.

## Verification

Dry-run verification:

- `OPENAI_BASE_URL=https://asian-acc.we-token.cc/v1`
- endpoint: `/v1/images/generations`
- model: `gpt-image-2`
- size: `1024x1024`

Live smoke test:

- Prompt: simple centered blue circle on white background, no text, no watermark
- Model: `gpt-image-2`
- Size: `1024x1024`
- Quality: `low`
- Result: success
- Runtime: about `80.4s`
- Output: `/Users/bonnie/Documents/乖乖成长日志/codex_outputs/imagegen_smoke_test/weai_az_smoke_20260710.png`
- File check: PNG, RGB, `1024 x 1024`, about `38K`

## Notes

The WE-AI docs recommend using long client timeouts for image generation, roughly 30 minutes, because the service may retry upstream image requests internally.
