---
name: sa-boo-style-mixer
description: SA&BOO style mixing and style-transfer prompt skill for generating multiple aesthetic versions of the same theme across liquid silver, technical blueprint, Victorian ornament, East-West luxury, cyberpunk, Memphis, minimalism, gothic, dreamcore, acid design, and social-media cover styles. Use when the user asks to quickly create prompts in different styles, compare style directions, remix a theme, or build prompt variants. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Style Mixer

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Generate multiple style-translated prompts for one theme while preserving the same core subject.

## Principle

Keep the subject constant; change the aesthetic logic through material, composition, color, light, detail density, era, and emotional tone.

## Default output

For each style version, provide:

```text
风格名称：
适合用途：
中文口令：
英文关键词：
视觉重点：
```

## Core style menu

1. 液态银色金属：chrome, mercury, acid, Y2K, luxury future.
2. 技术蓝图线稿：line art, blueprint, annotations, multi-view, vector-ready.
3. 维多利亚极繁装饰：Rococo, floral, scrollwork, emblem, luxury frame.
4. 东方梦核银箔：eastern surrealism, ink, silver foil, dreamcore, low saturation.
5. 赛博朋克未来：neon, silhouette, goggles, cold tech, high contrast.
6. 孟菲斯高饱和：geometric, playful, bold color, anti-boring, postmodern.
7. 极简高级海报：negative space, Swiss grid, tiny typography, refined object.
8. 哥特暗黑奢华：black silver, wings, cross, gothic rose, sacred darkness.
9. 复古未来主义：retro-futurism, film grain, chrome, 70s/80s sci-fi.
10. 新媒体黑底封面：black background, strong title zone, high contrast, personal IP.

## Mixing method

For each requested style, rewrite these dimensions:

- Material
- Color
- Composition
- Lighting
- Texture
- Typography/text presence
- Detail density
- Commercial use case

## Fast command pattern

When the user says “把{主题}做成不同风格口令”, produce 5-10 variants. If no number is given, produce 6:

1. Liquid Silver Luxury
2. Technical Blueprint
3. Victorian Ornamental
4. Minimal Editorial
5. Cyber Acid
6. Xiaohongshu Cover

## Avoid

Do not make all variants synonyms. Each must have a clearly different visual mechanism.
## Trend-aware style expansion

When the user asks for current/Canva-like/Adobe/Figma/social visual directions, pair this skill with `sa-boo-visual-style-prompt-lab` and remix the subject through trend mechanisms, not just named styles. Recommended current mechanisms include: Reality Warp, Texture Check, Opt-Out quiet editorial, Drama Club cinematic hook, Prompt Playground retro-tech UI, Notes App Chic, Zinegeist, 3D immersive web hero, and dark chrome retrofuture.

Each variant should state the changed mechanism: material, composition, light, texture, typography/text zone, detail density, and commercial use case.

