# Bilingual Design Keyword Ontology: 3D, Typography/Logo, and IP Characters

Use this reference when a user supplies mixed design keywords and wants prompt translation, output direction, image analysis, or tool routing. The boards combine software names, visual styles, materials, production methods, mood terms, and output specifications. Normalize each term before using it.

## Contents

1. Source audit and cross-domain model
2. 3D / C4D / Blender / render vocabulary
3. Typography / logo / text-design vocabulary
4. IP character / art-toy / blind-box vocabulary
5. Sophisticated-design taste gate
6. Cross-domain prompt contracts
7. Tool and MCP routing
8. Image-analysis output

## 1. Source audit and cross-domain model

The supplied screenshots cover:

- **六、3D类（C4D / Blender / 3D 渲染）** — 3D / Cinema 4D / Blender / rendering;
- **二、字体 / Logo / 文字设计类** — typography, logo, and text design;
- **七、IP角色类（潮玩 / Q版 / 盲盒）** — IP character, designer toy, chibi, and blind-box presentation.

These are keyword briefs, not finished visual references. The text tells us what to inspect or control; it does not prove a particular image contains those properties.

Use this shared model:

| Layer | 中文 | What it controls |
|---|---|---|
| IDENTITY | 身份 / 主体 | object, logo, character, brand asset, or scene |
| FORM | 形体 / 结构 | silhouette, proportions, topology, glyph anatomy, pose |
| MATERIAL | 材质 / CMF | matte, metal, glass, acrylic, resin, PVC, ceramic, roughness |
| LIGHT | 灯光 / 光影 | source, direction, softness, reflection, shadow, volume |
| GRAPHIC | 图形 / 文字 | glyphs, logo geometry, layout, color roles, text-safe zones |
| STYLE | 风格机制 | toon, realistic, retro, cyber, handmade, minimal, ornate |
| OUTPUT | 输出与技术 | render engine, resolution, vector, file format, multi-view |
| MOOD | 气质 / 叙事 | cute, healing, premium, mysterious, playful, collectible |
| PRODUCTION | 生产 / 工具 | C4D, Blender, Illustrator, Figma, prototype, editable handoff |

A software name belongs to PRODUCTION; a material belongs to MATERIAL; a head-to-body ratio belongs to FORM; “cute” belongs to MOOD. Do not use one layer as evidence for another.

## 2. 3D / C4D / Blender / render vocabulary

### 2.1 Normalized bilingual terms

