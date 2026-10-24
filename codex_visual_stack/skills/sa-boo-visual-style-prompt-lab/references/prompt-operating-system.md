# SA&BOO Prompt Operating System

Use this to turn a design intention into controllable prompts across image/video models and design MCP workflows.

Use the spine as an optional vocabulary, not a mandatory form. Retain only fields
that change the current result. Resolve the project purpose and image-making idea
with the domain owner before adding rendering detail. If recent prompts keep
inserting the same finish despite different references, remove that inherited
positive instruction; more negative adjectives do not resolve the contradiction.

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
Reference roles: ...
Preserve/change contract: ...
Typography/text zone: ...
Mood: ...
Constraints: ...
Negative prompts: ...
Output specs: ...
```

Chinese compact formula:

```text
为{用途/平台}生成{主体}视觉，核心表达是{具体内容}。用{主要视觉关系}组织{主体/字图/空间/动势}，配合必要的{材料、光、色彩或镜头判断}。文字承担{主视觉/回应/说明}角色，按{字形、尺度、节奏与图像关系}构图。保持{实际不变量}，避免{本稿已知失效条件}。
```

English compact formula:

```text
Create a {channel/use} visual expressing {specific proposition}. Organize {subject, imagery, type, space or motion} through {dominant relationship}. Use only the {material, light, colour or camera decisions} that support it. Give real words {their intended role and hierarchy}. Preserve {actual invariants}; avoid {known failure conditions}.
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

## 3. Reference and edit controls

For edits, inpainting, outpainting, or multi-image workflows, map every input:

```text
Reference 1: subject identity / product geometry
Reference 2: composition / camera
Reference 3: material / lighting / palette
Keep unchanged: ...
Change only: ...
Remove: ...
Add: ...
Output continuity: same crop / same proportions / same logo position / same label spelling
```

Do not use “参考这个感觉” as the only instruction. Name the transferable property and reject visible copying of protected or client-specific work.

## 4. Platform adapters

### Image generation — current host

- Use natural language with clear constraints.
- Keep prompt coherent; avoid huge keyword dumps.
- Use the image-generation skill and tool actually exposed in the current host;
  do not ban its built-in tool because another environment used a different route.
  Follow current tool instructions for inputs, edits, transparency, and output.
- If an external Images API is needed and authorized, check the configured endpoint,
  credentials, and supported model/capabilities without exposing credential values.
  Do not inherit a static latest-model claim or provider restriction from this file.
- Separate orchestration/text tools from actual bitmap generation. A configured
  provider or exposed tool does not prove a completed image; inspect the real output.
- Plan exact copy and typography with the image. Use a layout editor for the
  requested editable/production stage or a necessary bounded repair.
- Good for: concepts, product shots, editorial visuals, clean social imagery, style exploration.

### Editable-layer handoff

Only when editability or a production master is requested, plan:

```text
Handoff plan: preserve the approved visual relationships while separating the
required hero art, exact copy, official identity, and other editable elements in
the requested production surface. Text regions follow the composition already
designed; do not rebuild the image around a generic blank caption box.
```

Do not treat a successful image generation as proof that the final layout,
Chinese/English text, logo geometry, or brand system is production-ready.

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

## 5. Negative prompt bank

This is a menu of context-dependent examples. Use only exclusions supported by the
current brief or a concrete failure; do not paste whole categories into every
prompt or turn words such as luxury into a fixed saturation or texture policy.

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

Edit continuity:
`subject drift, altered product geometry, moved logo, misspelled label, duplicated object, mismatched perspective, edge seam, unintended crop, inconsistent shadow, style drift`

Editable handoff:
`flattened unreadable text, fake brand mark, merged foreground and background,
unclean object edges, accidental crop, hidden CTA area, inconsistent layer logic,
unrecoverable background, rasterized logo`

## 6. QA checklist

- Is the visual intent concrete enough for a model?
- Does the prompt include subject, composition, material, light, color, render mode, constraints?
- Is style hierarchy clear, or are there too many conflicting aesthetics?
- Is exact text necessary? If yes, should it be added manually after generation?
- Are reference roles and preserve/change constraints explicit?
- Are output size, quality, format, background behavior, and batch count compatible with the selected provider?
- Does the output need a design tool route: Figma/Canva for typography, layout, export, brand kit?
- Are client privacy/copyright/cultural references safe?
