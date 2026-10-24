# Bilingual Prompt Translation Mode

Use this mode when the request is primarily to translate, strengthen, structure, or adapt a Chinese design intention into prompts for image or video models.

## Rule

Translate design intent into controllable visual variables; do not translate words literally.

## Required output

```text
中文口令：
英文口令：
关键词：
负面词：
平台建议：
可替换变量：
参考图角色（如适用）：
保留/修改约束（如适用）：
输出规格：
```

## Variables to preserve

- purpose and subject;
- style engine and composition;
- material, texture, lighting, and palette;
- camera/render mode;
- reference-image roles;
- keep/change/remove/add contract;
- aspect ratio, size, quality, format, and background behavior;
- continuity constraints for edits.

## Useful mappings

- 高级感 → refined / premium editorial
- 弥散光 → soft diffused light
- 低调奢华 → understated luxury
- 留白 → negative space
- 符号化 → symbolic abstraction
- 线稿蓝图 → technical line-art blueprint

## Platform adaptation

- Midjourney: visual mechanism + composition + material + aspect ratio.
- Hermes image route: separate generation from edit contracts; use `bonnie-creative-backend-routing` and verify the real image backend.
- Stable Diffusion: positive and negative prompts separately.
- 即梦: retain Chinese semantic nuance and add concise English material/camera terms.
- Runway/video: add motion, camera movement, duration, transition, and subject stability.

For real retail project imagery, inherit the approved evidence and stage from `sa-boo-retail-design-partner`; label unsupported style exploration as exploration, not a project solution.
