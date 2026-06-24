# SketchUp Skill Router

Use this router to avoid skill overload. Choose by current production phase, not by plugin availability.

## Routing rule

```text
User request → identify phase → choose one primary skill → add only necessary support skills → define next image checkpoint.
```

Default maximum per round:

- 1 primary SketchUp/interior skill.
- 1-3 support skills.
- 1 QA/cleanup skill only if needed.
- Do not load/render/style skills before white-model scale and camera are clear.

## Phase matrix

| Phase | User intent | Primary skill | Support skills | Do not call yet |
|---|---|---|---|---|
| 0 Intake | “我有一个想法/项目/需求” | `sa-boo-project-intake` | `sa-boo-sketchup-interior-director`, `sa-boo-visual-first-core` | Detailed modeling plugins |
| 1 CAD bridge | “从CAD建模/清CAD/导入SU” | `sa-boo-cad-sketchup-bridge` | `cadq`, `autocad-drafting`, `sketchup-edge-tools-cleanup`, `sketchup-selection-toys-selection-control` | Render/material skills |
| 2 Layout | “平面怎么改/动线/户型优化” | `interior-layout-optimizer` | `cadq`, `sketchup-space-finder-planning` | Organic/renderer plugins |
| 3 White model | “先搭空间体块/墙顶地/基础白模” | `sketchup-1001bit-architectural-tools` | `sketchup-edge-tools-cleanup`, `sketchup-solid-inspector-repair`, `sketchup-profile-builder` | AI render until scale proof exists |
| 4 Profile/detail | “线条/护墙板/门套/收口/柜体立面” | `sketchup-profile-builder` | `sketchup-floor-panel-grid`, `sketchup-curic-align-view`, `sketchup-selection-toys-selection-control` | Organic tools unless curved detail needed |
| 5 Panel/grid | “地面/墙面/天花分缝/石材木饰面模数” | `sketchup-floor-panel-grid` | `sketchup-texture-positioning`, `sketchup-material-replacer`, `sketchup-curic-align-view` | Rendering before panel scale QA |
| 6 Curve/organic | “弧形/软包/异形/流动曲面/雕塑感” | Choose one: `sketchup-truebend-bending` / `sketchup-artisan-organic-modeling` / `sketchup-sketchyffd-deformation` / `sketchup-soap-skin-bubble-surfaces` | `sketchup-solid-inspector-repair`, `sketchup-s4u-slice-section-cuts` | All curve tools at once |
| 7 Cleanup/repair | “乱线/破面/选不中/导入很脏/模型很卡” | Choose one: `sketchup-edge-tools-cleanup` / `sketchup-selection-toys-selection-control` / `sketchup-solid-inspector-repair` | CleanUp³ if installed, `sketchup-flatten-faces-cleanup` | Design styling |
| 8 Material/UV | “换材质/木纹方向/石材比例/颜色体系” | `sketchup-material-replacer` | `sketchup-texture-positioning`, `sketchup-color-maker-palettes`, `sa-boo-material-supplier-budget-db` | Camera/render if material zones unresolved |
| 9 Furnishing/scatter | “摆件/植物/书/地毯纤维/软装氛围” | `sketchup-skatter-scattering` | `sketchup-artisan-organic-modeling`, `sketchup-dbs-move-rotate-open-close` | Construction CAD skills |
| 10 Camera/views | “找角度/立面正视/客户汇报镜头” | `sketchup-advanced-camera-tools` | `sketchup-curic-align-view`, `sa-boo-realtime-render-presentation` | New geometry unless view exposes issue |
| 11 Lighting/render | “出白模图/AI Render/灯光/材质效果” | `sketchup-ai-render-workflow` | `sketchup-lightup-lighting`, `sa-boo-realtime-render-presentation`, `sa-boo-prompt-translator` | Modeling plugins except to fix failed QA |
| 12 Presentation | “做提案/图包/客户汇报/小红书” | `sa-boo-proposal-deck-director` | `sa-boo-realtime-render-presentation`, `sa-boo-xiaohongshu-ip` | Raw modeling unless missing image assets |

## Tool choice rules for similar skills

### Selection vs cleanup vs solid repair

- Use `sketchup-selection-toys-selection-control` when the problem is **how to select the right entities**.
- Use `sketchup-edge-tools-cleanup` when the problem is **gaps, stray curves, imported linework, curves, colinear edges**.
- Use `sketchup-solid-inspector-repair` when the problem is **non-solid groups, boolean/export/3D print failure**.
- Use CleanUp³ only when installed and the problem is **whole-model cleanup or bloat**.

### Curved/organic tools

- Use `sketchup-truebend-bending` for precise length-preserving bends of linear objects: trims, slats, rails, counters.
- Use `sketchup-sketchyffd-deformation` for cage/lattice deformation of an existing object/mass.
- Use `sketchup-artisan-organic-modeling` for sculpted/subdivision forms: cushions, soft furniture, organic decor.
- Use `sketchup-soap-skin-bubble-surfaces` for membrane surfaces from boundaries: canopy, dome, soft stretched panels.
- Do not call all four unless comparing methods conceptually.

### Material tools

- Use `sketchup-material-replacer` for batch replace and scheme A/B swaps.
- Use `sketchup-texture-positioning` for UV/texture direction, stone slab, wood grain, tiles.
- Use `sketchup-color-maker-palettes` for palette/color standardization.
- Use material-supplier skill for cost/vendor/procurement, not SketchUp painting.

### View and render tools

- Use `sketchup-curic-align-view` for wall elevations, cabinet faces, aligned section-like views.
- Use `sketchup-advanced-camera-tools` for hero camera/lens/framing planning.
- Use `sketchup-lightup-lighting` for real-time light diagnostics.
- Use `sketchup-ai-render-workflow` for white-model-to-concept render prompts and image production.

## Minimal route output

Before complex execution, state:

```text
任务阶段：
本轮主 skill：
辅助 skill：
暂不调用：
下一视觉检查点：
```

## Examples

### Example A — CAD imported and messy

```text
任务阶段：CAD bridge / cleanup
主 skill：sa-boo-cad-sketchup-bridge
辅助：sketchup-selection-toys-selection-control, sketchup-edge-tools-cleanup
暂不调用：材质、渲染、曲面插件
下一视觉检查点：CAD clean top view / SU imported reference screenshot
```

### Example B — TV wall with stone and wood blocks

```text
任务阶段：profile/detail + panel/grid
主 skill：sketchup-profile-builder
辅助：sketchup-floor-panel-grid, sketchup-curic-align-view, sketchup-material-replacer
暂不调用：Skatter, Artisan, STL, CAD drafting
下一视觉检查点：正立面白模截图 + 一个透视白模截图
```

### Example C — curved sofa background

```text
任务阶段：curve/organic
主 skill：sketchup-truebend-bending or sketchup-sketchyffd-deformation
辅助：sketchup-artisan-organic-modeling only if soft cushion/subdivision is needed
暂不调用：Soap Skin Bubble unless it is a membrane surface
下一视觉检查点：弧形体块白模图 + 侧向剖面图
```

### Example D — ready to render

```text
任务阶段：lighting/render
主 skill：sketchup-ai-render-workflow
辅助：sketchup-advanced-camera-tools, sa-boo-realtime-render-presentation, sa-boo-prompt-translator
暂不调用：建模插件，除非白模 QA 失败
下一视觉检查点：2张AI Render草图 + 1张材质/灯光对照图
```