| 源词 | Preferred English | Layer | Meaning and control | Boundary |
|---|---|---|---|---|
| 3D类 | 3D / CG rendering | OUTPUT | computer-generated three-dimensional image or scene | A medium/output family, not one visual style. |
| C4D | Cinema 4D / C4D | PRODUCTION | software and workflow vocabulary | A final image rarely proves it was made in Cinema 4D. |
| Blender | Blender | PRODUCTION | 3D modeling, animation, simulation, and rendering software | Do not claim Blender-specific geometry from pixels alone. |
| 3D渲染 | 3D rendering / CG render | OUTPUT | rendered image from a 3D scene | Add camera, geometry, material, and light to make it controllable. |
| 渲染风格 | rendering language / render look | STYLE + LIGHT | combination of shading, light, camera, color, and post | Not the same as software identity. |
| 材质 | materials / CMF | MATERIAL | surface, color, finish, and material behavior | Separate physical material from a visual material cue. |
| 灯光 | lighting design / lighting setup | LIGHT | source, direction, hardness, color, and falloff | State key/fill/rim or environment; “good lighting” is not enough. |
| 建模风格 | modeling language / modeling approach | FORM | silhouette, edge treatment, proportions, topology, detail density | Do not infer topology or hidden construction from a hero render. |
| 精度 | geometric fidelity / modeling precision | FORM + OUTPUT | accuracy of shape, edge, scale, and small details | Not identical to 8K or high resolution. |
| 配色 | color palette / color system | GRADE + MATERIAL | hue, value, saturation, and role hierarchy | A sampled color is not automatically an approved brand token. |
| 质感 | surface character / tactile material quality | MATERIAL | roughness, sheen, grain, translucency, thickness, softness | Translate into visible cues rather than the adjective alone. |
| 3D卡通 | stylized 3D / toon 3D | STYLE | simplified proportions, clean shapes, cel or soft stylized shading | Specify cute, graphic, toy-like, or animation-like. |
| 写实 | realistic 3D / photoreal 3D | STYLE | plausible proportion, light, material, camera, and environment | “Realistic” does not guarantee accurate engineering or dimensions. |
| 黏土 | clay render / clay-like sculptural surface | MATERIAL + STYLE | matte, soft, hand-sculpted, claymation, or neutral clay-preview look | Clarify actual clay, clay-like material, or a clay render for form review. |
| 磨砂 | matte / frosted finish | MATERIAL | broad diffuse highlight, reduced specularity, soft reflection | Matte is not blur or low resolution. |
| 金属 | metallic material / metal finish | MATERIAL | high reflectance, environment-dependent reflections, metalness | Specify brushed, polished, anodized, chrome, or painted metal. |
| 玻璃 | glass / transparent glass material | MATERIAL | transmission, refraction, Fresnel reflection, thickness, edge highlight | Glass needs an environment and thickness cue; do not make it invisible. |
| 亚克力 | acrylic / PMMA | MATERIAL | transparent, translucent, tinted, or glossy polymer behavior | Acrylic is not generic glass; specify transparency, edge tint, and thickness. |
| 三点布光 | three-point lighting | LIGHT | key light + fill light + rim/back light | A setup vocabulary; still specify direction, ratio, and softness. |
| 反射 | reflection / reflectance | MATERIAL + LIGHT | environment or light source mirrored on a surface | Reflection needs a source/environment and material roughness. |
| 粗糙度 | roughness | MATERIAL | PBR surface parameter controlling highlight spread | Roughness alone does not define material identity. |
| OC渲染 | Octane render / Octane rendering | PRODUCTION | likely shorthand for Octane Renderer | Normalize OC to Octane only when context supports it; do not assume the software from pixels. |
| 软边缘 | beveled / rounded soft edges | FORM | bevel radius, rounded contour, softened edge highlight | It is geometry or shading, not Gaussian blur or melted edges. |
| 体积光 | volumetric lighting / light shafts | LIGHT + ATMOSPHERE | light visible through mist, dust, smoke, or participating media | A beam needs a source and medium; do not add white cones without cause. |
| PBR材质 | physically based materials / PBR shading | PRODUCTION + MATERIAL | physically inspired material parameters such as base color, roughness, metalness, IOR | PBR is a workflow, not a specific “premium” look. |
| 柔光 | soft diffused light | LIGHT | large source, soft shadow edges, gradual falloff, low glare | Do not equate soft light with low detail. |
| 高细节 | high detail / finely resolved detail | FORM + OUTPUT | controlled micro-detail, edge precision, surface information | Detail should support hierarchy; noise is not detail. |
| 8K | 8K output / high-resolution 8K | OUTPUT | output-size or resolution target | It does not improve design, material logic, or anatomy by itself. |
| 卡通质感 | cartoon-like surface character | STYLE + MATERIAL | simplified, clean, tactile, toy-like or cel-shaded finish | Choose between graphic flatness, clay toy, or polished 3D animation. |
| 极简 | minimal / minimalist | STYLE | reduced geometry, restrained palette, negative space, controlled detail | Do not leave the subject generic; minimalism needs a distinctive anchor. |

### 2.2 3D analysis and generation rules

Separate what can be seen from what can only be inferred:

- Confirmed from pixels: silhouette, camera angle, edge rounding, visible material cues, shadow direction, reflection shape, texture scale, and color hierarchy.
- Likely: PBR-like shading, three-point lighting, Octane-like glossy response, or a C4D/Blender workflow when multiple cues support it.
- Unknown from a final render: exact software, hidden topology, real dimensions, actual PBR values, polygon count, render samples, or production readiness.

A reliable 3D prompt has this order:

~~~text
subject and geometry
→ camera and composition
→ modeling language and edge treatment
→ material/CMF and roughness
→ lighting setup and environment
→ renderer/look development
→ output resolution and file needs
→ negative constraints
~~~

