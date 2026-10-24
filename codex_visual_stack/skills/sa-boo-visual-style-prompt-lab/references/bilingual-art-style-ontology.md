# Bilingual Art-Style Ontology and Taste Gate

Use this reference to translate, normalize, identify, compare, mix, or generate art styles in Chinese and English. Treat it as controlled vocabulary, not as a claim that every source label is a canonical art-historical movement. When a style brief also specifies color tone, lighting, filters, or optical effects, pair it with `bilingual-tone-lighting-ontology.md` and keep those controls in a separate light stack.

## Contents

1. Source audit
2. Classification model
3. Recognition and translation protocol
4. Bilingual normalization table
5. Critical distinctions
6. Taste and style-mixing gate
7. Generation translation
8. Analysis output

## 1. Source audit

The supplied reference image contains 60 bullets in three columns. It has 59 unique labels because `浪漫油画风格` appears twice, at entries 12 and 60.

The list mixes several different kinds of language:

- named movements or lineages, such as `印象派 / Impressionism`;
- cultural traditions, such as `传统水墨 / traditional Chinese ink wash`;
- media or processes, such as `水彩画 / watercolor painting`;
- formats or disciplines, such as `平面设计 / graphic design`;
- genres or worldbuilding systems, such as `赛博朋克 / cyberpunk`;
- visual mechanisms, such as `霓虹 / neon lighting`;
- moods or finish levels, such as `精致细腻 / refined and finely detailed`;
- ambiguous, non-canonical labels, such as `野性艺术 / raw or wild art aesthetic`.

Do not compare or combine these as if they occupy the same level. A useful prompt or diagnosis assigns each label a role.

## 2. Classification model

Use one primary class for normalization and add secondary roles only when useful.

| Class | 中文 | Meaning |
|---|---|---|
| `LINEAGE` | 艺术运动 / 谱系 | Historically or critically recognized movement, school, or broad lineage |
| `TRADITION` | 文化传统 | Culture-, place-, or practice-specific visual tradition |
| `MEDIUM` | 媒介 / 工艺 | Material, mark-making, production, or rendering process |
| `FORMAT` | 形式 / 学科 | Output form, discipline, or spatial mode |
| `GENRE` | 类型 / 世界观 | Subject-world, narrative, or speculative setting |
| `MECHANISM` | 视觉机制 | Composition, light, geometry, palette, rhythm, or surface behavior |
| `MOOD` | 气质 / 完成度 | Emotional tone, market positioning, or finish quality |
| `AMBIGUOUS` | 歧义标签 | Label whose intended meaning must be clarified from pixels or brief |
| `DUPLICATE` | 重复项 | Source-audit marker; deduplicate before building a reusable vocabulary |

## 3. Recognition and translation protocol

1. Inspect the actual pixels or bind the written brief. Do not diagnose style from a filename or keyword list alone.
2. Separate six layers: lineage/tradition, medium/process, format, genre/worldbuilding, mechanism, and mood/finish.
3. Collect evidence from at least two independent cue groups before asserting a named style:
   - composition and spatial organization;
   - shape, contour, proportion, and perspective;
   - mark-making, surface, material, or production cues;
   - light, value, palette, and edge behavior;
   - iconography, subject, typography, or period detail.
4. Name the primary candidate, nearest alternatives, contradictory evidence, and local confidence.
5. Translate the visual mechanism, not only the noun. Keep established movement names capitalized in English.
6. For generation, assign one role to each style component. Use a hierarchy, not a pile of synonyms.

Subject matter is weak evidence by itself. A robot is not automatically cyberpunk; a palace is not automatically Baroque; a red palette is not automatically revolutionary art; rough marks are not automatically Art Brut; and visible brush texture is not automatically oil paint.

## 4. Bilingual normalization table

### Source column 1 — entries 1–20

