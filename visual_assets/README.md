# Visual Assets｜本地视觉资产链表与索引

本目录把原本的 Markdown 口令升级为：

```text
原视觉资产引用 → 本地低分辨率预览缓存 → 元数据 → 文本向量索引 → 视觉资产链表/图谱 → Prompt 配方
```

## 重要版权边界

- `cache/thumbs/` 保存的是低分辨率 research preview，用于内部学习、索引和风格检索。
- `cache/original/` 默认不提交第三方高清原图，仅保留 `.gitignore`；如有授权素材可手动放入。
- 第三方图片不应作为 SA&BOO 自有商业素材直接复用或再分发。
- 真正商用时，请使用自有素材、授权图库、客户授权图片，或重新生成/拍摄。

## 核心文件

| 文件 | 作用 |
|---|---|
| `visual_asset_manifest.jsonl` | 主资产表，一行一个节点 |
| `visual_asset_manifest.json` | JSON数组版，方便程序读取 |
| `visual_asset_manifest.csv` | 表格版，可导入 Notion / Airtable |
| `visual_asset_gallery.md` | 远程引用画廊 |
| `visual_asset_linked_list.md` | 本地缩略图链表，可直接在 GitHub 中浏览 |
| `asset_graph.json` | 节点 + 边的图谱结构 |
| `cache/thumbs/` | 本地低分辨率缩略图 |
| `cache/original/` | 默认不提交第三方高清原图；授权素材可放入 |
| `cache/cache_manifest.json` | 缓存状态、尺寸、hash |

## 链表/图谱结构

`asset_graph.json` 中：

- `nodes`：视觉资产节点
  - `id`
  - `platform`
  - `trend`
  - `source_url`
  - `asset_url`
  - `local_thumbnail`
  - `local_original_cache`
  - `sha256`
  - `perceptual_hash_proxy`
  - `visual_mechanism`
  - `sa_boo_translation`
  - `prompt_tags`
- `edges`：关系边
  - `next_in_platform`
  - `prev_in_platform`
  - `semantic_related`
  - `prompt_recipe_reference`

## 语义检索

```bash
python3 scripts/search_visual_assets.py "液态银 dark chrome retrofuture"
python3 scripts/search_visual_assets.py "Texture Check 触觉材质 glass wax"
python3 scripts/search_visual_assets.py "小红书 戏剧感 封面"
```

## 重新缓存图片

```bash
python3 scripts/cache_visual_assets.py
python3 scripts/build_asset_graph.py
```

## 当前覆盖范围

- Canva 2026 趋势：10 个趋势节点；由于官方趋势图没有稳定公开直图，暂以趋势页节点保存，可后续补截图。
- Adobe 2026 Creative Trends：4 张视觉参考已缓存。
- Figma 2026 Web Trends：15 张视觉参考已缓存。
- Figma MCP：4 张工具流程视觉已缓存。
- Canva MCP：1 张工具流程视觉已缓存。