Do not use a keyword pile such as “C4D, Blender, Octane, PBR, 8K, high detail” without assigning roles. A sophisticated render is usually created by coherent geometry, credible light, material differentiation, restrained color, and a clear focal hierarchy.

## 3. Typography / logo / text-design vocabulary

### 3.1 Normalized bilingual terms

| 源词 | Preferred English | Layer | Meaning and control | Boundary |
|---|---|---|---|---|
| 字体 / Logo / 文字设计类 | typography, logo, and text design | GRAPHIC | type system, wordmark, symbol, layout, and text treatment | A logo system is not just a font with an effect. |
| 字体风格 | typeface style / typographic character | STYLE + GRAPHIC | overall historical, formal, and emotional character | Modern, retro, cyber, and handwritten are broad hypotheses. |
| 字形特征 | glyph anatomy / letterform features | FORM + GRAPHIC | skeleton, terminals, counters, joins, width, x-height, proportions | Analyze the actual letterforms, not only the mood. |
| 笔画质感 | stroke texture / brush behavior | FORM + MATERIAL | modulation, pressure, brush drag, roughness, ink spread, or smooth vector edge | Texture is not the same as font weight. |
| 配色 | color scheme / color roles | GRADE + GRAPHIC | primary, secondary, accent, contrast, background, and reproduction behavior | Keep identity colors separate from metallic/glow effects. |
| 排版 | typesetting / layout / composition | GRAPHIC | alignment, spacing, scale, hierarchy, lockup, and negative space | Exact text hierarchy must be tested at the delivery size. |
| 特效 | text treatment / graphic effects | GRAPHIC + MATERIAL | outline, glow, gradient, extrusion, emboss, shadow, texture | Effects should support recognition; they cannot repair weak glyph anatomy. |
| 现代 | modern / contemporary type | STYLE | clean construction, restrained contrast, current proportion, rational spacing | Specify geometric, neo-grotesk, humanist, or editorial. |
| 复古 | retro / vintage-inspired type | STYLE | period-specific proportion, terminals, printing, distress, or signage logic | Name decade, region, and medium; retro is not a texture preset. |
| 赛博 | cyber / cyber-tech typography | STYLE | modular cuts, digital grid, techno terminals, controlled distortion | Avoid unreadable random cuts and generic neon. |
| 手写 | handwritten / script / brush-lettered | STYLE + FORM | personal gesture, pressure, rhythm, irregularity, connected or separated strokes | Specify marker, brush, calligraphic, casual, or refined script. |
| 粗细 | weight / stroke thickness | FORM | thin, regular, medium, bold, black, monoline, or modulated weight | Weight is not the same as outline thickness or extrusion depth. |
| 衬线 | serif | FORM | bracketed, unbracketed, wedge, slab, hairline, or contrast serif | A serif family needs anatomy and proportion, not just “classical.” |
| 无衬线 | sans serif | FORM | geometric, grotesque, humanist, neo-grotesk, or rounded sans | Sans does not automatically mean modern or minimal. |
| 倒角 | bevel / chamfer | MATERIAL + 3D | angled edge catching light on a glyph or logo | Use subtle bevel for legibility; over-bevel makes type look toy-like. |
| 立体效果 | 3D extrusion / dimensional type | MATERIAL + 3D | depth, extrusion, cast shadow, perspective, or emboss | Separate physical extrusion from a fake drop shadow. |
| 光泽 | gloss / specular highlight | MATERIAL + LIGHT | tight or broad highlight caused by surface reflectance | Gloss is a surface treatment, not a typeface style. |
| 金属 | metallic type treatment | MATERIAL | metal reflectance, anisotropy, brushed or polished finish | Specify metal and lighting; metallic font alone produces cliché chrome. |
| 磨砂 | matte / frosted type treatment | MATERIAL | diffuse, low-glare, powdery, sandblasted, or frosted surface | Preserve edge clarity and contrast. |
| 玻璃质感 | glass-like / translucent glass treatment | MATERIAL | transmission, refraction, internal tint, edge reflection, thickness | Keep glyph silhouette readable; transparent type needs a controlled background. |
| 描边 | outline / stroke | GRAPHIC | contour around a glyph or logo | State inside/outside/center alignment and weight. |
| 发光 | glow / luminous treatment | LIGHT + GRAPHIC | local emission, halo, bloom, or rim light | Use one effect hierarchy; do not turn every edge into a neon border. |
| 渐变 | gradient | GRADE + GRAPHIC | linear, radial, conic, mesh, or material-driven color transition | State direction, stops, contrast, and print/web destination. |
| 浮雕 | emboss / deboss / relief | MATERIAL + GRAPHIC | raised or recessed physical impression with directional shadow | Distinguish true relief from a flat bevel filter. |
| 构图比例 | composition and proportion | GRAPHIC | symbol-to-wordmark ratio, margins, optical balance, clear space | Mechanical centering is not optical balance. |
| 可复制提示词 | reusable prompt template | OUTPUT | variable-driven prompt with slots and locked constraints | A prompt is not final artwork or a vector master. |

