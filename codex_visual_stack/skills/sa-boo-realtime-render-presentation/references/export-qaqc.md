# Export and QA Standard

## Export sizes

| Use | Ratio | Recommended size |
|---|---|---|
| Proposal PDF | 16:9 | 1920×1080 or 2560×1440 |
| Proposal detail / print | flexible | 3000px+ long edge if possible |
| A4 page image | A4 | 2480×3508 px for 300dpi equivalent when needed |
| Xiaohongshu cover | 3:4 | 1080×1440 or 1242×1660 |
| Douyin/Reels cover | 9:16 | 1080×1920 |
| Behance hero | wide | 1920×1080 / 2560×1440 |
| Website case | responsive | 1600-2400px wide variants |

## File package

```text
/RENDER_EXPORT
  /STILLS
  /BEFORE_AFTER
  /VIDEO
  /PANORAMA
  /FIGMA_READY
  /SOURCE_SCREENSHOTS
  shot_log.csv
  qa_checklist.csv
```

## Shot log fields

```text
Shot No, File Name, Tool, Camera, Scene State, Lighting Story, Material Option, Purpose, Status, Notes
```

## QA checklist

- [ ] Correct project and revision/date.
- [ ] Correct camera names and sequence.
- [ ] No missing textures.
- [ ] No floating assets or intersecting furniture.
- [ ] No repeated people/assets distracting from design.
- [ ] Reflections controlled.
- [ ] Exposure consistent.
- [ ] Before/after pairs aligned.
- [ ] Export size matches platform.
- [ ] Disclaimer added for concept renders.
- [ ] Client privacy checked.

## Proposal disclaimer

```text
本页效果图用于表达空间氛围、比例关系与材质方向；最终施工尺寸、节点、色差、纹理与安装方式以施工图、材料实样及现场复核为准。
```

## Figma/PDF packaging

For each render pack, create:

- 1 cover image.
- 1 before/after page.
- 1 material detail page.
- 1 lighting scene page.
- 1 annotated decision page.

Use `sa-boo-figma-brand-kit` for page templates.
