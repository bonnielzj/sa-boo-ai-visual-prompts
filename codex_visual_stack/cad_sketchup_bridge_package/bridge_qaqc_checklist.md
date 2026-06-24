# CAD↔SketchUp Bridge QA/QC Checklist

## CAD→SU ready / CAD 到 SU 准备完成

- [ ] Original CAD preserved in `01_CAD_Original/`.
- [ ] `SU_IMPORT_CLEAN` file created in `02_CAD_Clean_For_SU/`.
- [ ] Units confirmed and recorded.
- [ ] Model extents checked; far-away geometry removed or isolated.
- [ ] Hatches/text/title blocks removed or isolated.
- [ ] Useful layers renamed to `X-SU-REF-*`.
- [ ] Known dimension selected for verification.
- [ ] Imported CAD locked in SketchUp as `CAD_REF_PLAN`.
- [ ] Known dimension checked after import.
- [ ] White model rebuilt using clean SU geometry.

## SU visual-ready / SU 视觉输出准备完成

- [ ] Top plan screenshot readable.
- [ ] At least two white-model perspective views exported.
- [ ] One key elevation/section/focal-wall view exported.
- [ ] Camera hierarchy is clear: entrance / focal wall / circulation / display / material moment.
- [ ] No oversized hidden CAD reference affects zoom/extents.
- [ ] No obvious overlapping wrong shapes or duplicate surfaces.
- [ ] Scale matches CAD layout plan.
- [ ] Assets indexed in `visual_asset_index.json` or equivalent.

## SU→CAD ready / SU 回 CAD 准备完成

- [ ] Design decision confirmed by Bonnie/client.
- [ ] Aligned view/section/plan exported intentionally.
- [ ] Raw SU linework isolated as reference layer.
- [ ] Final CAD linework redrawn/cleaned.
- [ ] CAD dimensions and notes authored in CAD.
- [ ] Material tags and construction annotations added.
- [ ] Revision log updated.
- [ ] Issued PDF/screenshot checked.

## Render/imagegen gate / 渲染与 imagegen 门槛

Do not render if any item below fails:

- [ ] CAD scale confirmed.
- [ ] SU model extents are clean.
- [ ] Camera view is readable.
- [ ] Spatial hierarchy is clear.
- [ ] Material zones are legible.
- [ ] Lighting story is plausible.
- [ ] Visual assets are sharp enough for review.

If failed:

```text
本轮不进入渲染，先做模型 V_next。
```
