# Bilingual Tone, Lighting, Filter, and Optical-Effect Ontology

Use this reference when a request contains color tone, grading, filters, lighting, shadows, glow, atmospheric effects, reflections, or poetic light descriptions. These labels are visually powerful, but many are descriptors rather than styles. Translate them into a controllable light stack before using them in a prompt or critique.

## Contents

1. Source audit
2. Layer model
3. Translation rules
4. Bilingual normalization table
5. Taste and visual-critique gate
6. Mixing grammar
7. Bilingual prompt spine
8. Image-analysis output

## 1. Source audit

The supplied board is titled 色调&光效风格, best translated as **Color Tone & Lighting-Effect Styles**. It contains 40 bullets in two columns and 39 unique descriptors: 神秘的紫色光辉 appears at entries 11 and 31.

The board mixes:

- global tone or grade: warm, cool, blue-violet, purple, orange, silver;
- light sources: sun, moon, lamp, fire, neon, sky, stars, water reflection;
- shadow and contrast behavior: dark, crisp, harsh-sun, firelit, glimmer in shadow;
- optical and environmental effects: bloom, halo, caustics, mist shafts, dappled light, rain-after light;
- narrative atmosphere: mysterious, dreamy, deep night, chromatic fantasy.

Do not call every item a style. A prompt becomes reliable when each term is assigned to the correct layer.

## 2. Layer model

Use this stack from broadest to most local:

~~~
scene exposure and value range
→ global color grade / palette temperature
→ key light source and direction
→ fill, rim, or reflected light
→ shadow hardness, density, and edge behavior
→ atmosphere / participating medium
→ optical effect (bloom, halo, caustic, refraction, dispersion, bokeh)
→ material response (specular, roughness, translucency, wetness)
→ camera/filter and post-processing
~~~

| Layer | 中文 | Ask |
|---|---|---|
| GRADE | 全局色调 / 调色 | Does the whole image shift in hue, value, or saturation? |
| SOURCE | 光源 | What emits or reflects the light, and from where? |
| SHADOW | 阴影 / 对比 | Are shadows hard, soft, deep, broken, colored, or moving? |
| ATMOSPHERE | 空气介质 | What makes a beam visible: mist, dust, smoke, rain, or haze? |
| OPTICAL | 光学效果 | Is the effect bloom, halo, caustic, refraction, dispersion, or bokeh? |
| SURFACE | 材质响应 | How do wet, glossy, matte, translucent, or metallic surfaces react? |
| MOOD | 叙事气氛 | What emotional reading is created after the physical cues are specified? |

## 3. Translation rules

- 色调 → **color tone**, **color grade**, or **tonal palette**. Use lighting only when a physical source is implied.
- 光晕 → **halo** when it is a localized ring or rim; **bloom** when bright highlights spread into nearby pixels; **glow** for a broader luminous emission.
- 光斑 → **dappled light patches** when caused by an occluder, or **bokeh/light spots** when caused by out-of-focus optics. The source image does not decide which one; keep it ambiguous until the image or brief does.
- 折射效果 → **refraction** for bending through a transparent interface; **caustics** for concentrated reflected/refracted patterns cast onto a surface. Use water caustics only when water or a transparent medium is supported.
- 光束 → **light beam**; **volumetric light shaft** only when mist, smoke, dust, or rain makes the beam visible.
- 梦幻 → soft diffusion, gentle haze, low-to-medium local contrast, restrained bloom, and smooth color transitions. Do not default to glitter, bubbles, or rainbow clutter.
- 神秘 → selective visibility, cool or unusual local color, directional falloff, and controlled shadow—not an undifferentiated purple wash.
- 清晨 → low-angle or broad soft light, cool ambient fill, modest contrast, and atmospheric clarity; it is not automatically pastel.
- 落日 / 余晖 → low-angle warm key, long shadows, warm reflected ambient, and a cooler or neutral shadow family.
- 月光 → a cool, relatively directional source with low saturation, silver-blue highlights, and dark ambient; do not make every surface metallic.
- 霓虹 → emissive source, colored spill, reflections, and local bloom. Keep the emission spatially anchored; neon everywhere is visual noise.
- 白色雾霭 → a participating medium that reveals beams and softens distant contrast; do not add opaque white fog over the whole image.

## 4. Bilingual normalization table

### Source column 1 — entries 1–20