| # | 源标签 | Preferred English | Class | 可见与生成机制 / Visible and generative mechanism | Boundary |
|---:|---|---|---|---|---|
| 1 | 卡通风格 | Cartoon / toon illustration | `FORMAT` | 简化轮廓、形体夸张、平涂或赛璐璐明暗 / simplified contours, exaggerated proportions, flat or cel shading | Specify 2D, editorial, comic, or 3D-toon; “cartoon” alone is broad. |
| 2 | 现实主义风格 | Realism | `LINEAGE` | 可信比例、连贯透视、可验证光材逻辑、克制理想化 / credible proportion, coherent perspective, plausible light and material, restrained idealization | Not identical to photorealism; may refer to a movement or a general representational mode. |
| 3 | 水彩画风格 | Watercolor painting | `MEDIUM` | 透明罩染、水痕与晕染、纸纹、软硬边交替 / transparent washes, blooms and bleeds, paper grain, varied edges | Avoid simultaneously demanding fully opaque airbrushed surfaces unless deliberately hybrid. |
| 4 | 黑白电影风格 | Black-and-white cinema aesthetic | `FORMAT` | 灰阶层级、电影布光、胶片颗粒、时代化镜头与构图 / grayscale hierarchy, cinematic lighting, film grain, period-aware framing | A monochrome filter alone does not create cinematic language. |
| 5 | 赛博朋克风格 | Cyberpunk | `GENRE` | 高科技与低生活并置、暗部霓虹、潮湿反射、密集城市层级 / high tech versus low life, dark neon, wet reflections, dense urban layers | Neon robots alone are insufficient; social and spatial worldbuilding matters. |
| 6 | 抽象艺术风格 | Abstract art | `LINEAGE` | 以形、色、线、肌理、动作取代再现叙事 / form, color, line, texture, and gesture over representation | Specify geometric, lyrical, gestural, color-field, or another subtype. |
| 7 | 印象派风格 | Impressionism | `LINEAGE` | 断续笔触、综合色、瞬时自然光、轮廓软化 / broken brushwork, optical color mixing, transient natural light, softened contours | Do not reduce to “blurry pastel painting.” |
| 8 | 未来主义风格 | Futurism | `LINEAGE` | 斜向力线、重复轮廓、同时性、机械时代速度 / diagonals, repeated contours, simultaneity, machine-age speed | Historical Futurism is not the same as the adjective “futuristic.” |
| 9 | 油画风格 | Oil painting | `MEDIUM` | 罩染或厚涂、颜料体积、画布纹理、可见笔触 / glazing or impasto, pigment body, canvas texture, visible brushwork | Add a lineage, subject, and edge treatment; the medium is not a complete style. |
| 10 | 现代简约风格 | Modern minimalist design | `MECHANISM` | 减少形体与色彩、功能清晰、留白充足、细节收束 / reduced forms and palette, functional clarity, generous space, controlled detailing | A contemporary design language, distinct from historical/conceptual Minimalism. |
| 11 | 浪漫主义风格 | Romanticism | `LINEAGE` | 崇高自然、情绪尺度、戏剧光线、废墟风暴与个体经验 / sublime nature, emotional scale, dramatic light, ruins, storms, individual experience | Not simply “romantic,” pretty, floral, or sentimental. |
| 12 | 浪漫油画风格 | Romantic oil-painting aesthetic | `MOOD` + `MEDIUM` | 抒情光线、柔和边缘、暖冷过渡、油画层次 / lyrical light, soft edges, warm-cool transitions, layered oil-paint handling | A hybrid mood-medium label, not a canonical movement; entry 60 duplicates it. |
| 13 | 超现实主义风格 | Surrealism | `LINEAGE` | 可信描绘与不可能并置、梦逻辑、尺度错位、陌生化 / credible rendering plus impossible juxtapositions, dream logic, scale shifts, defamiliarization | Random fantasy clutter is not automatically Surrealist. |
| 14 | 装饰艺术风格 | Art Deco / decorative arts | `AMBIGUOUS` | 若指 Art Deco：几何对称、阶梯形、放射纹、黑金漆面；若泛指装饰艺术：以工艺与饰面为主 / if Art Deco: geometric symmetry, stepped forms, sunbursts, lacquer and metal; if decorative arts: object craft and ornament | Confirm whether the intended term is the 1920s–30s movement or decorative art broadly. |
| 15 | 低调写实风格 | Understated realism / low-key realism | `AMBIGUOUS` | 克制色彩与叙事，或低调布光下的写实形体 / restrained palette and narrative, or realistic form under low-key lighting | Clarify whether `低调` means understated or photographic low-key lighting. |
| 16 | 超现代风格 | Ultramodern aesthetic | `MOOD` | 单体化几何、无缝细节、先进材料、受控光带 / monolithic geometry, seamless detailing, advanced materials, controlled light strips | A broad market adjective; specify architecture, product, graphic, or fashion context. |
| 17 | 复古风格 | Retro / vintage aesthetic | `MOOD` | 特定年代的配色、字形、印刷或胶片痕迹 / era-specific palette, typography, print, or film wear | Always specify decade and place; retro recreation differs from authentic vintage material. |
| 18 | 朋克风格 | Punk aesthetic | `GENRE` | DIY 拼贴、磨损肌理、剪贴字、反精修与高反差 / DIY collage, distressed texture, cut-and-paste type, anti-polish, high contrast | Distinguish punk, post-punk, cyberpunk, and generic grunge. |
| 19 | 动感插画风格 | Dynamic illustration | `MECHANISM` | 斜线、透视缩短、动作裁切、速度线与节奏重复 / diagonals, foreshortening, action crops, motion lines, rhythmic repetition | Implied motion in a still, not Kinetic Art as a physical movement-based practice. |
| 20 | 幻想风格 | Fantasy art | `GENRE` | 神话生物、魔法因果、异世界环境与象征光线 / mythic creatures, magical causality, invented worlds, symbolic light | Specify high fantasy, dark fantasy, fairy tale, mythic, or another subgenre. |

