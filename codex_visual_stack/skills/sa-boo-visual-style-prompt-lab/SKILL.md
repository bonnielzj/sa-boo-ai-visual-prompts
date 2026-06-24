---
name: sa-boo-visual-style-prompt-lab
description: SA&BOO trend-aware text-to-image prompt laboratory for converting design intentions into controllable visual-style systems, drawing from current Canva/Adobe/Figma/Pinterest-like visual trends, SA&BOO prompt skills, and available image/Figma/Canva-style MCP routes. Use when the user asks to strengthen image prompts, generate prompt systems, remix visual styles, research Canva-like design aesthetics, choose image/video tools or MCPs, build moodboards, or translate brand/interior/content ideas into Midjourney, DALL·E/gpt-image, Stable Diffusion, 即梦, Runway, Figma, or Canva workflows. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Visual Style Prompt Lab

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Translate current visual culture into reusable, controllable text-to-image systems for SA&BOO. Use this skill as the bridge between trend research, prompt engineering, brand art direction, and tool/MCP execution.

## Default stance

- Treat trends as **visual mechanisms**, not looks to copy.
- Preserve SA&BOO DNA: restrained luxury, material translation, East-West narrative, symbolic abstraction, editorial craft, commercial clarity.
- Convert vague taste words into controllable variables: subject, material, camera, light, composition, texture, typography zone, motion, negative constraints.
- For current trend or product-capability claims, browse official sources and cite links. If sources are login-gated, state the limitation and use public official pages or user screenshots.
- Pair this skill with:
  - `sa-boo-prompt-translator` for bilingual prompt output.
  - `sa-boo-style-mixer` for multiple style variants.
  - `sa-boo-liquid-silver-style`, `sa-boo-lineart-blueprint`, `sa-boo-victorian-ornamental-line` for deep house styles.
  - `imagegen` when the user wants actual bitmap generation/editing.
  - Figma skills/MCP when the result should become a design system, screen, component, FigJam diagram, or presentation layout.

## Workflow

1. **Classify the task**
   - Exploration: moodboard, art direction, visual territories.
   - Production: ready-to-use image prompts, ad/KV, social cover, product mockup, interior concept, brand symbol.
   - Systemization: prompt library, style matrix, reusable variables, negative prompt bank.
   - Tool routing: image model, Figma, Canva MCP, browser, deck/PDF output.

2. **Choose the trend lens**
   - Read `references/visual-style-radar-2026.md` when the user asks about Canva-like, Adobe/Figma, current, 2026, social, web, or broad visual-style trends.
   - Use trend names as shorthand only after translating them into visual variables.

3. **Build the prompt operating system**
   - Read `references/prompt-operating-system.md` when generating serious prompt sets, platform-specific prompts, negative prompts, image QA, or prompt templates.
   - Always separate: core intent / style engine / composition / material / light / camera-render / constraints / platform parameters.

4. **Select recipes and house styles**
   - Read `references/style-recipes.md` when the user wants immediate prompt variants or “做成不同风格”.
   - Combine external trend mechanisms with SA&BOO house styles instead of copying platform examples.

5. **Route to tools/MCPs**
   - Read `references/mcp-tool-routing.md` when the user asks what tools, plugins, or MCPs to use/install, or when the output needs Figma/Canva/workflow integration.
   - If a requested MCP/plugin is unavailable in the current tool list, say so and provide the exact future setup route rather than pretending it is installed.

6. **Output and QA**
   - For prompts, output concise bilingual prompts plus variables and negative terms.
   - For systems, output a matrix: style / best use / prompt formula / risks / tool route.
   - Run a risk check: copyright, client privacy, model limitations, text rendering, brand uniqueness, platform terms.

## Standard output formats

### Ready-to-use image prompt

```text
视觉方向：
适合用途：
中文口令：
English prompt：
关键词：
负面词：
可替换变量：
平台建议：
MCP/工具路线：
QA检查：
```

### Visual style matrix

```text
主题：
核心视觉判断：
风格矩阵：风格｜视觉机制｜中文口令｜英文关键词｜适合平台｜风险
优先推荐：
下一步生成/落地：
```

### MCP/tool route

```text
目标：
当前可用：
推荐路线：brief → prompt → generation/prototype → edit → export → QA
可考虑安装/连接：
不可用或需用户授权：
```

## Prompt quality rules

- Add sensory language only when it improves controllability: tactile, translucent, waxy, glassy, grainy, velvet, metallic, paper fiber, ambient sound, cinematic rhythm.
- For image models, do not rely on abstract labels alone: “高级感” must become material + lighting + composition + restraint.
- For typography-heavy prompts, specify a reserved text area and keep generated text minimal; exact Chinese/English text is often better added later in Figma/Canva.
- For social covers, reserve title-safe zones and avoid clutter behind text.
- For brand/logo exploration, request vector-friendly marks, simple silhouettes, and no fake brand names; final marks still require uniqueness checks.
- For interiors, label AI images as concept explorations and verify dimensions/material feasibility before client-facing use.
