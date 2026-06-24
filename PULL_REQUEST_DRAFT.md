# PR Draft — SA&BOO Codex Visual Stack Backup

## Summary / 摘要

This PR packages Bonnie's SA&BOO Codex visual-production stack into a GitHub-synced backup and reusable reference library.

本 PR 将 Bonnie 的 SA&BOO Codex 视觉生产体系打包为可同步到 GitHub 的备份与复用型视觉工作流资料库。

## Included / 已包含

- `codex_visual_stack/skills/` — visual-related Codex skill backups.
- `codex_visual_stack/manifests/` — visual skill manifest in JSON and CSV.
- `codex_visual_stack/mcp_templates/` — MCP configuration templates with placeholder keys and URLs.
- `codex_visual_stack/visual_chains/` — real visual chain manifests, gallery, linked list, graph, and vector-like metadata.
- `codex_visual_stack/project_examples/logicat_r16/` — Logicat R16 real QA evidence chain including PNG, JSON indexes, and QA reports.
- `codex_skills/` — refined high-priority SA&BOO skill snapshots.
- `visual_assets/project_qa/logicat_r16/` — project visual QA assets for reference and reuse.

## Security / 安全处理

No real API keys, relay tokens, private URLs, or credentials are committed.

未提交真实 API key、relay token、私人 URL 或认证信息。

Placeholders are used instead:

```text
${OPENAI_API_KEY}
${GITHUB_TOKEN}
${FIGMA_ACCESS_TOKEN}
${AIMAMI_RELAY_URL}
${AIMAMI_RELAY_TOKEN}
${SKETCHUP_MCP_BRIDGE_SCRIPT}
```

## Design production logic / 设计生产逻辑

The package preserves the SA&BOO visual-first workflow:

```text
Co-design alignment
→ visual evidence
→ CAD/layout truth
→ SketchUp model proof
→ detail/model QA
→ material-light-camera proof
→ three-route output
→ image QA
→ asset index
→ next decision
```

中文：

```text
共创对齐
→ 视觉证据
→ CAD / 平面真值
→ SketchUp 模型证明
→ 重点节点 / 模型 QA
→ 材质灯光镜头证明
→ 三路出图
→ 图像 QA
→ 视觉资产归档
→ 下一轮设计决策
```

## Three output routes / 三路出图

```text
Route A — Model-native render
SketchUp / 3ds / D5 / Enscape / V-Ray / Twinmotion

Route B — AI / imagegen route
AI Render / imagegen / white-model-to-render / material-light studies

Route C — Portable prompt pack
Other agent / Midjourney / 即梦 / Stable Diffusion / Runway / human renderer
```

## Review focus / 建议审核重点

1. Check that the visual stack is not only language scaffolding but includes actual asset chains and project QA examples.
2. Confirm MCP templates use placeholders only.
3. Confirm the Logicat R16 visual chain is useful as a reusable evidence-chain example.
4. Decide whether to merge this branch as the main visual-stack baseline.

## Branch / 分支

```text
codex/sa-boo-integrated-production-loop
```