### 3.2 Typography/logo analysis gate

Analyze three separate axes:

1. **Glyph anatomy:** skeleton, width, terminals, counters, stroke modulation, serif/sans logic, rhythm, and legibility.
2. **Surface treatment:** bevel, metal, matte, glass, outline, glow, gradient, emboss, shadow, and texture.
3. **Identity and application system:** symbol geometry, wordmark lockup, clear space, small-size behavior, monochrome/reverse use, color roles, and editable output.

Do not let a surface effect hide a weak wordmark. Exact Chinese or English text is often unreliable in image models. Use generation for visual hypotheses, then set final type and logo geometry in Illustrator, Figma, PPT, or another vector-capable editor.

## 4. IP character / art-toy / blind-box vocabulary

### 4.1 Normalized bilingual terms

| 源词 | Preferred English | Layer | Meaning and control | Boundary |
|---|---|---|---|---|
| IP角色类 | character IP / character-brand design | IDENTITY | repeatable character identity with visual and narrative anchors | IP is a system, not one isolated render. |
| 潮玩 | designer toy / art toy / collectible toy | STYLE + PRODUCTION | collectible object culture, authored form, material, edition, and display value | Trendy toy is less precise; use art toy or designer toy. |
| Q版 | chibi / super-deformed (SD) | FORM + MOOD | enlarged head, reduced body, simplified anatomy, expressive face | Define head-to-body ratio; cute alone is not enough. |
| 盲盒风格 | blind-box collectible aesthetic / blind-box presentation | OUTPUT + PRODUCTION | collectible scale, toy-like finish, packaging/series logic, surprise-box context | Blind box is a product/presentation format, not a complete visual style. |
| 形象设定 | character design / character bible | IDENTITY | identity anchors, personality, silhouette, costume, palette, behavior, and variants | A single prompt cannot replace a character bible. |
| 风格类型 | style archetype / character visual language | STYLE | chibi, toy-like, healing, Chinese-inspired, clay, cartoon, etc. | Use one primary style and name secondary mechanisms. |
| 五官表情 | facial features and expression | FORM + MOOD | eye shape, brow, mouth, blush, gaze, asymmetry, affect | Preserve expression anchors across views. |
| 体型比例 | body proportions / body ratio | FORM | head-to-body ratio, limb length, torso width, hand/foot scale | Lock proportions before changing costume or material. |
| 服饰 | costume / clothing | IDENTITY + FORM | silhouette, layers, closures, materials, culture, and function | Do not use costume to hide an unresolved body shape. |
| 配色 | character palette / colorway | GRADE + IDENTITY | main color, secondary, accent, skin/material neutral, background separation | Keep signature color anchors stable in variants. |
| 材质 | toy material / surface material | MATERIAL | matte, resin, PVC, ceramic, clay, painted vinyl, flocking | Material affects reflectance, edge, weight, and production plausibility. |
| 光影 | character lighting / shading | LIGHT | soft key, rim, contact shadow, studio light, environment | Soft light does not remove volume or contact with the ground. |
| 细节特征 | signature details / identity cues | IDENTITY | emblem, ear shape, eye mark, accessory, seam, color patch, texture | Use a minimum set of repeatable anchors, not random decoration. |
| 治愈 | soothing / comforting / cozy aesthetic | MOOD | gentle expression, soft palette, tactile material, calm pose, safe spacing | Mood must become visible behavior; do not default to pastel overload. |
| 国风 | Chinese-inspired / Chinese cultural visual language | STYLE + TRADITION | specified regional, historical, material, or symbolic references | Avoid generic red-gold, dragons, clouds, and random ancient motifs. |
| 黏土 | clay-like / hand-sculpted clay surface | MATERIAL + STYLE | matte soft volume, finger/hand marks, sculptural simplicity | Distinguish claymation, ceramic, and clay-render preview. |
| 卡通 | cartoon / toon character | STYLE | simplified anatomy, graphic contour, expressive gesture, stylized shading | Specify editorial, animation, toy, or comic treatment. |
| 头身比 | head-to-body ratio | FORM | exact or approximate proportion such as 2.5-head or 3-head chibi | Do not leave ratio implicit when consistency matters. |
| 发型 | hairstyle | IDENTITY + FORM | silhouette, fringe, volume, parting, curl, accessory, color | Hair is a character anchor and must remain consistent across views. |
| 服饰装饰 | costume and accessories | IDENTITY + FORM | trims, badges, jewelry, props, closures, motifs, and attachment | State what is permanent identity versus optional variant. |
| 神态 | affect / facial demeanor | MOOD | calm, curious, mischievous, sleepy, proud, shy, healing | Translate into eyes, mouth, brow, gaze, and posture. |
| 动作姿态 | pose and gesture | FORM + MOOD | stance, balance, limb direction, hand action, body rhythm | A pose should support personality and product display. |
| 哑光 | matte finish | MATERIAL | diffuse reflection, low glare, soft color response | Do not flatten every surface into a gray matte blob. |
| 树脂 | resin | MATERIAL + PRODUCTION | cast resin, painted resin, translucent or opaque resin | State whether it is a visual cue or production proposal. |
| PVC | PVC toy material / vinyl figure material | MATERIAL + PRODUCTION | smooth molded vinyl, semi-matte or glossy toy response | Avoid claiming actual material without product evidence. |
| 陶瓷 | ceramic / porcelain finish | MATERIAL | hard glazed or unglazed surface, weight, brittle edge behavior | Ceramic is not synonymous with matte clay. |
| 全身造型 | full-body character view | OUTPUT | complete head-to-foot silhouette with feet, costume, and proportions visible | Do not crop away the identity anchors. |
| 纯色背景 | solid-color background | OUTPUT + COMPOSITION | neutral or brand-color studio backdrop with clear silhouette separation | Choose a color that preserves edge contrast; white is not always best. |
| 可爱 | cute / endearing | MOOD | proportion, gaze, gesture, scale, softness, and rhythm that create affection | Cute is an effect; specify the mechanisms. |

