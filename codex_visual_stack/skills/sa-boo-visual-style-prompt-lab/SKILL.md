---
name: sa-boo-visual-style-prompt-lab
description: Use for writing, translating, normalizing, or strengthening bilingual image/video prompts and controllable visual-generation vocabulary. Do not use as the design owner for typography, brand, product, campaign, interior, or image critique.
---

# SA&BOO Visual Style Prompt Lab

## Scope boundary

Use the current brief and supplied references directly. Do not start a reference
library, asset index, visual audit, or design-strategy workflow merely to write a
prompt. Route actual lettering, brand, product, campaign, interior, or critique
decisions to their owner and translate the selected or clearly provisional project direction into controllable
generation language.

Translate current visual culture into reusable, controllable text-to-image systems for SA&BOO. Use this skill as the bridge between trend research, prompt engineering, brand art direction, and tool/MCP execution.

## Default stance

- Treat trends as **visual mechanisms**, not looks to copy.
- Preserve the current project's supplied identity and tone. SA&BOO house-style
  recipes apply only to SA&BOO work or when Bonnie explicitly selects them; never
  transfer restrained-luxury or East-West language into YOSH or another artist/brand by default.
- Convert vague taste words into controllable variables: subject, material, camera, light, composition, texture, typography zone, motion, negative constraints.
- Separate style claims into **lineage/tradition, medium/process, format/discipline, genre/worldbuilding, visual mechanism, and mood/finish**. Do not flatten all six into one “style” bucket.
- Separate tone and lighting claims into **global grade, source, shadow, atmosphere, optical effect, surface response, and mood**. Do not treat a color filter, a physical light source, and a lens effect as interchangeable.
- Treat a style name as a hypothesis until the pixels or brief support it. Subject matter alone does not prove style: robots do not automatically mean cyberpunk, red does not automatically mean revolutionary art, and ornament does not automatically mean Baroque.
- Judge taste through hierarchy, coherence, material/process credibility, specificity, restraint, and original translation—not through an assumption that luxury, realism, detail, or historical ornament is inherently superior.
- For current trend or product-capability claims, browse official sources and cite links. If sources are login-gated, state the limitation and use public official pages or user screenshots.
- Pair this skill with:
  - `references/bilingual-art-style-ontology.md` when the task involves art-style names, bilingual terminology, style recognition from images, taste calibration, style mixing, or converting broad labels into visible/generative mechanisms.
  - `references/bilingual-tone-lighting-ontology.md` when the task involves color tone, grading, filters, lighting, shadows, glow, halo, bloom, caustics, refraction, mist shafts, dappled light, bokeh, rainbow, or poetic light descriptions.
  - `references/bilingual-design-keyword-ontology.md` when the task mixes 3D/C4D/Blender/render terms, typography/logo/text-design terms, IP-character/art-toy/blind-box terms, materials, software, production, and output keywords across fields.
  - `references/bilingual-prompt-translation.md` when the request is to translate, strengthen, structure, or adapt a bilingual image/video prompt.
  - `references/style-mixer-mode.md` for multiple style variants of one locked subject.
  - `references/house-style-liquid-silver.md` for liquid silver, chrome, mercury, acid/Y2K, and cyber-luxury prompts.
  - `references/house-style-lineart-blueprint.md` for technical line art, product blueprints, annotations, and vector-ready design sheets.
  - `references/house-style-victorian-ornamental-line.md` for Victorian, Rococo, Renaissance, floral, emblem, frame, and decorative line systems.
  - `bonnie-creative-backend-routing` plus Hermes `image_generate` when the user wants actual bitmap generation/editing. Verify the effective non-text image backend with a real call before claiming availability; never route bitmap work through a text/Responses provider.
  - Figma skills/MCP when the result should become a design system, screen, component, FigJam diagram, or presentation layout.

## Live retail-project gate / 真实零售项目许可

When the output proposes a real retail or branded-commercial space, use
`sa-boo-retail-design-partner` first. Style mixing may explore how an approved
mechanism appears, but it may not define the project object, replace
merchandising or operating logic, or approve concept through visual attraction.

