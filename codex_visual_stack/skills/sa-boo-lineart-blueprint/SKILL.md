---
name: sa-boo-lineart-blueprint
description: SA&BOO technical line-art and blueprint prompt workflow for product design sketches, jewelry, handbags, furniture, mechanical flowers, robotic devices, packaging structures, fashion accessories, and concept design sheets. Use when the user asks for line drawing, hand draft, blueprint, technical annotation, multi-angle design sketch, vector-ready commercial line art, or product development AI prompts. Must follow SA&BOO visual-first rule - prioritize a high-quality visual asset chain and use text as interpretation when applicable.
---

# SA&BOO Lineart Blueprint

## SA&BOO visual-first hard rule

- Treat `sa-boo-visual-first-core` as the governing rule for SA&BOO work: build or cite a high-quality visual asset chain before writing long text whenever the task involves design learning, research, style, proposal, prompt, rendering, CAD/FF&E assets, or project review.
- Use `sa-boo-visual-asset-index` when assets must be cached, cited, tagged, linked, or searched.
- Reject low-quality assets: blurry, unreadable, over-compressed, unattributed, aesthetically weak, irrelevant, or legally unsafe. **宁缺毋滥。**
- Keep the method efficient: do not force irrelevant images into quick text-only answers; for substantial outputs, include asset IDs, thumbnails/paths, sources, rights status, and quality notes.
- Let text serve the visuals: summarize, compare, decide, and translate; do not replace visual evidence with pure prose.

Generate product/design prompts as refined technical design drawings: clear linework + annotations + multi-angle views + material/process notes.

## Style DNA

- Technique: hand draft, sketch, doodle, technical blueprint, fine black line art, pen drawing, vector-ready outline.
- Information: dimensions, material notes, craft explanation, exploded view, curved-surface expansion, stitching/panel map, mechanism annotations.
- Composition: main view + side view + 3/4 view + scattered detail thumbnails + measurement lines.
- Quality: clean white or blueprint paper background, precise line hierarchy, commercial print standard, no jagged edges.
- Suitable objects: jewelry, brooch, bag, furniture, robotic arm, engine, mechanical flower, installation, packaging.

## Workflow

1. Identify object and function.
2. Decompose structure: silhouette, parts, joints, material, manufacturing logic.
3. Add views: front, side, 3/4, detail close-ups, exploded parts.
4. Add annotation language: dimensions, materials, operations, craft notes.
5. Choose style level:
   - clean luxury sketch
   - industrial blueprint
   - Moebius sci-fi complexity
   - Victorian ornamental linework
   - commercial vector icon

## Chinese prompt skeleton

```text
{主体}的产品设计线稿/技术蓝图，白色背景，黑色精细线描，线条清晰、精准、流畅，包含正视图、侧视图、四分之三视图、局部结构放大图与零散缩略图。加入尺寸标注、材料说明、工艺注释、结构拆解线、测量线。整体呈现高级产品研发手稿质感，比例协调，细节丰富但画面干净，可直接转矢量图，商业印刷级，高清，边缘无锯齿。
```

## English prompt skeleton

```text
technical product blueprint of {subject}, refined black line art on clean white background, precise and elegant hand-drafted design sketch, front view, side view, three-quarter view, exploded details, measurement lines, material annotations, craft notes, structural callouts, clear line hierarchy, vector-ready commercial illustration, high-resolution, crisp edges, no shadows.
```

## Useful vocabulary

- 手稿: hand draft
- 草图: sketch / doodle
- 网格系统: grid system
- 字体: typography
- 色彩: color system / color spectrum
- 辅助图形: auxiliary graphics
- 图案: pattern / textile
- 图形: 2D graphics
- 转译: translate into
- 符号化: symbolize
- 简化: simplify
- 优化: refine
- 锐化: sharpen

## Negative constraints

No photorealistic rendering unless requested. Avoid messy handwriting, unreadable annotations, random brands, watermark, chaotic background, low-resolution lines.
