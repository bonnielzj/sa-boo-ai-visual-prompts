# SC071 Source Index

Use this reference when you need to understand or query the vectorized source asset library.

## Source library

- Mounted source root: `/Volumes/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+`
- SMB source: `smb://SABOO_STUDIO1._smb._tcp.local/homes/saboo内部学习资料/SC071—135个通用户型平面布局优化方案2000+`
- Indexed on: 2026-06-20

## Vectorized artifacts

The skill stores a local retrieval layer, not just text notes:

- `assets/index/cases.jsonl`: 135 case records with case-level vectors.
- `assets/index/assets.jsonl`: 2,973 source asset records with asset-level vectors and source paths.
- `assets/index/manifest.json`: build metadata and counts.
- `assets/index/contact_sheets/*.jpg`: visual overview sheets.

Vector dimensions:

- `semantic_vector`: 128 deterministic metadata/design-intent dimensions.
- `visual_vector`: 32 lightweight image/file-geometry dimensions.
- `vector`: 160 combined dimensions used by `scripts/query_index.rb`.

Each record keeps source attribution fields: `path`, `smb_url`, `case_name`, `file_name`, `file_role`, `quality_signal`.

## Library statistics

- Cases: 135
- Assets: 2,973
- Images: 2,950
- Extensions: `.jpg` 1,815; `.png` 1,135; `.pdf` 22; `.dwg` 1
- Typologies: 平层 83; 别墅 19; 复式 14; 大平层 13; 异型平层 4; 未标注 2
- Area buckets: `<50㎡` 2; `50-79㎡` 11; `80-119㎡` 13; `120-159㎡` 36; `160-219㎡` 30; `220-399㎡` 19; `400㎡+` 23; 未标注 1
- Role labels: 主讲/推导方案 56; 优秀案例 156; 其他案例 149; 原始/建筑图 77; 反例 66; 普通方案 2,469

## Retrieval commands

Run from the skill directory or pass absolute script path:

```bash
ruby -EUTF-8:UTF-8 scripts/query_index.rb --query "70㎡ 一居 小户型 收纳 优秀案例" --scope both --quality positive -n 8
ruby -EUTF-8:UTF-8 scripts/query_index.rb --query "135㎡ 3+1 改善型 家政 套房 反例" --scope both --area-min 120 --area-max 160 -n 8
ruby -EUTF-8:UTF-8 scripts/query_index.rb --query "复式 楼梯 上下层 动静分区" --scope cases --typology 复式 -n 6
ruby -EUTF-8:UTF-8 scripts/query_index.rb --query "别墅 多层 家政 动线" --scope both --typology 别墅 -n 8
```

Use `--json` when you need machine-readable results.

## Record fields

Important fields in `assets.jsonl`:

- `id`: stable asset id.
- `path`: local mounted path for opening/inspection.
- `smb_url`: network source location.
- `case_name`, `case_id`: parent case.
- `area_m2`, `area_bucket`, `typology`, `bedroom_count`, `plus_room`.
- `file_role`: `原始/建筑图`, `主讲/推导方案`, `优秀案例`, `反例`, `其他案例`, `方案`, or `广告/无关`.
- `quality_signal`: `positive`, `negative`, `neutral`, or `ignore`.
- `width`, `height`, `ext`, `bytes`.
- `semantic_vector`, `visual_vector`, `vector`.

Important fields in `cases.jsonl`:

- `representative_assets`: top source assets to open first.
- `by_role`, `by_ext`: source composition.
- `vector`: case-level retrieval vector.

## High-signal study sets

### 小户型正反例

- `34㎡一居室平层（40稿方案）`: 6 反例, 9 主讲/推导方案, 25 其他案例.
- `65㎡一居室平层（27稿方案）`: 6 优秀案例, 10 反例.
- `67㎡一居室平层（36稿方案）`: 原始图 + 3 主讲方案 + 30 优秀案例 + 3 反例.
- `70㎡一居室平层（24稿方案）`: 原始图 + 3 主讲方案 + 8 优秀案例 + 13 其他案例.
- `73㎡一居室平层（25稿方案）`: 3 反例 + 多个其他案例.

### 中大平层正反例

- `135㎡3+1房平层（25稿方案）`: 19 优秀案例 + 3 反例.
- `153㎡3+1房平层（17稿方案）`: 原始图 + 优秀案例 + 多方案.
- `173㎡三居室平层（27稿方案）`: 2 主讲方案 + 18 优秀案例 + 9 反例.
- `214㎡3+1房平层（22稿方案）`: 原始图 + 主讲方案 + 优秀案例 + 反例.

### 复式 / 别墅 / 大平层 / 异型

- `1+1异型平层（47稿方案）`: 原始图 + 主讲方案 + many variants; use for斜墙/不规则边界.
- `212㎡复式（9稿方案）`, `251㎡复式（24稿方案）`, `276㎡复式（9稿方案）`: use for楼梯、上下层、动静分区; 251㎡ and 276㎡ contain positive/negative signals.
- `371㎡小别墅（18稿方案）`, `460㎡小别墅户型（5稿方案）`, `720㎡别墅（10稿方案）`, `780㎡别墅（9稿方案）`: use for别墅多层、多动线、服务/家政体系.
- `378㎡大平层（14稿方案）`, `489㎡大平层（23稿方案）`, `500㎡大平层（17稿方案）`: use for大平层横厅、套房、洄游、尺度控制.

## Contact sheets

Open these for quick visual orientation:

- `assets/index/contact_sheets/small-space-positive-negative.jpg`
- `assets/index/contact_sheets/mid-large-improvement.jpg`
- `assets/index/contact_sheets/special-typologies-duplex-villa-largeflat.jpg`

## Citation rule

When using this skill in client-facing answers, cite source cases/assets as local paths or SMB URLs. Example:

- Source: `/Volumes/homes/.../70㎡一居室平层（24稿方案）/05优秀案例6-01.png`
- Why relevant: 70㎡ one-bedroom positive precedent for compact storage + public-zone integration.
