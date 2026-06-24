# SA&BOO SketchUp Master Workflow Index

Use this reference when Bonnie wants the last two days of SketchUp 2025, MCP, plugins, skills, AI Render, image generation, QA, and design judgment fused into one callable operating system.

## Prime contract

Bonnie should not need to remember plugin names. Convert natural-language design intent into:

```text
intent -> visual question -> production phase -> tool route -> SketchUp action -> image checkpoint -> QA -> next iteration
```

Never start from "which plugin do we have?". Start from:

```text
这轮要证明哪张图？
```

## One-sentence triggers

Map Bonnie's words to the right phase:

- "我有想法/客户需求/风格方向" -> intake and visual target.
- "先搭白模/体块关系" -> closed shell, plan proof, perspective white model.
- "这个立面想做石材木饰面/线条/灯带" -> focal-wall profile and panel rhythm.
- "想要弧形/包裹感/柔软/异形" -> curve or organic modeling.
- "材质深化/木纹/石材/颜色" -> material zones, UV, replacement, palette.
- "角度不好看/出图镜头" -> camera and composition.
- "AI Render/继续渲染/出图" -> model-before-render gate, prompt, source image, render QA.
- "做提案/给客户看/小红书" -> curated image pack and presentation sequence.

## Fixed phase order

Do not skip phases unless the required proof already exists.

1. **Intent Lock**
   - Output: brief, assumptions, visual target.
   - Skills: `sa-boo-project-intake`, `sa-boo-visual-first-core`.

2. **Accuracy Lock**
   - Output: plan/top proof, dimensions, fixed constraints.
   - Skills/tools: `cadq`, `sa-boo-cad-sketchup-bridge`, `interior-layout-optimizer`, AutoCAD/CAD skills when drawings exist.

3. **Spatial White Model**
   - Output: closed-room shell, furniture blocks, plan proof, two perspective sources.
   - Skills/plugins: SketchUp MCP, `sketchup-1001bit-architectural-tools`, `sketchup-edge-tools-cleanup`, `sketchup-solid-inspector-repair`.

4. **Focal Wall / Profile / Panel Logic**
   - Output: aligned elevation, focal-wall perspective, line/proportion rhythm.
   - Skills/plugins: `sketchup-profile-builder`, `sketchup-floor-panel-grid`, `sketchup-curic-align-view`, `sketchup-s4u-slice-section-cuts`.

5. **Curve / Soft / Organic Logic**
   - Output: curved mass proof, side/section proof, render-ready smoothness check.
   - Skills/plugins: choose one main tool:
     - `sketchup-truebend-bending` for precise bent slats/trims/rails.
     - `sketchup-sketchyffd-deformation` for cage-warped masses.
     - `sketchup-artisan-organic-modeling` for cushions, sofas, soft forms, sculptural pieces.
     - `sketchup-soap-skin-bubble-surfaces` for membranes/canopies/bubble-like surfaces.

6. **Material / Color / UV**
   - Output: material zoning image, material names, A/B scheme if needed.
   - Skills/plugins: `sketchup-material-replacer`, `sketchup-texture-positioning`, `sketchup-color-maker-palettes`, `sketchup-architextures-materials`, `sa-boo-material-supplier-budget-db`.

7. **Lighting / Camera**
   - Output: camera list, locked scenes, source contact sheet.
   - Skills/plugins: `sketchup-advanced-camera-tools`, `sketchup-curic-align-view`, `sketchup-lightup-lighting`, `sa-boo-realtime-render-presentation`.

8. **AI Render / Image Generation**
   - Output: prompt pack, render draft, comparison image, QA notes.
   - Skills/tools: `sketchup-ai-render-workflow`, `imagegen`, `sa-boo-prompt-translator`, `sa-boo-visual-style-prompt-lab`.

9. **Curation / Presentation**
   - Output: selected hero/detail/elevation sequence, proposal or social image pack.
   - Skills: `sa-boo-proposal-deck-director`, `sa-boo-xiaohongshu-ip`, presentations/PDF skills when needed.

## Routing rule

Use the smallest route that can produce the next image:

```text
1 primary skill
1-3 support skills
0-1 QA skill
```

If too many tools seem relevant, choose by failure mode:

- Bad scale or layout -> layout/CAD/spatial skill.
- Weak model -> white model/profile/panel/curve skill.
- Weak material -> material/UV/palette skill.
- Bad angle -> camera skill.
- Weak render -> AI render skill only after source model passes.
- Weak client communication -> proposal/presentation skill.

## Mandatory model-before-render gate

Before AI Render or image generation from a SketchUp view, source images must prove:

- closed room shell,
- valid camera,
- clear focal hierarchy,
- believable scale,
- controlled material zones,
- plausible lighting logic,
- clean tags/materials/no back-face leaks,
- one authored spatial idea.

If any item fails, stop and return to modeling:

```text
本轮不进入渲染。
失败原因：
模型 V_next 修正：
下一视觉检查点：
```

## Plugin meaning in plain language

Use this as Bonnie-facing translation:

- 1001bit: quick architectural bones.
- Profile Builder: repeated trims, skirting, frames, ribs, reveals, cabinetry rhythm.
- MyPanelGrid/Floor Generator: floor, wall, ceiling, stone, tile, veneer panel grids.
- TrueBend: controlled bent strips, slats, trims, rails.
- SketchyFFD: free-form bending, bulging, tapering of masses.
- Artisan: soft furniture and sculptural organic refinement.
- Soap Skin Bubble: membrane or stretched-surface ideas.
- Edge Tools / Solid Inspector / Flatten: cleanup, repair, planar preparation.
- Material Replacer / Texture Positioning / ColorMaker / Architextures: material iteration and UV discipline.
- Skatter: books, plants, objects, fibers, repeated visual texture after architecture works.
- Advanced Camera Tools / Curic Align View: hero shots, physical camera logic, aligned elevations.
- LightUp / realtime render skills: light testing before final visual output.
- AI Render / imagegen: materialized concept images after model proof.

## Default response when Bonnie gives an idea

Use this compact shape:

```text
本轮要证明：
下一张图：
准确性底线：
审美探索：
主 skill：
辅助 skill：
暂不调用：
SketchUp 动作：
输出资产：
QA 门槛：
```

## Default response when Bonnie asks "你来做"

Act in this order:

1. Inspect current model/file/context.
2. State the next image checkpoint.
3. Create or revise SketchUp model/source views.
4. Export contact sheet or source PNG.
5. QA source.
6. Only then render or write prompt.
7. Save image paths and notes.

## Memory of the failed test

The first living-room test failed because rendering started before the source model had enough authored design. The correction was Design V2:

- closed shell,
- stronger TV-wall hierarchy,
- triptych stone,
- walnut display/storage spines,
- profile/reveal logic,
- panel grid,
- curved sofa-wall logic,
- better camera set,
- source-to-render comparison.

Use this as a permanent caution: prompt quality cannot rescue weak spatial authorship.

## Quality sentence

Before finalizing any image, answer:

```text
这张图证明了哪个设计判断？它为什么不是一张漂亮但空洞的 AI 图？
```