### 4.2 IP character analysis and generation rules

A reusable character prompt must lock:

~~~text
identity anchor and character role
→ silhouette and head-to-body ratio
→ face and expression
→ hairstyle and costume
→ signature accessory or mark
→ material and surface finish
→ pose and gesture
→ lighting and ground contact
→ background and camera
→ allowed variants and prohibited drift
~~~

For multi-view consistency, keep the following invariant unless the user requests a change:

- head-to-body ratio and silhouette;
- eye spacing, mouth shape, signature mark, and hair contour;
- costume identity, key accessory, and palette anchors;
- material response and scale language;
- camera family, crop, and ground contact when comparing views.

Use art toy or designer toy for the object culture; use blind-box only when the packaging, collectible scale, series logic, or surprise-box presentation matters. Use Chinese-inspired only when the cultural source, era, region, or material language is named.

## 5. Sophisticated-design taste gate

Good taste across these fields is not maximum detail, chrome, cuteness, or technological vocabulary. Check:

- **Hierarchy:** identity and focal form remain clear before materials or effects.
- **Specificity:** broad words such as modern, cyber, healing, Chinese-inspired, premium, and cute are converted into observable decisions.
- **Material truth:** metal reflects an environment; glass transmits and refracts; matte surfaces control glare; resin/PVC/ceramic have distinct edge and weight cues.
- **Typography integrity:** glyph anatomy survives bevel, glow, gradient, emboss, or texture; exact text is handled in a vector editor when needed.
- **Character identity:** one or more signature anchors remain recognizable at thumbnail and full-body scale.
- **Restraint:** one primary style, one secondary mechanism, and one material/light treatment usually outperform keyword accumulation.
- **Scalability:** a logo works in mono and at small size; a character works across front, three-quarter, and product-display views.
- **Production honesty:** software, renderer, 8K, PBR, blind box, PVC, resin, and ceramic are labeled as process/output/material hypotheses rather than invented facts.
- **Originality and safety:** use supplied references as role-specific evidence; do not clone a recognizable living character, logo, or protected typeface treatment.
- **Editability:** separate generated raster mood from exact type, logo geometry, master artwork, and production files.