| # | 源标签 | Preferred English | Layer | 视觉控制 / Visual control | Boundary / QA |
|---:|---|---|---|---|---|
| 1 | 暖色调的夕阳 | Warm-toned sunset / warm sunset grade | GRADE + SOURCE | 低角度暖光、金橙色高光、偏暖环境与拉长阴影 / low-angle warm light, golden-orange highlights, warm ambient, elongated shadows | Do not tint every shadow orange; preserve a cooler or neutral shadow family. |
| 2 | 霓虹灯闪烁的夜晚 | Night scene with flickering neon lights | SOURCE + MOOD | 暗环境、多个不稳定彩色发光源、局部彩色溢出与反射 / dark environment, multiple unstable colored emitters, local spill and reflections | “Flicker” is a temporal cue; in a still, imply it through staggered intensity and irregular reflections. |
| 3 | 蓝色冷光 | Blue cool light / cool blue illumination | SOURCE | 蓝色主光、冷色高光、低暖色填充 / blue key light, cool highlights, low warm fill | Separate physical blue illumination from a global blue color grade. |
| 4 | 温暖黄色灯光 | Warm yellow lamplight | SOURCE | 局部暖黄光源、软化边缘、暖色接触与墙面反弹 / localized warm-yellow source, softened edges, warm contact and wall bounce | Specify lamp position and falloff; avoid a flat yellow overlay. |
| 5 | 银色月光 | Silvery moonlight | SOURCE + GRADE | 低饱和冷白/银蓝高光、深暗环境、方向性边缘光 / low-saturation cool-white or silver-blue highlights, dark ambient, directional edge light | Silver is a perceived highlight, not proof that objects are metallic. |
| 6 | 冷色调的蓝光 | Cool-toned blue lighting / blue-cool grade | GRADE + SOURCE | 冷蓝全局倾向或冷蓝主光、降低暖色比例 / global cool-blue tendency or blue key light, reduced warm content | State whether the entire palette shifts or only a local source is blue. |
| 7 | 柔和的金色阳光 | Soft golden sunlight | SOURCE + SHADOW | 柔边暖金主光、温和高光、低到中等对比 / soft-edged warm-gold key, gentle highlights, low-to-medium contrast | “Soft” controls shadow edge and falloff, not merely lower saturation. |
| 8 | 清晨的阳光透过窗帘 | Early-morning sunlight through curtains | SOURCE + OPTICAL | 低角度光束、帘缝分割、室内冷暖混合、柔和灰尘感 / low-angle shafts, curtain-slit segmentation, indoor cool-warm mix, subtle dust | The curtain or its occlusion pattern must be visible or implied; do not use random stripes. |
| 9 | 夜晚的街头霓虹光效 | Nighttime street-neon glow | SOURCE + SURFACE | 暗街、招牌发光、湿地反射、彩色溢光与局部 bloom / dark street, luminous signs, wet reflections, colored spill, localized bloom | Wet reflections require a reflective surface; otherwise keep the ground matte. |
| 10 | 暖橙色的灯光 | Warm orange lighting | SOURCE + GRADE | 橙色局部主光、温暖肤色/材质反应、控制饱和度 / orange local key, warm skin/material response, controlled saturation | Do not push all neutrals into orange; retain material identity. |
| 11 | 神秘的紫色光辉 | Mysterious purple glow | MOOD + SOURCE | 选择性紫色边缘/背景光、深暗对比、少量冷暖分离 / selective purple rim or background light, deep contrast, restrained cool-warm separation | A mood label; avoid a full-frame magenta wash. Entry 31 duplicates it. |
| 12 | 金色的火焰光效 | Golden firelight / golden flame glow | SOURCE + SHADOW | 跳动暖金主光、快速衰减、边缘橙红、非对称阴影 / flickering warm-gold key, rapid falloff, orange-red edges, asymmetric shadows | A still image can imply flicker through irregular shadow edges; do not invent motion blur everywhere. |
| 13 | 阴暗的光影效果 | Dark low-key lighting / shadowy chiaroscuro | SHADOW + GRADE | 低调曝光、深阴影、有限高光、可保留的暗部层次 / low-key exposure, deep shadows, limited highlights, retained shadow detail | “Dark” is not crushed blacks; preserve identity-critical detail and contact shadows. |
| 14 | 光斑照射的阳光 | Dappled sunlight / gobo light patches | OPTICAL + SOURCE | 树叶或格栅遮挡形成的离散亮斑、方向一致、软硬边混合 / discrete patches through leaves or a grille, consistent direction, mixed edge softness | Distinguish from bokeh; a physical occluder should explain the patches. |
| 15 | 蓝紫色的夜空 | Blue-violet night sky | GRADE + MOOD | 深蓝到紫蓝渐变、低照度、稀疏高光、远景空气层次 / deep blue-to-violet gradient, low exposure, sparse highlights, atmospheric depth | Keep the night dark enough; avoid a bright purple studio backdrop. |
| 16 | 透过水面反射的光线 | Water-surface caustics / refracted light through water | OPTICAL + SURFACE | 水面折射形成的游移光纹、局部波纹投影、透明介质高光 / shifting caustic patterns from water, localized ripple projection, transparent-medium highlights | Use caustics when patterns land on a surface; do not spread a generic ripple texture everywhere. |
| 17 | 烈日照射下的阴影 | Hard-sun shadows / shadows under harsh sunlight | SOURCE + SHADOW | 高角度或强直射、硬边深阴影、明确投影方向、高值差 / strong direct sun, hard-edged deep shadows, clear cast direction, high value contrast | Hard does not mean black; account for bounce light and surface color. |
| 18 | 充满梦幻光效的彩虹 | Rainbow with dreamy luminous effects | OPTICAL + MOOD | 光谱色彩、柔和 bloom、薄雾与低对比过渡 / spectral color, restrained bloom, fine haze, low-contrast transitions | Keep the rainbow as a focal event; avoid glitter, lens-flare clutter, and candy saturation. |
| 19 | 梦幻般的紫色氛围 | Dreamlike purple atmosphere | GRADE + ATMOSPHERE + MOOD | 紫色环境染色、柔化远景、轻微 haze、低边缘对比 / purple ambient tint, softened distance, gentle haze, low edge contrast | Dreaminess comes from diffusion and hierarchy, not a uniform purple filter. |
| 20 | 柔和的暖色阳光 | Soft warm sunlight | SOURCE + SHADOW | 暖色主光、柔边阴影、温和反射、舒适中低对比 / warm key, soft shadow edges, gentle bounce, comfortable low-to-medium contrast | Distinguish from #7 “golden” if the palette should remain cream/peach rather than metallic gold. |

