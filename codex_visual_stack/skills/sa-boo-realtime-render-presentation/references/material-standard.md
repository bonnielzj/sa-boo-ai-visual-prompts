# Material Standard

## Material priorities

1. Correct scale.
2. Correct roughness/glossiness.
3. Correct bump/normal depth.
4. Correct edge/detail treatment.
5. Correct color under project lighting.

## SA&BOO material language

| Material | Visual rule |
|---|---|
| Stone | avoid tile repetition; show veining scale and slab direction |
| Wood | align grain direction with real installation; avoid orange saturation |
| Metal/chrome | controlled reflection, not full mirror unless designed |
| Silk/textile | soft anisotropic feeling; avoid plastic shine |
| Glass | slight tint/reflection; check transparency and edge thickness |
| Paint/plaster | subtle roughness, not flat digital color |
| Leather | fine grain and controlled highlight |

## PBR map checklist

- Base color/albedo.
- Roughness.
- Normal/bump.
- Metallic when applicable.
- Displacement only when needed and performance allows.
- Opacity/translucency for glass/fabric if needed.

## Material option workflow

Create option states:

```text
Option A: calm ivory / warm stone / champagne metal
Option B: darker ink / stronger bronze / dramatic contrast
Option C: color accent / art-forward / social-media impact
```

Keep camera and light identical when comparing options.

## Avoid

- Random downloaded material with wrong scale.
- Stock marble everywhere.
- Over-reflective floors.
- Over-clean surfaces without bevels/shadows.
- Mismatch between render material and actual supplier sample.

## Client-safe note

Use this sentence in proposals when needed:

```text
效果图用于呈现空间氛围与材质方向，最终颜色、纹理、反光与施工节点以材料实样、施工图及现场条件为准。
```