Keep independent style research available for learning and aesthetic
calibration. For project work, require stage permission and label unsupported
formal exploration `NOT YET TESTABLE / 暂不可判断`.

## Workflow

1. **Classify the task**
   - Exploration: moodboard, art direction, visual territories.
   - Production: ready-to-use image prompts, ad/KV, social cover, product mockup, interior concept, brand symbol.
   - Systemization: prompt library, style matrix, reusable variables, negative prompt bank.
   - Tool routing: image model, Figma, Canva MCP, browser, deck/PDF output.

2. **Run the style-literacy gate**
   - Read `references/bilingual-art-style-ontology.md` when translating or identifying art styles, interpreting a list of labels, comparing style families, diagnosing an image, or converting a style into a prompt.
   - Read `references/bilingual-tone-lighting-ontology.md` when translating or diagnosing tone, lighting, filters, shadows, atmospheric effects, or optical effects.
   - Read `references/bilingual-design-keyword-ontology.md` when normalizing cross-domain keywords or translating 3D, typography/logo, or IP-character briefs.
   - Normalize each term before use: preferred Chinese and English name, label class, visible mechanisms, nearest alternatives, ambiguity, and confidence.
   - For image diagnosis, pair with `sa-boo-visual-reasoning-critic`; inspect the actual pixels, then report primary lineage, secondary mechanism, medium/process, genre/mood, evidence, alternatives, and local confidence.
   - For generation, use a hierarchy rather than a keyword pile: one primary lineage or design logic + one secondary mechanism + one medium/render method + one light/finish treatment.
   - For tone/light, build the light stack in order: exposure/value → global grade → source/direction → shadow → atmosphere → optical accent → surface response → camera/filter.
   - For cross-domain briefs, separate identity, form, material, light, graphic, style, output, mood, and production. Treat software names and resolution targets as workflow/output cues, not visual style proof.

3. **Choose the trend lens**
   - Read `references/visual-style-radar-2026.md` when the user asks about Canva-like, Adobe/Figma, current, 2026, social, web, or broad visual-style trends.
   - Use trend names as shorthand only after translating them into visual variables.

4. **Build the prompt operating system**
   - Read `references/prompt-operating-system.md` when generating serious prompt sets, platform-specific prompts, negative prompts, image QA, or prompt templates.
   - Keep intent, reference roles, composition, and necessary preserve/change controls clear. Include material, light, camera, motion, output, and platform detail only when they change this result; do not turn every prompt into a long fixed form.

5. **Select recipes and house styles**
   - Read `references/style-recipes.md` when the user wants immediate prompt variants or “做成不同风格”.
   - Read `references/style-mixer-mode.md` when several variants must preserve the same subject, geometry, camera, crop, logo/text-safe zone, and palette anchors.
   - Load only one deep house-style reference unless Bonnie explicitly asks to compare or mix several.
   - Use a house-style recipe only when the current SA&BOO project or Bonnie's selection supports it. Otherwise translate the selected reference mechanism directly; do not add a recurring luxury, paper, grain, chrome, or lighting finish merely because it is familiar.

6. **Route to tools/MCPs**
   - Read `references/mcp-tool-routing.md` when the user asks what tools, plugins, or MCPs to use/install, or when the output needs Figma/Canva/workflow integration.
   - If a requested MCP/plugin is unavailable in the current tool list, say so and provide the exact future setup route rather than pretending it is installed.
   - Distinguish a developer-documentation MCP from a production design connector. A docs server that answers SDK questions is not a design editor.
   - For current OpenAI model routing, keep orchestration models and image-generation models separate; do not send bitmap generation through a text/reasoning model route.

7. **Output and QA**
   - For prompts, output concise bilingual prompts plus variables and negative terms.
   - For systems, output a matrix: style / best use / prompt formula / risks / tool route.
   - Run a risk check: copyright, client privacy, model limitations, text rendering, brand uniqueness, platform terms.


