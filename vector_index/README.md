# Vector Index｜视觉资产向量索引

此目录包含 `visual_asset_vectors.json`，由 `visual_assets/visual_asset_manifest.jsonl` 中的 caption、趋势、标签、SA&BOO转译文字生成。

- 向量类型：hashed TF-IDF sparse vector
- 维度：512
- 优点：无需外部API，可离线运行，可提交到GitHub。
- 限制：不是CLIP图像向量，也不是OpenAI embedding；它是文本语义索引，适合快速检索视觉资产引用。

运行搜索：

```bash
python3 scripts/search_visual_assets.py "液态银 dark chrome"
python3 scripts/search_visual_assets.py "Texture Check 触觉材质"
python3 scripts/search_visual_assets.py "小红书 戏剧感 封面"
```
