# Visual Language Ontology

Use this vocabulary to replace mood-only prose with observable, causal visual language. Select only terms that answer the current decision.

## 1. Core sentence patterns

```text
Observation: [where] + [what] + [visible property] + [relation]
Effect: [perceptual / functional consequence]
Judgment: [fit or conflict with stated intent]
Action: [smallest exact change]
Limit: [what the image cannot prove]
```

Prefer:

```text
画面右下的浅色体块与主物体边缘相接，但接触阴影中断，因此看起来悬浮。
```

Reject:

```text
这里不够高级，关系有点奇怪。
```

## 2. Composition and hierarchy / 构图与层级

| Concept | Visual question | Precise language |
|---|---|---|
| entry point / 视觉入口 | 眼睛先落在哪里，为什么 | highest value contrast, isolation, scale, face/gaze, sharpness |
| reading path / 阅读路径 | 视线随后如何移动 | directional line, repetition, gaze, alignment axis, gradient of contrast |
| focal competition / 焦点竞争 | 有几个元素同时争夺注意 | equal scale/contrast, isolated accents, repeated high saturation |
| figure-ground / 图底关系 | 主体是否与背景分开 | edge contrast, silhouette clarity, overlap, scrim, tonal merger |
| balance / 平衡 | 视觉重量如何分布 | symmetric, asymmetric, radial, top-heavy, edge-heavy, counterweight |
| rhythm / 节奏 | 重复是否有组织 | interval, sequence, alternation, acceleration, pause, variation |
| density / 密度 | 信息或物体是否拥挤 | count per area, cluster size, separation distance, empty interval |
| negative space / 负空间 | 空白在做什么 | isolates, frames, separates, creates pause, leaves crop tolerance |
| crop pressure / 裁切压力 | 元素是否被边界压迫 | tangent, clipped joint, insufficient breathing room, intentional bleed |
| visual weight / 视觉重量 | 哪些元素“更重” | size, darkness, saturation, texture, detail, face, edge proximity |

Do not enforce a universal “one focal point” rule. Some editorial, maximalist, or narrative images intentionally use several focal nodes. Judge whether their hierarchy supports the brief.

## 3. Structure, geometry, and spatial relation / 结构与空间关系

### Entity properties

```text
silhouette / 外轮廓
profile / 侧向轮廓
massing / 体量
proportion / 比例
axis / 轴线
contour / 边界曲线
thickness / 厚度
opening / 开口
seam / 缝线
joint / 接缝或节点
attachment point / 附着点
support / 支撑
clearance / 净距
module / 模块
recess / 凹入
projection / 凸出
```

### Relations

```text
left/right/above/below
inside/contains
attached to / suspended from / rests on / embedded in
aligned with / offset from / centered on
occludes / is occluded by
overlaps / merely touches / is separated from
repeats / mirrors / continues / terminates
front/back/side/oblique relation
```

### View and camera

```text
front / back / side / top / oblique / unknown
wide / medium / close
high / low / eye-level
orth is known only when explicitly shown
orth/south never inferred from image top/bottom
```

Use normalized regions when exact pixels are unnecessary:

```text
upper-left quarter
center band
lower third
right edge
bbox approximately x=0.62–0.81, y=0.55–0.74
```

## 4. Material and construction / 材质与工艺

A material claim needs visible cues or documentation. Separate appearance from composition.

### Surface cues

| Cue | What can be said | What cannot be assumed |
|---|---|---|
| pile / nap / 绒毛长度与倒向 | long/short pile, edge diffusion, directional nap | exact fiber composition |
| roughness / 粗糙度 | matte scatter, granular highlight, uneven micro-shadow | supplier or grade |
| sheen / specularity / 光泽 | broad soft highlight, tight hard highlight, metallic reflection | exact coating chemistry |
| translucency / 半透明 | background transmission, edge glow, internal tint | exact resin/glass type |
| thickness / 厚度 | raised edge, cast shadow, compression, fold radius | measured millimeters without scale |
| drape / 垂坠 | fold frequency, fold depth, gravity response | fabric weight number |
| compression / 压缩 | flattened contact area, rebound, soft deformation | foam density |
| texture scale / 纹理尺度 | micro vs macro grain relative to object | real-world scale without cues |