### Source column 2 — entries 21–40

| # | 源标签 | Preferred English | Class | 可见与生成机制 / Visible and generative mechanism | Boundary |
|---:|---|---|---|---|---|
| 21 | 巴洛克艺术风格 | Baroque | `LINEAGE` | 强对角线、明暗戏剧、空间纵深、动态身体与繁复材质 / strong diagonals, dramatic chiaroscuro, deep space, dynamic bodies, rich material | Grandeur or gold alone is not enough. |
| 22 | 平面设计风格 | Graphic-design language | `FORMAT` | 网格、字图层级、矢量形、留白、色彩系统与交付尺寸 / grid, type-image hierarchy, vector form, negative space, color system, delivery format | A discipline, not one style; specify poster, editorial, identity, social, or information design. |
| 23 | 写实油画风格 | Realist oil painting | `MEDIUM` + `LINEAGE` | 观察性造型与可信光材，加上油画罩染或笔触 / observed form and plausible light/material with oil glazing or brushwork | Distinguish from photoreal digital painting and academic idealization. |
| 24 | 光影摄影风格 | Light-and-shadow / chiaroscuro photography | `MECHANISM` | 侧光或逆光、负补光、剪影、掠射肌理、受控高光 / side or back light, negative fill, silhouettes, raking texture, controlled highlights | Use “chiaroscuro” only when tonal drama and modeling support it. |
| 25 | 赛博奇幻风格 | Cyber fantasy | `GENRE` | 奇幻生物与符号结合义体、全息、霓虹、数字魔法 / fantasy beings and symbols combined with cybernetics, holograms, neon, digital magic | Assign which system controls worldbuilding; otherwise it becomes incoherent style soup. |
| 26 | 动态艺术风格 | Kinetic art / dynamic art | `AMBIGUOUS` | 若指 Kinetic Art：真实或光学运动、序列模块、平衡机构；若泛指动态感：节奏与方向 / if Kinetic Art: real or optical motion, serial modules, balancing mechanisms; if generic dynamism: rhythm and direction | Confirm whether the work physically moves or merely depicts motion. |
| 27 | 简约插画风格 | Minimalist illustration | `FORMAT` | 少量线面、有限配色、符号化主体、主动留白 / few lines and shapes, limited palette, symbolic subject, deliberate negative space | Not automatically Minimalism as an art movement. |
| 28 | 高光油画风格 | Luminous / highlight-rich oil painting | `AMBIGUOUS` | 发光般亮部、罩染深度、受控镜面高光、明暗焦点 / luminous highlights, glazing depth, controlled specular accents, value focus | Not a standard art-historical term; clarify high-key painting versus glossy highlights. |
| 29 | 科幻风格 | Science-fiction art | `GENRE` | 推演技术、陌生环境、尺度对比与世界规则 / speculative technology, unfamiliar environments, scale contrast, coherent world rules | Specify hard sci-fi, space opera, retrofuturism, biotech, utopian, or dystopian. |
| 30 | 新古典风格 | Neoclassicism / Neoclassical | `LINEAGE` | 平衡几何、古典题材、清晰轮廓、克制色彩与秩序 / balanced geometry, classical subject, clean contours, restrained palette, order | Distinguish the historical movement from contemporary “new classic” interiors. |
| 31 | 迷幻艺术风格 | Psychedelic art | `LINEAGE` | 高饱和互补色、流体有机形、扭曲字形、光学重复 / saturated complementary color, fluid organic forms, warped type, optical repetition | Visual intensity should remain structured; random rainbow noise is not enough. |
| 32 | 艺术装置风格 | Installation art | `FORMAT` | 场地特定、观者尺度与路径、物体关系、时间或互动 / site specificity, viewer scale and path, object relations, time or interaction | Not simply a sculpture photographed in a room. |
| 33 | 精致细腻风格 | Refined, finely detailed finish | `MOOD` | 精确边缘、微观肌理、受控复杂度、无随意噪声 / precise edges, microtexture, controlled complexity, no accidental noise | A finish level, not a lineage; detail density alone does not equal taste. |
| 34 | 高科技风格 | High-tech aesthetic | `MECHANISM` | 玻璃金属复材、模块网格、显露技术、发光界面、精密节点 / glass, metal, composites, modular grids, exposed technology, luminous interfaces, precise joints | Clarify consumer-tech imagery versus High-Tech architecture. |
| 35 | 华丽装饰风格 | Ornate / opulent decorative aesthetic | `MOOD` | 高密度但有秩序的纹样、层叠材质、对称或节奏 / dense but ordered ornament, layered materials, symmetry or rhythm | Opulence is not permission for indiscriminate clutter. |
| 36 | 现代工业风格 | Modern industrial aesthetic | `MECHANISM` | 外露结构、钢混材质、功能节点、中性色、厂房尺度 / exposed structure, steel and concrete, functional joints, neutral palette, factory scale | Distinguish honest construction logic from decorative “industrial” props. |
| 37 | 传统艺术风格 | Traditional art | `AMBIGUOUS` | 必须指定文化、时期、媒介、图像制度与工艺 / specify culture, period, medium, iconographic system, and craft | There is no universal traditional-art look. |
| 38 | 数字艺术风格 | Digital art | `MEDIUM` | 数字绘制、合成、矢量、3D 或生成流程的可控痕迹 / digitally painted, composited, vector, 3D, or generative production cues | A medium/domain; specify the rendering and finish. |
| 39 | 未来城市风格 | Futuristic cityscape | `GENRE` | 巨构、分层交通、发光导视、空气透视与尺度参照 / megastructures, layered transit, luminous wayfinding, atmospheric depth, scale references | Futuristic subject matter does not equal historical Futurism. |
| 40 | 白描艺术风格 | Chinese baimiao line drawing | `TRADITION` + `MEDIUM` | 单色控制线、线重变化、少或无明暗洗染、以线造型 / controlled monochrome contour, varied line weight, little or no tonal wash, form built by line | Preserve its Chinese line discipline; do not collapse it into generic vector outline art. |

