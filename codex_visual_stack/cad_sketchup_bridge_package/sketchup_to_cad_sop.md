# SketchUp → CAD SOP / SketchUp 回传 CAD 标准流程

## 0. Gate name / 关卡

`SU02 design decision → CAD_R##_construction_update → issue package`

## 1. What can return to CAD / 可回传 CAD 的内容

Only return confirmed design information:

- new or changed wall positions / 新增或调整墙体
- openings / 门窗洞口
- fixed furniture and built-ins / 固定家具和柜体轮廓
- ceiling levels and lighting points / 天花标高和灯位
- material boundaries / 材料分界
- panel seams / 分缝
- aligned elevations / 对齐立面
- section/cut linework / 剖切线稿
- flattened curved-panel references / 曲面展开参考

Do not return as construction fact:

- unapproved AI-render decoration / 未确认 AI 渲染装饰
- atmospheric lighting only / 氛围光效
- downloaded mesh noise / 下载模型杂线
- furniture styling without confirmed dimensions / 无尺寸软装摆场

## 2. Export strategy / 导出策略

| Need | SketchUp action | CAD action |
|---|---|---|
| wall elevation | aligned scene / Curic Align View | import as `X-SU-REF-ELEV`, redraw final lines |
| section | section plane / s4u Slice | redraw section profile + dimensions |
| panel layout | Floor Panel Grid / clean model lines | CAD layer standard + material code |
| curved panel | Flatten Faces / 2D reference | redraw buildable panel geometry |
| ceiling/light | top scene + reference exports | CAD reflected ceiling plan |

## 3. CAD standardization / CAD 标准化

- Put raw SU export on `X-SU-REF-*` first.
- Redraw final construction linework on SA&BOO CAD layers.
- Add CAD-authored dimensions, not screenshot-only measurements.
- Add material tags, notes, revision marks.
- Update revision log and title block revision table.

## 4. Required visual proof / 必须产出的视觉证明

A complete return package should include:

```text
R##_su_design_intent_view.png
R##_su_aligned_elevation_reference.png
R##_cad_redrawn_elevation_or_plan.pdf/png
R##_cad_su_conflict_report.md
R##_revision_log.csv
```

## 5. Decision ownership / 决策归属

```text
Precise dimensions / construction issue → CAD is source of truth.
Spatial composition / client approval → SketchUp is source of truth.
Material mood / lighting / render → render/SU asset is source of truth.
Issued construction drawings → CAD/PDF issue package is source of truth.
```

If CAD and SketchUp conflict, stop and write a conflict report before continuing.
