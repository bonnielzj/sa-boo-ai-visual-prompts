# SA&BOO 2026 AI视觉口令包

这是 SA&BOO / Bonnie 的 AI 视觉口令资料仓库，用于文字转图片、视觉风格探索、品牌视觉、室内概念图、小红书封面、提案视觉、产品KV 与 Figma / Canva / MCP 工作流。

## 内容

- `00_使用说明.md`
- `01_2026视觉趋势转译.md`
- `02_Prompt操作系统.md`
- `03_可直接复制风格口令库.md`
- `04_平台适配指南.md`
- `05_MCP与工具路线.md`
- `06_一页速查表.md`
- `source_skill_files/`：原始 skill 资料备份

## 使用原则

- 不复制趋势，而是把趋势转译为可控视觉变量。
- 不只写“高级感”，必须写清：材质、光线、构图、留白、镜头、颜色与约束。
- 文字多的画面，建议先生成背景/主体，再在 Figma、Canva 或 PPT 中排版。

## Codex Skills Backup

本仓库已追加 `codex_skills/`，用于备份和协作以下已经强化过的 SA&BOO AI 视觉 skills：

- `sa-boo-visual-style-prompt-lab`
- `sa-boo-prompt-translator`
- `sa-boo-style-mixer`
- `sa-boo-design-research-radar/references/mcp-reserve.md`

同时追加 `automation_notes/weekly_update_sa_boo_prompt_mcp.md`，记录每周自动更新 SA&BOO 视觉 Prompt 与 MCP 储备的任务说明。

## 视觉资产链表与向量索引

本仓库现在不仅包含 Markdown 口令，还包含本地视觉资产索引系统：

- `visual_assets/visual_asset_linked_list.md`：可浏览的本地缩略图链表
- `visual_assets/asset_graph.json`：节点 + 边的视觉资产图谱
- `visual_assets/cache/thumbs/`：低分辨率本地预览图，避免外链失效
- `vector_index/visual_asset_vectors.json`：本地文本语义向量索引
- `scripts/search_visual_assets.py`：命令行语义搜索工具

示例：

```bash
python3 scripts/search_visual_assets.py "Texture Check 触觉材质"
python3 scripts/search_visual_assets.py "dark chrome retrofuture 液态银"
python3 scripts/search_visual_assets.py "戏剧感 小红书封面 聚光灯"
```

版权边界：第三方视觉缓存仅用于内部研究和索引，不作为自有商用素材直接再分发。


## Codex Visual Stack Backup / 视觉工作流备份包

本仓库新增 `codex_visual_stack/`，用于同步 Bonnie Codex 中与视觉、室内、CAD、SketchUp、渲染、Figma、Prompt、视觉资产链相关的 skills 与工作流。

包含：

- `codex_visual_stack/skills/`：72 个视觉相关 Codex skill 备份，包含真实 `SKILL.md`、references、scripts（已排除密钥、缓存、大型专有二进制）。
- `codex_visual_stack/mcp_templates/`：MCP / key / URL 占位模板，所有敏感值均为 `${PLACEHOLDER}`。
- `codex_visual_stack/visual_chains/`：视觉资产链表、manifest、asset graph、vector index 示例。
- `codex_visual_stack/project_examples/logicat_r16/`：Logicat R16 项目的非空 QA 视觉链样例，含 PNG、JSON 链表和 QA 报告。
- `codex_visual_stack/manifests/visual_skills_manifest.json`：可检索 skill 清单。

安全边界：不要提交真实 API key、token、私密 relay URL、`auth.json`、`secrets.json`、客户私密 CAD/SKP/DWG。模板中的 key/url 需要在本地私有配置中填写。
