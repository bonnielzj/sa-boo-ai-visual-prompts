---
name: sa-boo-prompt-translator
description: SA&BOO prompt translator for converting Chinese design intentions into structured AI image prompts for Midjourney, DALL·E, Stable Diffusion, Jimeng/即梦, Runway, and other image/video models. Use when the user asks to write, improve, translate, structure, or adapt AI prompts across styles, platforms, languages, or prompt formulas.
---

# SA&BOO Prompt Translator

Translate Chinese aesthetic intentions into structured prompts that image/video models can understand while preserving SA&BOO's refined design language.

## Core principle

Do not merely translate words. Translate design intention into model-controllable visual variables.

## Required structure

When generating prompts, output:

```text
中文口令：
英文口令：
关键词：
负面词：
平台建议：
可替换变量：
```

## Prompt variables

Always consider these fields:

- Subject: person, product, logo, flower, interior, object, installation.
- Style: minimalism, acid, cyberpunk, Victorian, blueprint, Memphis, East-West luxury.
- Material: liquid metal, paper, silk, leather, glass, acrylic, stone, wood, gold foil.
- Composition: centered, symmetric, asymmetrical, grid system, close-up, wide angle, poster layout.
- Color: black-silver, gold, pink-purple-blue, high saturation, low saturation, monochrome.
- Lighting: soft diffusion, rim light, studio lighting, backlight, Tyndall effect, cinematic light.
- Detail density: minimal, maximal, ultra-fine line, clean negative space.
- Camera/render: 3D render, product photography, editorial poster, illustration, hand draft.
- Constraints: no watermark, no messy text, no extra objects, clean background.

## Chinese to English mapping

- 高级感 → premium / high-end / refined / luxury editorial
- 液态银色金属 → liquid silver metal / mercury-like chrome
- 弥散光 → diffused glow / soft diffusion
- 酸性设计 → acid design
- 梦核 → dreamcore
- 朦胧感 → hazy atmosphere / soft blur
- 低调奢华 → understated luxury
- 极繁主义 → maximalist intricate detail
- 线稿蓝图 → technical line-art blueprint
- 留白 → negative space
- 符号化 → symbolic abstraction

## Platform notes

- Midjourney: emphasize visual style, composition, materials; add aspect ratio if user gives format.
- DALL·E: use natural language, clear constraints, fewer stacked style tags.
- Stable Diffusion: include positive prompt + negative prompt separately.
- 即梦/Chinese tools: bilingual prompts often work; keep Chinese semantic richness.
- Runway/video: add motion, camera movement, duration, transition, atmosphere.

## Refinement checklist

Before finalizing, ensure prompt has: subject, material, composition, lighting, color, quality, constraints, and purpose.
## Trend-aware extension

When the request mentions Canva-like trends, current visual styles, MCP/tool routing, or asks to strengthen a text-to-image workflow, pair this skill with `sa-boo-visual-style-prompt-lab`. Use that skill's references to translate trends into visual mechanisms before writing the final bilingual prompt.

Before finalizing serious image prompts, check: core intent, style engine, composition, material/texture, light/color, camera/render, typography/text zone, constraints, negative prompts, and platform adapter.