### Anti-generic firewall

Reject or rewrite prompts that rely on:

- C4D + Blender + Octane + PBR + 8K as a style pile with no visual roles;
- default chrome, neon, orange-teal, bloom, bevel, or gold accents;
- “Q版 + 盲盒 + 可爱” with no silhouette or signature feature;
- “国风” as generic red/gold, cloud, dragon, blossom, or palace decoration;
- metallic/glass text that makes letters unreadable;
- “high detail” that adds noise, micro-patterns, or random accessories;
- blind-box language when there is no collectible/product/packaging context.

## 6. Cross-domain prompt contracts

### 6.1 3D render prompt

~~~text
中文：生成一张{主体}的{3D卡通/写实/黏土}三维渲染图。锁定{轮廓/比例/相机/构图}；建模采用{圆角倒角/极简几何/高精度细节}；材质为{金属/玻璃/亚克力/磨砂/黏土}，以{粗糙度、反射、透射、厚度}表现；采用{三点布光/柔光/体积光}，主光方向为{方向}；使用{C4D/Blender/Octane/PBR-like}作为工作流提示，而非风格替代；输出{尺寸/格式/视图}。避免{材质混淆、浮空、过度反射、无依据体积光、廉价塑料感}。

English: Create a {stylized 3D / photoreal / clay-like} render of {subject}. Lock {silhouette, proportions, camera, and composition}. Use {rounded bevels / minimal geometry / high-fidelity detail}. Build {metal / glass / acrylic / matte / clay-like} materials through {roughness, reflection, transmission, and thickness}. Light with {three-point lighting / soft diffuse light / volumetric light} from {direction}. Treat {Cinema 4D / Blender / Octane / PBR-like} as workflow cues, not a substitute for visual specification. Output {size, format, and views}. Avoid {material confusion, floating parts, uncontrolled reflections, unexplained volumetrics, and cheap plastic}.
~~~

### 6.2 Typography/logo prompt

~~~text
中文：针对明确要求原创或重设计的{文字或字标}，分析并设计字形骨架、笔画粗细、衬线/无衬线、字距、比例、负空间与识别性；以{现代/复古/赛博/手写}作为主要字形气质，以{金属/磨砂/玻璃/纸张/油墨}作为独立表面处理；加入{描边/渐变/发光/倒角/浮雕}，但保持小尺寸清晰度与可读性。已提供的品牌Logo使用原始图稿，只改变明确要求的应用方式；不得擅自重画或重构。输出可复制的中文与英文提示词，仅在明确要求可编辑或生产文件时附相应制作说明。不要把表面特效当成字体结构，不要生成随机或拼写错误的文字。

English: For explicitly requested original or redesigned {lettering or wordmark}, design the letterform skeleton, stroke weight, serif/sans logic, spacing, proportion, negative space, and recognizability. Use {modern / retro / cyber / handwritten} as the primary typographic character, and treat {metal / matte / glass / paper / ink} as a separate surface treatment. Add {outline / gradient / glow / bevel / emboss} only if small-size legibility remains intact. Use supplied brand-logo artwork intact and change only its requested application; do not redraw or reconstruct it without instruction. Return reusable Chinese and English prompts; add production instructions only for an explicitly requested editable or production deliverable. Do not confuse surface effects with letterform structure and do not invent misspelled text.
~~~

### 6.3 IP character prompt

~~~text
中文：设计一个原创{潮玩/治愈/国风/黏土/卡通}IP角色，全身可见，头身比{比例}，轮廓以{形体锚点}为核心；五官与神态为{表达}，发型为{形状/颜色}，服饰与配件为{设计}，保留{签名细节}；材质为{哑光树脂/PVC/陶瓷/黏土质感}，采用{柔光/三点布光}，纯色背景，接地阴影自然；输出正面与四分之三视图，锁定比例、面部、服装与配色。避免随机配件、品牌抄袭、肢体变形、漂浮、过度复杂和泛化“国风”。

