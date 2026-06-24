# Design Output Logic

Use this reference when Bonnie wants confidence that tools, skills, MCPs, plugins, GitHub resources, or online references are being coordinated toward a clear design result.

## Prime rule

The number of tools is not the issue. The invariant is:

```text
design intention → visual target → spatial proof → model proof → material/light proof → curated image output → critique/iteration
```

Tools may change each round. The output logic must stay stable.

## Operating contract

Before acting on any substantial interior design task, define:

```text
1. 这轮要证明什么？
2. 最后要得到哪一类图片？
3. 哪些信息必须保持准确？
4. 哪些地方可以进行审美探索？
5. 本轮失败的判定标准是什么？
```

Never start from “which plugin should be used.” Start from the image and design decision the user needs.

## Six-stage output chain

### 1. Intent lock

Translate the user’s words into a small number of design commitments:

- spatial role: entrance, living room, bedroom, office, showroom, restaurant, etc.
- emotional temperature: quiet, ceremonial, warm, sculptural, precise, soft, dramatic.
- primary spatial move: axis, volume, frame, curve, wall thickness, ceiling fold, light slot, furniture island.
- material hierarchy: main / secondary / accent / tactile detail.
- human story: who uses it, what behavior it supports, what memory or identity it carries.

Output: a short brief and the first visual target.

### 2. Visual target definition

Define image assets before detailed work:

- plan-like proof image for layout and scale.
- white-model perspective to prove volume.
- aligned elevation/section to prove proportion.
- material/light test to prove atmosphere.
- final hero images and detail crops.

Output: shot list, not abstract description.

### 3. Accuracy and constraint lock

Separate facts from interpretation:

- facts: CAD dimensions, walls, openings, structural limits, plumbing, ceiling height, existing photos.
- assumptions: missing dimensions, furniture sizes, material availability, lighting positions.
- creative variables: composition, line rhythm, material proportions, furniture styling, color temperature.

Output: what cannot be changed and what can be explored.

### 4. Spatial/model proof

Build only enough model to answer the current visual question:

- use CAD/SU tools to create clean walls, openings, key volumes, furniture blocks, ceiling/floor zones.
- do not over-detail before proportion and camera are approved.
- reject renders based on wrong scale, bad axis, unclear focal wall, or impossible circulation.

Output: white-model screenshots or model-view capture instructions.

### 5. Material/light/camera proof

After the white model works:

- assign controlled material zones, not random full-detail materials.
- define light story: daylight / warm evening / accent / task.
- set camera hierarchy: hero view, human-eye view, elevation proof, detail crop.
- generate prompt/render drafts only from validated model views.

Output: material-light test images or prompt pack tied to specific screenshots.

### 6. Curated delivery and critique

Final output must be judged as images:

- select the strongest views; discard weak or repetitive ones.
- identify what each image proves.
- mark failures: scale, composition, material logic, lighting, buildability, AI-generic feeling.
- define the next iteration image, not only the next text task.

Output: image pack, selected prompts, QA notes, and next visual checkpoint.

## Tool routing principle

Use any necessary skill/plugin/MCP/GitHub/online source, but justify it by output role:

```text
CAD / cadq / AutoCAD MCP → accuracy, measurement, construction logic.
SketchUp MCP / SU plugins → spatial/model proof.
Material plugins / supplier references → material credibility.
Lighting/render plugins → atmosphere proof.
Image generation / prompt skills → visual exploration and final visual assets.
Proposal/presentation skills → communication and curation.
Online resources → current references, tool docs, real project/supplier evidence.
```

If a tool does not improve the next visual checkpoint, do not foreground it.

## Standard response skeleton

For complex design work, respond in this order:

```text
设计输出逻辑：
- 本轮要证明：
- 最终图像目标：
- 准确性底线：
- 审美探索范围：

视觉链：
- 已有图像/模型/CAD：
- 缺失图像：
- 下一张必须产生的图：

生产路径：
- CAD / SU / 插件 / MCP / online resource 如何服务这张图：
- 暂不做什么，为什么：

质量门槛：
- 通过标准：
- 失败信号：
- 下一轮迭代：
```

## Anti-drift rule

If the conversation becomes too conceptual, pull it back with:

```text
这段概念要落到哪一张图？
这张图要证明哪个设计判断？
现在缺的是 CAD 准确性、SU 体块、材质、灯光、镜头，还是渲染？
```

The goal is not to sound intelligent. The goal is to make the next visual decision clearer and produce stronger images.
