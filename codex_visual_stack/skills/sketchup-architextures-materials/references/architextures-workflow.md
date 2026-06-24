# Architextures material workflow reference

## Best interior-design uses

- Tile studies: square, subway, terrazzo, mosaic, stone-look, grout variants.
- Wood flooring: straight plank, herringbone, parquet-like patterns.
- Stone/concrete/plaster wall and floor finishes.
- Brick/block/paver concept surfaces.
- Wallpaper, carpet, acoustic felt, and repeating fabric-like finishes.
- Fast white-model-to-material concept render studies.

## Decision matrix

| Need | Prefer |
|---|---|
| Seamless pattern-controlled finish | Architextures |
| Photoreal scanned PBR material/HDRI/model | Poliigon |
| Flat paint/brand/RAL-like color | DBUR ColorMaker |
| Batch material replacement | TT Material Replacer |
| Rotate/align wood grain, stone vein, tile direction | Eneroth Texture Positioning |
| Actual panel/tile grooves, thickness, or seams | MyPanelGrid / Profile Builder / native modeling |
| Final renderer-specific shader tuning | D5/Enscape/V-Ray/Twinmotion material editor |

## Material setup checklist

- Define real dimensions before import: tile size, plank width/length, brick module, grout width.
- Pick material naming convention before applying multiple options.
- Keep concept materials and final materials separate when possible.
- Record source: Architextures material name/link if client/commercial deliverables need provenance.
- Check if free vs paid/pro features affect usage rights or map resolution.

## Recipes

### Tile or stone floor option

1. Decide module size: e.g. 600x600, 300x600, herringbone plank, mosaic.
2. Create/import the Architextures material at real-world dimensions.
3. Apply to floor group/face.
4. Use Texture Positioning to align a tile centerline or doorway threshold.
5. If grout needs physical shadow/gap, add MyPanelGrid or modeled grooves for close-up render.
6. Save material option scenes or duplicate material variants.

### Feature wall material

1. Define wall face and orientation.
2. Choose brick/stone/plaster/wallpaper pattern.
3. Import at correct scale.
4. Align horizontal datum, pattern start, or centerline with Texture Positioning.
5. Add trim/frame with Profile Builder or native geometry if visible.
6. Use Material Replacer for A/B/C palette swaps.

### White model to material concept

1. Start with clean white model groups: floor, wall, ceiling, built-ins, furniture blocks.
2. Assign broad material families: wood, stone, plaster, fabric, metal.
3. Use Architextures only where repeat scale matters.
4. Use ColorMaker for paint/color-only surfaces.
5. Export camera views to AI Render/D5/Enscape after material scale QA.

## QA checklist

- **Scale:** pattern module matches real-world dimensions.
- **Direction:** wood grain/stone vein/tile direction aligns with design intent.
- **Repeat:** no obvious ugly repetition in main camera views.
- **Seams:** texture seams align with architecture or are hidden; physical seams modeled when needed.
- **Organization:** material names include source/family/size/version.
- **Rights:** note Architextures source and subscription/free-use limits for commercial work.

## Good trigger requests

- “用 Architextures 做一版 600x600 微水泥瓷砖材质方案。”
- “这个木地板纹理应该怎么设置尺寸和方向？”
- “判断这个材质用 Architextures、Poliigon 还是 ColorMaker。”
- “帮我做白模到硬装材质概念的 SU 工作流。”
- “这个墙纸/砖/石材纹理怎么避免比例错误和重复感？”