English: Design an original full-body {designer-toy / comforting / Chinese-inspired / clay-like / cartoon} character IP. Lock a {ratio}-head-to-body proportion and a silhouette built around {identity anchor}. Give it {expression}, a {hairstyle}, {costume and accessories}, and the signature detail {anchor}. Use {matte resin / PVC vinyl / ceramic / clay-like} material with {soft / three-point} lighting, a solid-color background, and credible ground contact. Output front and three-quarter views while preserving proportions, face, costume, and palette. Avoid random accessories, recognizable IP imitation, distorted limbs, floating objects, over-complexity, and generic “Chinese style.”
~~~

## 7. Tool and MCP routing

The 2026-08-04 capability snapshot is historical, not current availability.
Use relevant capabilities exposed in this session within the task's authorization.
The actual task result and necessary readback or rendered inspection establish
scoped proof; do not add a separate probe for every call. Recheck when account,
backend, permissions, or required function changes, or actual execution fails.
Preserve the intended account/file, tool prerequisites, and permission boundaries.

### Minimum route by goal

| Goal | Route | Current gate |
|---|---|---|
| Translate or analyze these keywords | visual-style prompt lab + visual-reasoning critic | No new MCP required. |
| Generate a 3D concept image | concise prompt → current applicable image tool → inspect standard-resolution preview | Actual result proves that operation; upgrade only after selection and an explicit request. |
| Exact typography or supplied logo in an image | compose real copy and original logo artwork with the visual; repair local defects if needed | Check actual words, glyphs, logo identity, count, and unchanged regions; no default vector rebuild. |
| Explicit editable/production typography or logo artwork | current applicable vector-capable editor → inspect actual artwork/export | Preserve supplied identity; verify real copy and contours within the requested stage. |
| Editable social/brand layout | current applicable layout connector → inspect actual layout/export | Intended account/file and granted write scope; no availability claim from this dated snapshot. |
| Actual C4D/Blender scene or .blend/.c4d file | current native C4D/Blender app or explicitly connected bridge | Use a real exposed native capability; a prompt does not create native scene files. |
| IP character multi-view consistency | prompt lab + visual critic + multi-view consistency workflow | Lock identity anchors and use reference-role mapping. |
| Physical toy development | product-design partner + CAD/material/prototype owner | Render is a hypothesis; do not infer manufacturing or safety from it. |

MCP decision:

- For vocabulary translation, image analysis, and prompt architecture: **no additional MCP is needed**.
- For an explicitly requested editable logo/type deliverable, use a currently
  applicable vector-capable route. For tool selection and proof, follow
  [mcp-tool-routing.md](mcp-tool-routing.md); do not repeat a separate diagnostic.
- Use a native 3D bridge only when editable scene files, modifiers, materials,
  cameras, or render settings are requested. It is unnecessary for prompt
  translation, a raster concept, or image critique.
- Never install a plugin or expose client assets merely because a keyword mentions
  a software name. Preserve granted write scope and data destination; obtain
  required authorization for a new connection or expanded external action.

## 8. Image-analysis output

Pair with the visual-reasoning critic. Use evidence classes and local confidence:

~~~text
分析范围 / Scope:
主体与身份 / Subject and identity:
形体与比例 / Form and proportions:
材质与工艺 / Material and process:
灯光与相机 / Lighting and camera:
图形与文字 / Graphic and typography:
风格机制 / Style mechanism:
软件/工具线索 / Software or tool cues:
可见事实 / Visible facts:
有依据的推断 / Supported inferences:
未知 / Unknown:
审美判断 / Taste judgment:
最小修改或提示词 / Smallest change or prompt:
输出与工具路线 / Output and tool route:
~~~

Never state “made in C4D,” “made in Blender,” “PBR,” “Octane,” “PVC,” “resin,” or “ceramic” as confirmed from a screenshot unless the source or metadata proves it. Use “呈现出……视觉线索 / shows visual cues consistent with…” when evidence is visual only.
