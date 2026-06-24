# CAD↔SketchUp Bridge Deliverable Templates

## Project folder / 项目文件夹

```text
00_原始资料
01_CAD_Original
02_CAD_Clean_For_SU
03_SketchUp_Model
04_SU_Exports_View
05_Render_Assets
06_CAD_Construction
07_Client_Presentation
08_Revision_Log
assets/visual_cache
```

## File naming / 文件命名

```text
PROJECT_PLAN_ORIGINAL_R00.dwg
PROJECT_SU_IMPORT_CLEAN_R00.dwg
PROJECT_DESIGN_MODEL_R00.skp
PROJECT_WHITE_MODEL_VIEW_R00_01.png
PROJECT_RENDER_CONCEPT_R00_01.png
PROJECT_CONSTRUCTION_R00.dwg
PROJECT_REVISION_LOG_R00.csv
```

## Bridge report / 桥接报告模板

```text
桥接目标：CAD→SU / SU→CAD / 双向迭代
当前 gate：B00 / A01 / SU01 / SU02 / M01 / R01

当前输入资产：
- CAD/DXF/PDF/SU/图片：
- 版本：
- 单位/比例状态：

视觉主线：
- 本轮必须产出的图像资产：
- 参考/白模/渲染/施工图之间的关系：

CAD 处理：
1.
2.
3.

SketchUp 处理：
1.
2.
3.

需要调用的 skills / MCP：
1.
2.
3.

风险与冲突：
- 尺寸：
- 图层/导入：
- 模型：
- 施工表达：

交付物：
- SU_IMPORT_CLEAN：
- SketchUp 模型/视图：
- 白模/渲染图：
- CAD 回传/施工图：
- 版本记录：
```

## Conflict report / 冲突报告模板

```text
冲突位置：
CAD 事实：
SketchUp 状态：
视觉证据 asset_id：
影响：尺寸 / 模型 / 出图 / 施工
建议处理：以 CAD 为准 / 以 SU 方案为准后回改 CAD / 需要 Bonnie 确认
下一步：
```

## Visual asset record / 视觉资产记录模板

```json
{
  "asset_id": "project_r##_top_plan_scale_check",
  "gate": "SU01",
  "asset_type": "top_plan_screenshot",
  "source_file_path": "04_SU_Exports_View/R##_top_plan_cad_scale_check.png",
  "source_model_path": "03_SketchUp_Model/PROJECT_DESIGN_MODEL_R##.skp",
  "source_cad_path": "02_CAD_Clean_For_SU/PROJECT_SU_IMPORT_CLEAN_R##.dwg",
  "capture_date": "YYYY-MM-DD",
  "quality_status": "accepted / rejected / needs_recapture",
  "scale_status": "confirmed / conflict / unknown",
  "qa_notes": "",
  "prev_id": null,
  "next_id": null,
  "related_ids": []
}
```