### Source column 2 — entries 21–40

| # | 源标签 | Preferred English | Layer | 视觉控制 / Visual control | Boundary / QA |
|---:|---|---|---|---|---|
| 21 | 反射光的折射效果 | Reflected-light caustics / refracted reflection effect | OPTICAL | 透明或反射界面改变光路，在邻近表面形成集中亮纹 / a transparent or reflective interface bends light and creates concentrated patterns on a nearby surface | Refraction bends light; caustics describes the projected pattern. Name the interface: water, glass, crystal, or polished metal. |
| 22 | 冷冽的月光照射 | Cold moonlight illumination | SOURCE + SHADOW | 冷白或银蓝方向光、低暖色填充、深静阴影 / cold-white or silver-blue directional light, low warm fill, deep quiet shadows | “Cold” controls temperature and emotional distance, not necessarily high contrast. |
| 23 | 光晕照亮的物体 | Halo-lit object / object lit by a luminous halo | OPTICAL + SOURCE | 主体边缘或背后出现局部 halo、柔和 rim、受控 bloom / localized halo behind or around the subject, soft rim, controlled bloom | A halo is not automatic front illumination; preserve the light’s source and falloff. |
| 24 | 火光照射下的阴影 | Firelit shadows | SOURCE + SHADOW | 暖橙主光、跳动边缘、深暖阴影、局部反射 / warm-orange key, irregular edge movement, deep warm shadows, localized bounce | Keep the key direction and contact shadows coherent; do not use random orange noise. |
| 25 | 白色雾霭中的光束 | Light beams in white mist / volumetric light shafts | ATMOSPHERE + SOURCE | 白雾参与介质、可见光路、远景对比衰减、层次透视 / white mist as participating medium, visible rays, reduced distant contrast, layered depth | The beam needs a source and a medium; avoid opaque fog that erases the scene. |
| 26 | 炫目的霓虹光效 | Dazzling neon glow | SOURCE + OPTICAL | 高饱和发光源、局部 bloom、彩色溢出、镜面反射 / saturated emitters, localized bloom, colored spill, specular reflection | “Dazzling” should be a focal hierarchy, not global overexposure or unreadable color soup. |
| 27 | 清晨柔和的光线 | Soft early-morning light | SOURCE + SHADOW | 低角度或广阔散射光、冷暖平衡、柔和渐变、低中对比 / low-angle or broad diffuse light, cool-warm balance, gentle gradients, low-to-medium contrast | Do not force a pink filter; morning is a direction/quality/time cue. |
| 28 | 深邃的黑夜中星空的光辉 | Starlight in a deep night sky | SOURCE + GRADE | 深黑蓝环境、稀疏微小高光、低曝光与远距离感 / deep blue-black ambient, sparse pinprick highlights, low exposure, distance | Starlight should not illuminate every foreground surface equally. |
| 29 | 清晰的天光与影子 | Crisp daylight and shadows / clear skylight with shadows | SOURCE + SHADOW | 清澈天光、明确投影、较高微对比、自然色彩 / clear daylight, defined cast shadows, higher micro-contrast, natural color | Preserve atmospheric perspective; “clear” is not HDR halos or oversharpening. |
| 30 | 金色落日下的光影变化 | Shifting light and shadow at golden sunset | SOURCE + SHADOW + MOOD | 低角度金色光、长影、暖色反弹、明显明暗转折 / low-angle golden light, long shadows, warm bounce, visible value transitions | “Shifting” is a temporal/narrative cue; in a still, show changing edge positions or layered shadow states sparingly. |
| 31 | 神秘的紫色光辉 | Mysterious purple glow | DUPLICATE | 与 #11 相同 / same as #11 | Retain for source auditing, but deduplicate reusable vocabularies. |
| 32 | 影子中的微光 | Glimmer within shadows / faint light in shadow | SHADOW + SOURCE | 暗部保留少量反射或反弹光、局部可见、低饱和 / small bounce or reflected light retained in shadow, localized visibility, low saturation | It should anchor to a surface or source; avoid floating specks that read as dust or glitter. |
| 33 | 橙色余晖照射下的物体 | Object lit by an orange afterglow | SOURCE + GRADE | 日落后暖橙环境、弱主光、材质边缘余温 / warm orange afterglow, weak key, lingering warmth on material edges | Keep the overall exposure falling; it is afterglow, not a full orange spotlight. |
| 34 | 红色光晕围绕人物 | Red halo around a person / red rim light | OPTICAL + SOURCE | 人物背后或边缘的红色 rim、背景分离、局部 bloom / red rim around or behind the figure, subject separation, local bloom | Clarify whether it is a halo, rim light, neon sign, or narrative aura; do not draw a red outline. |
| 35 | 蓝天照射下的自然光线 | Natural daylight under a blue sky | SOURCE + GRADE | 太阳直射与蓝天散射填光、自然白平衡、轻微冷阴影 / direct sun plus blue-sky fill, natural white balance, slightly cool shadows | Blue sky is an ambient fill, not a uniform blue overlay. |
| 36 | 紫光照射的场景 | Scene illuminated by purple light | SOURCE | 紫色主光或环境光、明确方向、表面颜色响应 / purple key or ambient light, clear direction, surface color response | Distinguish actual purple illumination from purple grading; retain neutral materials where the light does not reach. |
| 37 | 细腻的光斑 | Delicate light spots / subtle bokeh or dappled highlights | OPTICAL | 小尺度亮点、浅景深散景，或轻微斑驳光纹 / small highlights from shallow-depth bokeh or delicate dappled patterns | Ambiguous without pixels; specify bokeh or dappled rather than leaving both active. |
| 38 | 透过窗帘的柔和光线 | Soft light through curtains | SOURCE + OPTICAL | 窗帘扩散光、柔边条带、室内渐变与轻微透射 / curtain-diffused light, soft bands, interior gradients, subtle transmission | Use curtain folds and light direction as evidence; avoid generic white haze. |
| 39 | 雨后的光线效果 | Post-rain light / after-rain illumination | ATMOSPHERE + SOURCE + SURFACE | 云隙光、湿地反射、清透空气、低角度冷暖交替 / broken-cloud light, wet reflections, clear air, low-angle cool-warm shifts | Wetness must affect contact areas and reflections; do not add rain streaks by default. |
| 40 | 梦幻色彩的光影 | Dreamlike chromatic light and shadow | GRADE + MOOD | 受控的彩色光影、柔和边缘、色相过渡与局部 bloom / controlled chromatic light and shadow, soft edges, hue transitions, localized bloom | Define the palette and hierarchy; “dreamy color” is not permission for uncontrolled rainbow saturation. |