### Construction cues

```text
stitched / 刺绣或缝制：thread direction, raised stitch, puncture rhythm
appliqué / 贴布：independent edge, thickness, cast shadow, seam
print / 印花：surface-flat color, no raised edge, follows substrate deformation
patch / 贴片：separate backing or border; do not use this word for embroidery
hardware / 五金：mount, loop, ring, zipper pull, connector, contact shadow
lamination / 覆膜：continuous sheen and edge behavior
joinery / 收口：reveals, shadow gaps, miters, butt joints, caps, trims
```

When uncertain, say “呈现出……视觉线索” rather than naming a material as fact.

## 5. Light, color, and atmosphere / 光色与氛围

### Light

```text
direction: front / side / back / top / mixed
hardness: hard-edged / soft-edged shadow
falloff: rapid / gradual
key-fill relationship: high or low contrast
rim separation: present / absent
contact shadow: anchored / weak / broken
reflection logic: coherent / inconsistent
haze: depth-softening atmospheric veil, not bubbles or sparkle
```

### Color

Separate:

- hue from value and saturation;
- local object color from global grade;
- material color from reflected/environmental tint;
- palette harmony from functional hierarchy;
- approximate sampled color from managed production color.

A HEX extracted from a screenshot is evidence about sampled pixels, not proof of the original design token or print color.

## 6. Typography, graphics, and symbols

Inspect:

```text
type role and hierarchy
line length and density
alignment axis
contrast against actual background
word/image competition
logo clear space
symbol legibility at delivery size
edge quality and scale of embroidery/print
exact asset identity vs model-simulated substitute
```

Do not identify a font family from appearance alone unless the source file exposes it. Use “接近某类字形特征” and list the visible traits.

## 7. Function and behavior

A behavior claim needs visible evidence or a stated brief:

```text
reach / grasp / sit / wear / enter / turn / queue / display / store / maintain
```

Translate to geometry:

- who or what acts;
- the path or contact point;
- required opening/clearance/support;
- obstruction or conflict;
- evidence and uncertainty.

## 8. Narrative, brand, and emotional signal

Do not stop at an adjective. Decompose it:

```text
“梦幻”
→ soft-focus diffused light + gentle haze + low edge contrast + restrained palette transitions
→ not bubbles, glitter, sparkle, or cheap bling unless explicitly requested

“高级”
→ controlled hierarchy + credible material + precise edges + intentional restraint + coherent production logic
→ not automatically beige, serif, dark backgrounds, or sparse content

“俏皮”
→ scale exaggeration, gesture, asymmetry, rhythmic accents, or unexpected relation
→ not random stickers or excessive repeated motifs
```

## 9. Artifact and failure vocabulary

```text
duplicate / 重复对象
ghosting / 半透明重影
double contour / 双轮廓
melted seam / 接缝融化
boundary halo / 边缘光晕
floating attachment / 附着悬空
warped geometry / 几何变形
texture drift / 纹理跨区漂移
material flattening / 材质被抹平
perspective break / 透视断裂
shadow mismatch / 阴影方向或接触不一致
local blur / 局部糊化
oversmoothing / 过度磨皮或去纹理
unrequested repetition / 未要求的密集复制
crop discontinuity / 裁切后构件中断
```

For each artifact, name region, affected entity, visible symptom, and consequence.

## 10. Confidence language

Use local confidence, not one global score:

```text
confirmed: directly visible and sufficiently resolved
likely: multiple visible cues support it
possible: one cue, viable alternatives remain
unknown: not shown or not readable
contradicted: conflicts with higher-authority evidence
```

Never use confidence to decorate an unsupported claim. If a detail is unimportant to the decision, omit it rather than assigning fake precision.
