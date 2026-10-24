# Visual Style Radar 2026 — SA&BOO Translation

Access lens: public official pages checked on 2026-07-19. Use this as a trend-to-prompt map; re-browse for “latest/current” claims.

## Source anchors

- Canva Newsroom, “Imperfect by Design”: https://www.canva.com/newsroom/news/design-trends-2026/
- Adobe 2026 Creative Trends forecast: https://business.adobe.com/resources/creative-trends-report.html
- Figma, Top Web Design Trends for 2026: https://www.figma.com/resource-library/web-design-trends/
- Canva Developer MCP docs (Apps SDK questions only): https://www.canva.dev/docs/mcp/
- Figma MCP blog: https://www.figma.com/blog/introducing-figma-mcp-server/
- Figma release notes: https://www.figma.com/release-notes/
- Figma MCP remote server docs: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- Canva Magic Layers in AI assistants: https://www.canva.com/newsroom/news/magic-layers-ai-assistants/
- OpenAI GPT-5.6 guide: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI image generation guide: https://developers.openai.com/api/docs/guides/image-generation
- Adobe Firefly current capabilities: https://helpx.adobe.com/firefly/whats-new.html
- MCP specification: https://modelcontextprotocol.io/specification

## Core diagnosis

2026 visual culture is not “more polished AI”. It is **AI-assisted but intentionally human**: tactile, cinematic, imperfect, locally rooted, emotionally direct, and increasingly system-aware across websites, decks, social covers, brand kits, and motion.

SA&BOO should translate this into: refined imperfection, material truth, controlled drama, cultural specificity, and a repeatable prompt system.

## 2026-07-19 production delta

### New capability signals verified this week

| Signal | Confirmed capability | SA&BOO translation | Prompt/control variables |
|---|---|---|---|
| Canva Magic Layers in AI assistants | Canva says Magic Layers can turn a flat generated image into editable text, object, and background layers inside Canva; the Canva AI Connector is available across major AI-assistant surfaces after account connection | For an explicitly requested editable deliverable, use this capability when exposed and applicable; finish typography, brand tokens, resizing, and export in the chosen editor | layer intent, foreground/background separation, object isolation, text-safe zone, brand-token handoff, resize targets |
| Canva remote MCP | Official docs describe design generation/editing, design search, asset and brand management, export, resizing, and comments; custom remote clients require access review and OAuth | Separate the production design connector from the Canva developer-docs MCP; route write/export/comment only after permission review | target design ID, operation class, read/write scope, approval checkpoint, output format |
| Figma MCP remote server | Official docs list `create_new_file`, `download_assets`, `generate_diagram`, write-to-canvas, variables/components, and Code Connect; write and diagram features remain beta/free for now and supported clients are limited | For a requested Figma artifact, target the named file/page, reuse applicable variables/components, and inspect the actual result/export | target file/page, node selection, variable/component reuse, diagram type, screenshot QA, rollback copy |
| OpenAI GPT Image 2 | Current Image API docs specify `gpt-image-2`, separate generations/edits, multi-image references, mask-guided edits, `n`, partial-image streaming, flexible resolutions, and no transparent background support | Use the current exposed image tool and its documented controls; verify a changed or unproven required feature through the actual task/result or one focused check | model ID, endpoint, reference roles, mask, batch count, size, quality, format, compression, background behavior |
| Adobe Firefly production surface | Current Firefly help exposes reference-image composition/style controls, Precision Flow beta, text-to-vector, Style Kits, custom models, Boards, and enterprise Creative Production batch workflows | Use Adobe when licensed/brand-controlled production and batch operations matter; keep exact typography and layout editable for an explicitly requested editable or production release | reference strength, style kit, custom model, vector vs raster, batch operation, provenance/content credentials |

These are workflow mechanisms, not new looks:

| Signal | Production mechanism | SA&BOO translation | Prompt/control variables |
|---|---|---|---|
| Figma MCP write-to-canvas and diagrams | Agent workflows can move from reading design context to creating/modifying canvas content and FigJam diagrams | Route reusable systems, tokens, diagrams, and screens to editable Figma artifacts | target node/page, variables, component reuse, screenshot QA, output destination |
| OpenAI Image API controls | Current image docs add a clearer production contract around model, size, quality, format, compression, background, masks, and partial outputs | Use documented controls from the selected current tool; do not repeat provider probes when the needed operation is already established in this session | endpoint/model, supported size, quality, output format, compression, alpha/background, latency budget |
| Adobe Firefly production stack | Boards, reference-based generation, batch production, style kits, custom models, and 3D/vector workflows support campaign systems | Use for licensed/brand-controlled batch production when the account route exists | campaign matrix, reference strength, style kit, brand lock, vector/raster path, bulk resize/reframe |

Choose the route for the requested stage: an image request reaches one inspectable
standard-resolution preview with exact-copy and supplied-identity checks. Add
variants, editable reconstruction, native layout, or export QA only when requested
or required by the actual deliverable. Use the actual call and necessary readback
as capability proof; add checks when account, backend, permissions, or function
changes. Select the preview before any explicitly requested 2K/4K upgrade.