## 5. Taste and visual-critique gate

Judge lighting by causal coherence and perceptual hierarchy, not by how many effects are visible.

- **Source plausibility:** every major highlight and shadow should have a believable emitter, reflector, or environmental explanation.
- **Direction consistency:** key, fill, rim, cast shadow, and reflection should agree unless the contradiction is intentional and named.
- **Value hierarchy:** the focal object should remain readable; dark mood must not erase form, and bright effects must not clip the focal surface.
- **Color discipline:** separate global grade from local light. Keep neutrals and material identity where colored light does not reach.
- **Material response:** glossy, wet, metallic, matte, translucent, and textured surfaces should react differently to the same light.
- **Atmospheric logic:** beams need participating media; mist softens distance; post-rain light changes surface reflection; none should be a decorative overlay.
- **Effect restraint:** bloom, halo, flare, caustics, bokeh, and rainbow dispersion are accents. Repeating them everywhere flattens hierarchy and reads as cheap AI effect stacking.
- **Narrative fit:** “mysterious,” “dreamy,” “serene,” “dangerous,” and “premium” must be decomposed into visible light behavior before use.
- **Edge integrity:** reject halos that look like cutout outlines, double contours, or a pasted filter.
- **Temporal honesty:** flicker, shifting light, and moving shadow can be implied in a still, but do not claim actual motion without video evidence.

