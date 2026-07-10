# imagegen 502 failure handling note

Date: 2026-07-10

## Context

Bonnie asked to check the system `imagegen` skill after seeing an image-generation error explanation screenshot for `502 Bad Gateway`.

Checked skill:

- `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md`

## Finding

The skill already had the correct high-level routing:

- use built-in `image_gen` by default
- use CLI fallback only when explicitly requested, or after explicit confirmation for true native transparency
- do not silently downgrade to `gpt-image-1.5`
- do not edit `scripts/image_gen.py`

However, the main `SKILL.md` only said that if the built-in tool fails, the assistant should tell the user the CLI fallback exists. It did not explicitly classify common transient service failures such as:

- `502 Bad Gateway`
- `504 Gateway Timeout`
- upstream timeout
- temporary service unavailable

This could cause future runs to misread a backend timeout as a prompt problem, a local file-path issue, an `OPENAI_API_KEY` issue, or an automatic reason to switch to CLI.

## Change Applied

Updated `/Users/bonnie/.codex/skills/.system/imagegen/SKILL.md` under **Top-level modes and rules**.

Added rules:

- classify built-in `image_gen` failures before choosing a next step
- treat `502`, `504`, upstream timeout, and temporary unavailable errors as transient backend/server failures
- explain that these errors usually are not prompt, local path, or `OPENAI_API_KEY` problems
- do not automatically switch to CLI fallback after transient built-in failures
- retry built-in once only when the user asked for immediate output and the request is cheap
- if the retry fails, stop and offer retrying later or explicit CLI fallback
- do not run save-path, chroma-key removal, or validation steps until an actual built-in image file exists

## Practical Handling Going Forward

When built-in `image_gen` returns `502 Bad Gateway`, the correct response is:

1. Tell Bonnie it is usually a temporary image backend/server issue.
2. Do not claim that the prompt, transparent-background setup, local path, or API key caused it.
3. Retry once only for cheap immediate-output tasks.
4. If it fails again, pause and offer:
   - retry later with built-in `image_gen`
   - explicit CLI fallback, which requires `OPENAI_API_KEY`

Do not run `scripts/image_gen.py` unless Bonnie explicitly asks for CLI/API/model fallback or confirms the fallback after being told it requires `OPENAI_API_KEY`.

## Push Reminder

This repository has a GitHub remote:

- `https://github.com/bonnielzj/sa-boo-ai-visual-prompts.git`

The persistent note is local only until Bonnie explicitly allows committing/pushing.