## Canva-like trend mechanisms

| Trend shorthand | Visual mechanism | SA&BOO translation | Prompt variables |
|---|---|---|---|
| Reality Warp | Liminal, uncanny, surreal editorial, distorted filters | Controlled dreamlike luxury; impossible but composed | liminal corridor, surreal reflection, lens distortion, dream haze, editorial lighting |
| Prompt Playground | Retro-tech UI, spreadsheets/code/dropdowns as visuals, lo-fi computing | Turn interface fragments into aesthetic symbols | old UI windows, data grid, cursor, dropdown, monochrome CRT, playful code blocks |
| Explorecore | Calm discovery, simple layouts, serif, slow reading | Quiet editorial exploration; premium knowledge space | clean serif, map fragments, open margins, field notes, soft off-white paper |
| Texture Check | Glass, wax, translucency, hyper-real tactile surfaces | Material-first prompt architecture | liquid glass, waxy surface, frosted acrylic, macro texture, specular highlight |
| Notes App Chic | Scrapbook, camera roll, rough notes, unfinished collage | Personal IP authenticity without cheap clutter | phone notes, torn paper, hand-cut edges, candid snapshots, marker circles |
| Opt-Out Era | Paired-back palette, serif, structured editorial, anti-cute | Low-noise luxury, quiet authority | monochrome, serif logotype, strict grid, negative space, restrained logo |
| Drama Club | Cinematic glam, stage light, curtain, bold type | High-drama but art-directed proposals/social covers | spotlight, velvet curtain, film still, high contrast, theatrical shadow |
| GrannyWave | Heritage craft, handloom, festival saturation, layered nostalgia | Modern craft revival for East-West decorative language | handloom texture, folk pattern, saturated festival palette, ornamental border |
| Zinegeist | DIY zine, anti-gloss, brutal type, collage | Raw editorial critique / campaign energy | photocopy grain, cut-and-paste, oversized type, black ink, torn edges |
| Block Party | Local symbols, vintage hues, folklore, warm everyday nostalgia | Community-rooted brand storytelling | vintage color wash, local motif, tiled pattern, warm sunlight, street-festival rhythm |

## Adobe trend mechanisms

| Adobe lens | Visual mechanism | Prompt translation |
|---|---|---|
| Multisensory visual | More than sight: tactile/taste/sound implied through depth and detail | describe surface, density, temperature, weight, scent/taste metaphor, macro detail |
| Emotional connection | Shared joy, affection, universal human moment | build a scene around gesture, gaze, ritual, small detail, cinematic payoff |
| Delightfully unhinged | Surreal humor, playful impossibility, AI not forced to mimic reality | bend physics, improbable object pairings, humorous scale, controlled absurdity |
| Local authenticity | Regional craft and community voice | specific craft, local material, real context, human presence, avoid generic “ethnic” styling |

## Figma/web/UI trend mechanisms

Use these when prompts need UI, websites, decks, or digital-product visuals.

- 3D/immersive: WebGL-like depth, interactive product model, AR preview, spatial hero.
- Experimental navigation: radial menu, hidden drawer, nonlinear journey, interactive map.
- Vibrant palettes: gradients, overlays, saturated accents; keep accessibility contrast.
- Bold typography: oversized headlines, layered type, scroll-animated type; add final text in Figma when exact wording matters.
- Dark mode: black/charcoal base, glow accents, high contrast, accessibility-first.
- Motion/scrollytelling: rhythm, transitions, micro interactions, cinematic sequence frames.
- Gamified design: progress bars, badges, levels, challenge cards; useful for learning/content products.
- Neumorphism/tactile UI: soft inset shadows, subtle gradients, touchable panels; test contrast.
- Retrofuturism: chrome, neon, pixel/arcade, early-web optimism.
- Maximalism/collage: density, sticker graphics, torn textures; maintain hierarchy.
- Neo-brutalism/anti-design: raw blocks, hard shadows, loud type; use selectively for rebellious brands.
- Sustainable/accessibility: optimized visuals, reduced clutter, inclusive contrast, no dark patterns.
- AI interfaces: chatbot, voice UI, progressive lead flows; use as product narrative, not just decoration.

## SA&BOO priority filters

Prioritize trends that strengthen:

1. Material atmosphere: Texture Check, multisensory, liquid glass, chrome, stone, silk, paper.
2. Editorial authority: Opt-Out Era, Explorecore, bold typography, dark luxury.
3. Emotional conversion: Drama Club, emotional connection, cinematic narrative.
4. Cultural depth: local authenticity, GrannyWave, Block Party, East-West ornament.
5. Prompt play: Reality Warp, Delightfully Unhinged, Prompt Playground for concept exploration.

Avoid overusing trends that may dilute premium positioning: chaotic zine clutter, childish UI nostalgia, generic surreal AI, unverified cultural motifs. Check exact text, supplied logos, and layout in the actual preview; repair only relevant defects. Use the supplied logo artwork intact. An editable tool is required only for the corresponding requested deliverable, and technical checks do not establish Bonnie's creative approval.
