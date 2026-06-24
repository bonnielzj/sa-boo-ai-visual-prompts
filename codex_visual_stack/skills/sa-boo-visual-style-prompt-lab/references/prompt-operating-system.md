# SA&BOO Prompt Operating System

Use this to turn a design intention into controllable prompts across image/video models and design MCP workflows.

## 1. Prompt spine

```text
[Purpose] for [audience/channel]
Subject: ...
Visual concept: ...
Style engine: ...
Composition: ...
Material/texture: ...
Lighting/color: ...
Camera/render: ...
Typography/text zone: ...
Mood: ...
Constraints: ...
Negative prompts: ...
```

Chinese compact formula:

```text
为{用途/平台}生成{主体}视觉，核心概念是{视觉母题}。画面采用{风格机制}，构图{位置/比例/留白/网格}，材质为{材质与触感}，光线{光型/方向/氛围}，色彩{主色/辅色/饱和度}，镜头/渲染{摄影/3D/插画/线稿}。预留{文字/Logo/CTA}区域。整体气质{情绪关键词}。避免{负面词}。
```

English compact formula:

```text
Create a {channel/use} visual of {subject}, built around {visual metaphor}. Use {style mechanism}, {composition}, {material/texture}, {lighting/color}, {camera/render mode}. Reserve a clean area for {text/logo/CTA}. Mood: {mood}. Avoid {negative constraints}.
```

## 2. Visual variables

- Subject: object, space, person, logo mark, product, installation, flower, UI scene.
- Style engine: editorial luxury, surreal AI, tactile material, retro-tech, blueprint, ornamental line, collage, cinematic drama.
- Composition: centered, symmetrical, grid, asymmetrical, close-up macro, wide hero, poster, split-screen, triptych, top-down, isometric.
- Material: liquid silver, chrome, glass, wax, paper fiber, silk, velvet, stone, wood, ceramic, acrylic, ink, gold/silver foil.
- Light: soft diffusion, rim light, spotlight, backlight, Tyndall effect, dark mode glow, daylight haze, stage lighting.
- Color: black-silver, cream-gold, off-white, muted earth, pale blue-violet, acid neon, hyper-saturated festival, monochrome.
- Detail density: minimal, editorial, rich but ordered, maximal ornament, zine chaos, UI micro-detail.
- Camera/render: product photography, 3D render, cinematic still, fashion editorial, macro, line art, vector-ready, UI mockup.
- Motion if video: slow push-in, parallax scroll, rotating product, drifting fabric, liquid morph, spotlight reveal.

## 3. Platform adapters

### DALL·E / gpt-image / built-in imagegen

- Use natural language with clear constraints.
- Keep prompt coherent; avoid huge keyword dumps.
- State exact text only when necessary; for final typography, prefer editing in Figma/Canva.
- Good for: concepts, product shots, editorial visuals, clean social imagery, style exploration.

### Midjourney

- Use dense visual keywords, composition, material, lighting, aspect ratio.
- Add `--ar` and `--stylize` if user needs a format; avoid too many conflicting styles.
- Good for: moodboards, art direction, fashion/editorial, surreal style search.

### Stable Diffusion / SDXL / Flux-like tools

- Separate positive and negative prompts.
- Add model-specific LoRA/control/reference rules only when known.
- Good for: controllable batches, style consistency, inpainting, local workflow.

### 即梦 / Chinese image tools

- Bilingual prompts often help: keep Chinese semantic richness, add English material/camera terms.
- Good for: Chinese social cover styles, commercial posters, fast variations.

### Runway / video tools

- Add action, camera movement, duration, transition, subject stability, atmosphere.
- Keep motion simple and directional.

## 4. Negative prompt bank

General:
`low quality, blurry, noisy, messy composition, watermark, fake logo, random text, distorted hands, extra objects, cluttered background, overexposed, cheap plastic, generic AI look`

Luxury/editorial:
`cheap glitter, gaudy decoration, overly saturated, messy reflections, crowded layout, low-end stock photo`

Line art/vector:
`photorealistic, shaded render, blurry lines, jagged edges, unreadable annotations, messy handwriting`

Interior:
`impossible structure, distorted furniture, unrealistic scale, unsafe stairs, blocked circulation, fake materials, overdecorated`

Social cover:
`unreadable title area, text behind busy background, random letters, low contrast, too many stickers`

## 5. QA checklist

- Is the visual intent concrete enough for a model?
- Does the prompt include subject, composition, material, light, color, render mode, constraints?
- Is style hierarchy clear, or are there too many conflicting aesthetics?
- Is exact text necessary? If yes, should it be added manually after generation?
- Does the output need a design tool route: Figma/Canva for typography, layout, export, brand kit?
- Are client privacy/copyright/cultural references safe?
