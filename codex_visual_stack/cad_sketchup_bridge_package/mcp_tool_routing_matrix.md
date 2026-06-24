# MCP Tool Routing Matrix / MCP 工具路由矩阵

This matrix keeps the bridge practical and prevents random visual changes.

## Tool choices / 工具选择

| Task | Primary tool/skill | Why |
|---|---|---|
| DWG/DXF semantic query | `cadq` | Ask drawing facts: areas, features, nearest items, elevation/profile when supported. |
| AutoCAD drafting/editing | `autocad-drafting` + `autocad_mcp` | Create/modify lines, layers, dimensions, blocks, plot PDFs. |
| CAD cleanup for SU | AutoCAD + `sa-boo-cad-sketchup-bridge` | Remove clutter, isolate layers, export clean DWG/DXF. |
| SketchUp white model | SketchUp MCP/manual + SketchUp skills | Rebuild clean model; do not use raw imported edges as final geometry. |
| Edge repair | `sketchup-edge-tools-cleanup`, `sketchup-solid-inspector-repair` | Fix gaps, strays, non-manifold/overlap issues. |
| Organic/curved modeling | `sketchup-artisan-organic-modeling`, `sketchup-sketchyffd-deformation`, `sketchup-truebend-bending` | Use after scale and base model are verified. |
| Camera/elevation | `sketchup-curic-align-view`, `sketchup-advanced-camera-tools` | Export accurate elevations and controlled perspectives. |
| Rendering | `sketchup-enscape-render-workflow`, realtime render skills | Only after bridge QA passes. |
| AI output | `sketchup-ai-render-workflow`, `imagegen`, prompt skills | Use white model/reference images as controlled input. |
| Asset chain | `sa-boo-visual-asset-index` | Store screenshot, source path, QA status, chain links. |

## Placeholder MCP config / 安全占位

Use placeholders only in committed files:

```text
${CADQ_BIN}
${PYTHON_BIN}
${AUTOCAD_MCP_SERVER_PATH}
${SKETCHUP_MCP_BRIDGE_SCRIPT}
${FIGMA_ACCESS_TOKEN}
${GITHUB_TOKEN}
${AIMAMI_RELAY_URL}
${AIMAMI_RELAY_TOKEN}
```

Do not commit actual local bridge URLs, tokens, or AiMaMi relay settings.

## Example route / 示例路由

```text
User: 检查 CAD 和 SU 是否对得上，准备出渲染。

1. cadq/autocad_mcp: confirm CAD units/extents/key dimension.
2. SketchUp QA: inspect imported CAD reference, hidden outliers, scale.
3. Export visual proof: top plan + white-model perspectives.
4. visual_asset_index: record assets and QA status.
5. If passed: Enscape/AI Render/imagegen route.
6. If failed: model cleanup V_next, no render.
```
