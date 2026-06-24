# CAD → SketchUp SOP / CAD 到 SketchUp 标准流程

## 0. Gate name / 关卡

`B00 source baseline → A01 verified layout → SU01 accurate white model`

## 1. Preserve source / 保留原始文件

- Copy original DWG/DXF/PDF into `01_CAD_Original/`.
- Never overwrite the original CAD.
- Create a separate file in `02_CAD_Clean_For_SU/` named:

```text
PROJECT_SU_IMPORT_CLEAN_R00.dwg
PROJECT_SU_IMPORT_CLEAN_R00.dxf
```

## 2. CAD audit / CAD 审查

Check and record:

| Item | English | 中文 |
|---|---|---|
| units | mm preferred for interiors | 室内优先毫米 |
| extents | no remote geometry | 无远距离垃圾线 |
| model space | useful linework in model space | 有效线在模型空间 |
| xrefs | bind/detach intentionally | 外部参照明确处理 |
| blocks | simplify only in clean copy | 仅在清洁版中简化块 |
| hatches | remove unless useful | 填充非必要则删除 |
| text/dim | isolate as reference | 文字尺寸只作参考 |
| duplicate/tiny gaps | clean before SU import | 导入 SU 前清理重复线/小缝 |

## 3. Keep vs remove / 保留与删除

Keep for SU import:

- wall outlines / 墙体轮廓
- structural boundaries / 结构边界
- openings / 门窗洞口
- fixed furniture and built-ins / 固定家具与柜体
- ceiling control lines / 天花控制线
- floor finish boundaries / 地面分区线
- critical datum and selected dimensions / 关键标高与少量校核尺寸

Remove or isolate:

- title blocks / 图框
- dense hatches / 密集填充
- general notes / 大段说明
- leaders / 引线
- repeated symbols / 重复符号
- unrelated MEP symbols / 无关机电点位
- far-away geometry / 远距离垃圾线

## 4. Layer/tag standard / 图层建议

```text
X-SU-REF-PLAN
X-SU-REF-WALL
X-SU-REF-OPENING
X-SU-REF-FURN
X-SU-REF-CEILING
X-SU-REF-FLOOR
X-SU-REF-ELEV
X-SU-REF-DIM
X-SU-NPLT-GRID
```

## 5. SketchUp import / SketchUp 导入

- Import units: millimeters unless project evidence says otherwise.
- Group imported CAD immediately.
- Lock imported CAD group/component.
- Assign tag: `CAD_REF_PLAN`.
- Check one known dimension with Tape Measure.
- Do not model on raw CAD edges; rebuild clean geometry.

## 6. Required visual proof / 必须产出的视觉证明

Save into `04_SU_Exports_View/`:

```text
R##_top_plan_cad_scale_check.png
R##_white_model_view_01.png
R##_white_model_view_02.png
R##_key_elevation_or_section.png
```

Each file should be added to visual asset index with:

```text
asset_id, source_file_path, capture_date, gate, scale_status, qa_status, prev_id, next_id
```