### Source column 3 — entries 41–60

| # | 源标签 | Preferred English | Class | 可见与生成机制 / Visible and generative mechanism | Boundary |
|---:|---|---|---|---|---|
| 41 | 传统水墨风格 | Traditional Chinese ink-wash painting | `TRADITION` + `MEDIUM` | 墨色层次、干湿笔、渗化、飞白、留白与诗性空间 / ink-value gradation, dry and wet brush, diffusion, flying white, reserve white, poetic space | Do not translate merely as “black watercolor.” |
| 42 | 洛可可风格 | Rococo | `LINEAGE` | 不对称贝壳卷草、粉彩、鎏金、轻盈私密与精巧装饰 / asymmetric shell scrolls, pastel, gilding, playful intimacy, delicate ornament | Distinguish from Baroque scale/drama and from generic floral luxury. |
| 43 | 民族风格 | Culture-specific folk / vernacular style | `AMBIGUOUS` | 指定地域、族群、材料、纹样语法、象征与制作方式 / specify place, community, material, motif grammar, symbolism, and making method | Avoid a generic “ethnic” collage or invented sacred motifs. |
| 44 | 3D动画风格 | 3D animation | `MEDIUM` + `FORMAT` | 建模体积、材质与灯光一致、镜头 staging、绑定或运动逻辑 / modeled volume, coherent materials and lighting, camera staging, rigging or motion logic | Specify stylized, toon, stop-motion-like, or photoreal rendering. |
| 45 | 水墨插画风格 | Ink-wash illustration | `MEDIUM` + `FORMAT` | 水墨渗化与干笔结合清晰叙事、现代构图或平面层级 / ink diffusion and dry brush combined with illustrative clarity and contemporary composition | More illustration-led than traditional ink painting; state what is modernized. |
| 46 | 手工艺风格 | Craft / handcrafted aesthetic | `MEDIUM` | 可见手痕、缝线或榫接、印刷偏差、真实材料边缘 / visible hand marks, stitching or joinery, print irregularity, authentic material edges | Name the actual process: embroidery, carving, weaving, paper cutting, ceramics, etc. |
| 47 | 野性艺术风格 | Raw / wild art aesthetic | `AMBIGUOUS` | 粗粝表面、强烈动作痕迹、不规则形与原始张力 / rough surfaces, forceful gesture, irregular form, raw tension | Non-canonical label; clarify Fauvism, Art Brut, Neo-Expressionism, or simply untamed energy. |
| 48 | 科幻黑白风格 | Monochrome science-fiction aesthetic | `GENRE` + `MECHANISM` | 灰阶推演世界、强轮廓、金属肌理、雾与胶片颗粒 / grayscale speculative world, strong silhouettes, metallic texture, haze, film grain | Combine sci-fi world rules with a real value hierarchy; do not just desaturate. |
| 49 | 机械风格 | Mechanical / machine aesthetic | `MECHANISM` | 齿轮、关节、活塞、面板、重复模块与可解释装配 / gears, joints, pistons, panels, repeated modules, explainable assembly | Decide whether mechanics must be functional or may be decorative greebling. |
| 50 | 自然主义风格 | Naturalism | `LINEAGE` | 环境与生物细节、普通生活、非理想化观察、因果可信 / environmental and biological specificity, ordinary life, non-idealized observation, credible causality | Overlaps Realism but often emphasizes empirical observation and environment. |
| 51 | 乡村田园风格 | Rustic pastoral / country aesthetic | `GENRE` | 天然材料、风化痕迹、乡野景观、暖日光、手作物件与慢节奏 / natural materials, weathering, rural landscape, warm daylight, handmade objects, slower rhythm | Specify region and era; avoid generic farmhouse kitsch. |
| 52 | 抽象构成风格 | Abstract composition / formalist abstraction | `MECHANISM` | 体块、线、色与负空间的平衡、节奏、张力和比例 / balance, rhythm, tension, and proportion among mass, line, color, and negative space | A compositional strategy; specify geometric, lyrical, Constructivist, or other logic. |
| 53 | 轻奢风格 | Contemporary understated luxury | `MOOD` | 克制的优质材质、细金属、石材或皮革、低装饰与精确收口 / restrained premium materials, subtle metal, stone or leather, low ornament, precise detailing | “Light luxury” is a Chinese market term, not an art movement; avoid generic beige-and-gold formulas. |
| 54 | 运动风格 | Sports / athletic aesthetic | `GENRE` | 运动姿态、性能材料、粗体字、对角线、速度与冲击 / athletic gesture, performance materials, bold type, diagonals, speed, impact | Specify the sport, audience, and editorial versus technical tone. |
| 55 | 霓虹风格 | Neon-light aesthetic | `MECHANISM` | 发光色、光晕、反射、暗底与受控光谱 / emissive color, bloom, reflection, dark ground, controlled spectral palette | A lighting/color treatment, not a complete genre; neon does not automatically mean cyberpunk. |
| 56 | 虚拟现实风格 | Virtual-reality / immersive digital aesthetic | `FORMAT` | 360 度空间、体积纵深、空间界面、临场感与互动线索 / 360-degree space, volumetric depth, spatial UI, presence, interaction cues | In a still image, describe representational cues rather than claiming actual interactivity. |
| 57 | 红色艺术风格 | Red-dominant art / revolutionary art | `AMBIGUOUS` | 若指色彩：红色控制价值与饱和层级；若指红色文化：需明确历史、政治图像与来源 / if color-led: control red value and saturation hierarchy; if revolutionary: specify historical and political iconography and source | Never infer political meaning from red alone. |
| 58 | 经典艺术风格 | Classical art / classic aesthetic | `AMBIGUOUS` | 若指古典：理想比例、平衡、古希腊罗马题材；若指经典：仅表示经久或典范 / if Classical: ideal proportion, balance, Greco-Roman subject; if “classic”: only enduring or canonical status | Confirm Classical, classic, academic, or traditional. |
| 59 | 极简主义风格 | Minimalism | `LINEAGE` | 观念性减法、基本几何、序列、材料在场与负空间 / conceptual reduction, essential geometry, seriality, material presence, negative space | Distinct from modern minimalist design and minimalist illustration. |
| 60 | 浪漫油画风格 | Romantic oil-painting aesthetic | `DUPLICATE` | 与 #12 相同 / same as #12 | Preserve the duplicate only when auditing the source; deduplicate in reusable vocabularies. |