### Anti-cheapness firewall

Avoid global blue-orange split-toning without a subject reason; crushed black shadows; uniform purple or orange washes; neon on every edge; bloom on matte surfaces; water caustics without water/glass; volumetric beams without mist/dust; wet reflections on dry matte floors; rainbow clutter; and random light spots with no optical or physical cause.

## 6. Mixing grammar

Use one clear choice per layer:

~~~
global grade
+ one primary light source
+ one shadow behavior
+ optional atmosphere
+ one optical accent
+ material response
+ camera/filter restraint
~~~

Examples:

- blue-violet night sky + silvery moonlight + crisp silhouettes + faint mist shafts + no neon.
- warm-toned sunset + soft sunlight + long cool shadows + dry surfaces + restrained bloom.
- dark street-neon + wet pavement reflections + local red rim light + deep ambient + no global magenta wash.
- traditional ink-wash illustration + cool moonlight + reserve white + soft water caustics only on the floor; do not add photographic lens flare.
- understated luxury interior + soft warm sunlight through curtains + controlled shadow detail + subtle glass reflection; avoid excessive gold and glitter.

Do not stack near-synonyms as separate effects: glow + halo + bloom + dazzling + luminous usually needs one selected optical behavior with a defined intensity.

## 7. Bilingual prompt spine

~~~
中文：为{用途}生成{主体}。全局色调为{grade/palette}；主光源为{source}，方向{direction}，硬度{hard/soft}；阴影{shadow behavior}；空气介质{mist/dust/rain/none}；仅加入{one optical effect}；材质以{surface response}回应光线。保持{subject, composition, camera, text-safe zone}。避免{unexplained effects, crushed blacks, clipped highlights, color wash, clutter}。

English: Create a {use/channel} visual of {subject}. Set the global grade to {palette}; use {source} as the key light from {direction} with {hard/soft} shadows; keep {shadow behavior}. Add {mist/dust/rain/none} as the participating medium. Use only {one optical effect}. Let the material respond through {surface response}. Preserve {subject, composition, camera, and text-safe zone}. Avoid {unexplained effects, crushed blacks, clipped highlights, global color wash, and effect clutter}.
~~~

## 8. Image-analysis output

Pair this reference with sa-boo-visual-reasoning-critic when judging an image. Use evidence classes rather than mood-only claims.

~~~
分析范围 / Scope:
全局色调 / Global grade:
主光源与方向 / Key source and direction:
阴影与对比 / Shadow and contrast:
空气介质 / Participating medium:
光学效果 / Optical effect:
材质响应 / Surface response:
可见依据 / Visible evidence:
设计效果 / Perceptual effect:
问题与风险 / Failure or risk:
最小修改 / Smallest effective change:
未知 / Unknown:
置信度 / Local confidence:
~~~

Use confirmed, likely, possible, unknown, or contradicted locally. If the image is only a text list, report that it teaches vocabulary but does not prove how any light actually looks on a subject.
