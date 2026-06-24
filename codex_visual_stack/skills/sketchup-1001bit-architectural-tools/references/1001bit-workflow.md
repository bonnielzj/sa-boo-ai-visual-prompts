# 1001bit Tools workflow reference

## Useful tool families for interior workflow

1001bit Freeware contains many small architectural tools. Exact menu wording can vary, but the installed package includes tool files for these families:

- Wall/opening/frame: `wall1`, `opening`, `dframe`, `wframe`.
- Stairs/escalator: `staircase1-4`, `spiralstair`, `escalator`.
- Roof/rafter: `roof1`, `hiproof`, `rafter1`, `slopeedges`.
- Louvre/grille/screen: `hlouvres`, `vlouvres`, `cgrille`, `rgrille`, `screen1`.
- Arrays/division: `linear_array`, `rect_array`, `polar_array`, `divide`, `paneldivide`.
- Edge/face helpers: `align`, `extend`, `fillet`, `chamfer`, `offset_edge`, `move_vertex`, `perpendicular_line`, `point_on_face`, `hline_faces`, `fonplane`, `bestface`.
- Form helpers: `revsurf`, `extrude1`, `extrude2`.

## Decision matrix

| Need | Prefer |
|---|---|
| Fast architectural white-model utility | 1001bit |
| Repeatable trim/slat/profile assembly | Profile Builder |
| Regular floor/wall/ceiling panel grid | MyPanelGrid |
| Clean imported CAD linework before modeling | Edge Tools² |
| Precise length-preserving bend | TrueBend |
| Membrane/bubble/soft skin surface | Soap Skin Bubble |
| Organic sculpted mesh/furniture | Artisan |
| Free-form deformation of an existing object | SketchyFFD |
| Batch material cleanup/scheme swap | TT Material Replacer |
| Texture/UV alignment after modeling | Eneroth Texture Positioning |

## Recommended usage recipes

### Door/window opening and frame white model

1. Start with clean wall massing, grouped by room/wall.
2. Mark opening centerline or dimensions.
3. Use 1001bit opening/frame tools for quick generation where appropriate.
4. Group generated frame/opening elements separately.
5. For final design-quality frames, rebuild important visible profiles with Profile Builder if needed.
6. Check face orientation and wall thickness.

### Stair study

1. Define floor-to-floor height, tread depth, riser count, width, landing needs.
2. Use 1001bit stair/spiral stair for quick option massing.
3. Name options clearly: `1001_Stair_OptionA_01`.
4. Check headroom, landing clearances, and circulation.
5. Replace or refine handrails/stringers manually/Profile Builder if final render needs detail.

### Louvre / grille / screen

1. Define boundary, module size, blade/slat angle, spacing, depth.
2. Use 1001bit louvre/grille/screen for fast white model.
3. If a curved screen is required, generate straight first, group it, then consider TrueBend or manual curved array.
4. If high-end visible detail is required, rebuild the final assembly with Profile Builder for cleaner profiles.
5. Apply material and use Texture Positioning if grain direction matters.

### Panel / array helper

1. Use 1001bit arrays/divide for quick distribution studies.
2. Use MyPanelGrid instead when the task is specifically floor/wall/ceiling panel layout with thickness/gaps.
3. Delete failed array experiments immediately to avoid model bloat.
4. Convert repeated objects to components where possible.

## Old-plugin caution checklist

- 1001bit v1.0.5 is useful but old; test tools on sample geometry first.
- Many tool implementations are encrypted `.rbs`; avoid using it on the only copy of a critical model.
- Keep backups and group outputs immediately.
- If a command creates messy geometry, use it as reference and remodel cleanly with native tools/Profile Builder.
- Do not expect every tool to replace modern specialized plugins.

## QA checklist

- **Before:** clean input, correct units, backup/copy exists.
- **After command:** group output, name it, check dimensions.
- **Geometry:** no stray raw edges, duplicate faces, reversed faces, tiny fragments.
- **Workflow:** decide whether output is final geometry or just a white-model/reference.
- **Rendering:** standardize materials; fix UV/textures before AI/D5/Enscape-style render handoff.

## Good trigger requests

- “用 1001bit 快速做楼梯白模。”
- “这个墙体上快速开门洞窗洞并做框。”
- “帮我判断格栅/百叶用 1001bit 还是 Profile Builder。”
- “用 1001bit 做一个建筑白模构件流程。”
- “这个模型需要快速生成屋顶/檩条/楼梯/屏风。”