## 5. Critical distinctions

### Realism cluster / 写实类

- `现实主义 / Realism`: a movement or broad representational logic based on observed, credible reality.
- `自然主义 / Naturalism`: stronger emphasis on empirical environment, ordinary life, and non-idealized causality.
- `写实油画 / realist oil painting`: Realist visual logic plus oil-paint process cues.
- `低调写实 / understated or low-key realism`: an ambiguous mood or lighting treatment applied to realistic depiction.
- `photorealism / 照相写实主义`: not present in the source list; requires photographic fidelity and should not be silently substituted for Realism.

### Minimal cluster / 简约类

- `现代简约 / modern minimalist design`: contemporary functional restraint.
- `简约插画 / minimalist illustration`: simplified illustrative format.
- `极简主义 / Minimalism`: an art/design lineage in which reduction, seriality, objecthood, or material presence is conceptually central.

### Classical European lineage / 欧洲古典谱系

- `Baroque`: scale, diagonal force, theatrical depth, dramatic light.
- `Rococo`: intimate scale, asymmetry, lightness, pastel, shell-and-scroll ornament.
- `Neoclassicism`: order, clean contour, moral or civic clarity, classical revival.
- `Classical`: Greco-Roman ideals or a broader classical canon; clarify scope.
- `Romanticism`: emotion, sublimity, nature, individual experience, and dramatic atmosphere; it is not a branch of Classical restraint.

