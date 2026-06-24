# SA&BOO CAD↔SketchUp Bridge Package

This package turns the `sa-boo-cad-sketchup-bridge` skill into a practical production kit for GitHub reuse. It is not only a language scaffold: it contains checklists, MCP routing, deliverable templates, and a visual-chain schema for CAD/SU evidence.

本包把 `sa-boo-cad-sketchup-bridge` 从技能说明升级为可执行的生产资料包：包含 CAD→SU、SU→CAD、QA、MCP 路由、交付物模板和视觉证据链 schema。

## Purpose / 目标

Keep CAD and SketchUp synchronized:

```text
accurate CAD truth
→ clean SU import reference
→ verified SketchUp white model
→ readable visual evidence
→ render/imagegen only after QA
→ confirmed design back to CAD
→ revision log and asset chain
```

中文：

```text
CAD 准确真值
→ SketchUp 清洁导入参考
→ 经验证的 SU 白模
→ 可读视觉证据
→ QA 后再进入渲染 / imagegen
→ 已确认设计回传 CAD
→ 版本记录与视觉链表
```

## Files / 文件

- `cad_to_sketchup_sop.md` — CAD 清理与 SketchUp 导入 SOP。
- `sketchup_to_cad_sop.md` — SketchUp 方案回传 CAD SOP。
- `bridge_qaqc_checklist.md` — 可勾选 QA/QC 表。
- `mcp_tool_routing_matrix.md` — 什么时候用 cadq / autocad_mcp / SketchUp MCP / imagegen。
- `deliverable_templates.md` — 项目文件夹、命名、报告、冲突记录模板。
- `visual_chain_schema.json` — CAD/SU 视觉证据链 JSON schema。
- `bridge_asset_chain.example.json` — 真实项目可套用的链表示例。

## Non-negotiable gates / 硬门槛

Do not render or imagegen before:

- CAD unit/scale is confirmed.
- SU clean import reference exists.
- Imported CAD is locked/isolate-tagged.
- Known dimension is checked inside SketchUp.
- Far-away/oversized/hidden CAD garbage is removed or isolated.
- White-model top view + perspectives are readable.
- Visual asset index records the evidence.

如果不满足：本轮不进入 Enscape / AI Render / imagegen，先做 `V_next` 模型清理。