## Premium reference input rule

Use `sa-boo-premium-reference-curator` when the visual evidence is insufficient or
the user requests a reference set. A clear supplied reference or already inspected
project source does not need another curation pass. Convert actual references into
controllable variables rather than copying style labels.

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

### Bilingual style diagnosis

```text
分析范围 / Scope：
规范术语 / Normalized term：
类别 / Class：lineage | tradition | medium | format | genre | mechanism | mood/finish
主要风格 / Primary style：
次要机制 / Secondary mechanism：
媒介与工艺 / Medium and process：
可见依据 / Visible evidence：
近邻风格 / Nearest alternatives：
不成立项 / Unsupported labels：
置信度与限制 / Confidence and limits：
生成转译 / Generation translation：
```

### Tone / lighting diagnosis

```text
分析范围 / Scope：
全局色调 / Global grade：
主光源与方向 / Key source and direction：
阴影与对比 / Shadow and contrast：
空气介质 / Participating medium：
光学效果 / Optical effect：
材质响应 / Surface response：
可见依据 / Visible evidence：
设计效果 / Perceptual effect：
风险与最小修改 / Risk and smallest effective change：
未知与置信度 / Unknowns and local confidence：
```

### Cross-domain keyword solution

```text
任务领域 / Domain：3D | typography/logo | IP character | mixed
规范术语 / Normalized terms：
身份与主体 / Identity and subject：
形体与结构 / Form and structure：
材质与工艺 / Material and process：
灯光与相机 / Lighting and camera：
图形与文字 / Graphic and typography：
风格机制 / Style mechanism：
输出规格 / Output specification：
生产工具 / Production tool：
中文口令 / Chinese prompt：
English prompt：
负面约束 / Negative constraints：
编辑交付与QA / Editable handoff and QA：
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
- Use no more than one primary lineage, one subordinate mechanism, one medium/render method, and one light/finish treatment unless the user explicitly requests an experimental style collision. State which layer controls composition, mark-making, material, and atmosphere.
- For tone/light prompts, name the source and direction before adding effects; choose one optical accent, preserve shadow detail, and explain any participating medium. Do not stack glow, halo, bloom, flare, and dazzling as separate controls without a defined hierarchy.
- For 3D, typography/logo, and IP-character prompts, assign every keyword to a layer before writing: identity, form, material, light, graphic, style, output, mood, or production. Do not treat C4D, Blender, Octane, PBR, 8K, blind box, or PVC as interchangeable style adjectives.
- For image models, do not rely on abstract labels alone: “高级感” must become material + lighting + composition + restraint.
- Choose the typography role before prompting. For expressive lettering or type-image composition, design the real words, silhouette, counters, hierarchy, and relation to the image together. For quiet factual copy, define a deliberate reading region. Add exact copy through a local layout tool when useful; a reserved blank area is not the default answer to typography, and post-compositing is not proof of integration.
- For edits or multi-reference work, assign each reference a role: subject identity, structure, composition, material, lighting, palette, or detail. State what must remain unchanged and what may change.
- For batch variants, lock subject geometry, product proportions, logo placement, palette anchors, camera, and crop before varying style.
- When a result must remain editable, plan the handoff explicitly: generated raster layers or reference assets → editable Canva/Figma layout → exact typography/brand tokens → export QA.
- For social covers, reserve title-safe zones and avoid clutter behind text.
- For brand/logo exploration, request vector-friendly marks, simple silhouettes, and no fake brand names; final marks still require uniqueness checks.
- Check exact words and character anatomy in the actual raster preview; repair only relevant defects. Use official logo artwork without regeneration. Finish independent paths or live text in a vector-capable editor when an editable or production master is explicitly requested, rather than imposing that step on every image request.
- For IP characters, lock head-to-body ratio, silhouette, face, hair, costume, signature detail, material, palette, camera, and ground contact before generating variants; treat blind box as a product/presentation format, not a complete style.
- For interiors, label AI images as concept explorations and verify dimensions/material feasibility before client-facing use.