### Future and technology cluster / 未来科技类

- `Futurism`: historical movement organized around speed, force, simultaneity, and machine-age dynamism.
- `futuristic cityscape`: an environment genre showing speculative urban futures.
- `science fiction`: a broad speculative narrative genre.
- `cyberpunk`: a specific high-tech/low-life socio-urban genre.
- `cyber fantasy`: fantasy ontology fused with cybernetic mechanisms.
- `high-tech`, `mechanical`, and `neon`: mechanisms or treatments, not complete worlds.
- `virtual reality`: an immersive format; a still can only represent its spatial-interface cues.

### Chinese ink and line cluster / 中国水墨与线描

- `传统水墨 / traditional Chinese ink wash`: ink tonality, wet-dry brush behavior, reserve white, poetic space, and tradition-specific composition.
- `水墨插画 / ink-wash illustration`: ink behavior organized for contemporary illustration and narrative clarity.
- `白描 / baimiao`: contour-led monochrome drawing with disciplined line variation and little or no tonal wash.

### Abstraction cluster / 抽象类

- `抽象艺术 / abstract art`: broad nonrepresentational or partially abstract lineage.
- `抽象构成 / abstract composition`: formal organization of mass, line, color, and negative space.
- Do not claim a subtype such as Constructivism, Suprematism, Color Field, or Abstract Expressionism unless the evidence supports it.

## 6. Taste and style-mixing gate

High taste does not mean more ornament, more realism, more detail, more luxury materials, or more style names. Approve a direction only when it passes these checks:

- **Hierarchy:** one visual logic clearly leads; secondary influences remain subordinate.
- **Coherence:** composition, mark-making, material, light, and worldbuilding do not contradict one another without intent.
- **Specificity:** era, culture, medium, genre, and output context are named where they matter.
- **Medium credibility:** watercolor behaves like watercolor; ink reserves white; oil paint has pigment body; 3D light and volume remain coherent.
- **Material credibility:** surfaces, joints, reflections, thickness, and wear support the stated object or space.
- **Restraint:** novelty is concentrated at meaningful points instead of spread as undifferentiated noise.
- **Original translation:** retain transferable principles, not recognizable compositions, motifs, or protected assets.
- **Cultural integrity:** culture-specific patterns and symbols have a stated source and role; do not fabricate a generic “ethnic” mixture.
- **Production fit:** the style supports the channel, scale, typography, editability, and delivery method.

Use this mixing grammar:

```text
primary lineage or design logic
+ subordinate mechanism
+ medium or render method
+ light or finish treatment
+ explicit exclusions
```

Good role assignment:

- `Baroque` controls diagonals and chiaroscuro; `cyberpunk` controls material and urban worldbuilding; 3D rendering controls volume.
- `Baimiao` controls line behavior; `futuristic cityscape` controls subject; off-white paper controls ground.
- `Minimalism` controls massing and negative space; `neon` appears as one restrained light accent.
- `Romanticism` controls sublime scale and atmosphere; `ink wash` controls mark-making and spatial emptiness.

Reject unresolved style soup such as “Baroque + Rococo + Minimalism + cyberpunk + watercolor + 3D animation” when no role hierarchy is assigned.

## 7. Generation translation

### Bilingual prompt spine

```text
中文：以{主风格/谱系}作为{构图、形体或叙事}主逻辑；仅用{次要机制}控制{明确变量}；以{媒介/渲染方式}表现{笔触、材质或体积}；采用{光线/色彩/完成度}。保留{主体、比例、相机、文字安全区}。避免{冲突风格、廉价套路、媒介失真、结构错误}。

English: Use {primary lineage/design logic} to control {composition, form, or narrative}. Use {secondary mechanism} only for {named variable}. Render through {medium/render method}, preserving its {mark, material, or volume behavior}. Apply {light, color, and finish}. Keep {subject, proportions, camera, and text-safe zone}. Avoid {conflicting style, cliché, medium mismatch, and structural errors}.
```

### Example — controlled hybrid

```text
中文：以巴洛克的强对角线与明暗戏剧作为构图主逻辑，以赛博朋克仅控制城市技术层、霓虹导视与潮湿反射；使用电影感 3D 渲染保持建筑尺度、材料接缝和接触阴影可信。黑青灰为主，酸性洋红只作少量焦点。避免洛可可花饰、随机齿轮、满屏霓虹、廉价塑料与无功能机械细节。

English: Use Baroque diagonals and dramatic chiaroscuro as the primary compositional logic. Let cyberpunk control only the urban technology layer, neon wayfinding, and wet reflections. Use cinematic 3D rendering with credible architectural scale, material joints, and contact shadows. Keep a black, blue-gray palette with restrained acid-magenta accents. Avoid Rococo ornament, random gears, wall-to-wall neon, cheap plastic, and nonfunctional mechanical clutter.
```

## 8. Analysis output

For image-style diagnosis, pair this reference with `sa-boo-visual-reasoning-critic` and return:

```text
分析范围 / Scope:
主要候选 / Primary candidate:
类别 / Class:
可见依据 / Visible evidence:
  composition and space:
  form and contour:
  mark, material, or process:
  light, value, and color:
  iconography, type, or period detail:
次要机制 / Secondary mechanism:
媒介与形式 / Medium and format:
近邻风格 / Nearest alternatives:
反证 / Contradictory or missing evidence:
置信度 / Local confidence:
生成转译 / Generation translation:
```

Use `confirmed`, `likely`, `possible`, or `unknown` locally. Never use a single global style-confidence score to hide contradictory evidence.
