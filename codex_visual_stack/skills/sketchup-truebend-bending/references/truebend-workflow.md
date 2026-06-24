# TrueBend workflow reference

## Best interior-design uses

- Curved skirting, crown moulding, trims, picture rails, architraves.
- Curved slat walls, grille screens, ribbed panels, linear ceiling baffles.
- Curved reception/counter fronts, banquette bases, cabinet decorative strips.
- Arches, semicircular portals, curved wall caps, niche trims.
- White-model massing where a straight block or linear assembly needs to become an arc.
- Furniture ribs and repeated parts that must keep approximate length while bending.

## Decision matrix

| Need | Prefer |
|---|---|
| Precise simple arc, preserve original length | TrueBend |
| Straight profile/assembly generation first | Profile Builder, then TrueBend on a copy |
| Free-form warp, non-uniform bend, bulge | SketchyFFD |
| Soft sculptural furniture or smoothed mesh | Artisan |
| Surface membrane / tensile skin | Soap Skin Bubble |
| Clean broken imported CAD lines before bending | Edge Tools² |
| Check solid/manifold after bending | Solid Inspector |
| Batch material scheme after bending | TT Material Replacer |
| Fix wood/stone/fabric direction after bending | Eneroth Texture Positioning |

## Geometry preparation notes

- TrueBend works on one selected group/component. If multiple elements must bend together, group them into one parent group first.
- The bend length is based on the object's X-axis extent. If the object refuses to bend or reports zero distance, rotate/re-axis/rebuild so the long direction is along local X.
- Add lengthwise subdivisions before bending. A rectangular prism with only end faces cannot become a smooth arc; it needs intermediate edges/faces.
- Components inside the bent group may deform as raw geometry only if exploded/nested appropriately. Test with a copy before applying to complex nested assets.
- For profile assemblies, keep one straight source component named `SRC_*` and create bent option copies named `TB_*`.

## Suggested workflow recipes

### Curved wall trim / skirting

1. Build a straight trim with Profile Builder or native push/pull.
2. Make it a group/component and align its length to local X.
3. Segment along length according to visual smoothness: more segments for tight radius.
4. Duplicate and name the copy `TB_Skirting_R_or_Angle_01`.
5. Apply TrueBend to target angle.
6. Check intersections at wall ends; trim/cut manually if needed.
7. Reapply/fix material direction.

### Curved slat wall

1. Model one slat or an array of slats as a single parent group.
2. Ensure vertical slats have enough horizontal segmentation if their faces must bend; simple rectangular slats can also be arrayed after building a curved guide depending on detail level.
3. Bend the parent group with TrueBend.
4. Inspect spacing from plan view; spacing may visually compress on the inner radius and open on the outer radius.
5. Use Skatter/Profile Builder/manual array for final high-count details if the bent group gets too heavy.

### Arched or semicircular decorative strip

1. Create a straight strip/profile with adequate length.
2. Group, set length on X, duplicate backup.
3. Bend to 180° for semicircle or 90° for quarter arch.
4. Verify radius and endpoints; scale or rebuild if architectural dimension must be exact.
5. Use Curic Align View or section/elevation scene to check the elevation outline.

## QA checklist

- **Before:** backup straight source, single group/component, local X axis correct, enough subdivisions.
- **During:** angle typed or visually controlled, bend direction correct, object not inverted.
- **After:** faces intact, no self-intersection, no tiny broken faces, normals acceptable, material orientation acceptable.
- **Performance:** use enough segments for render smoothness but avoid unnecessarily heavy assemblies.
- **Documentation:** save scene or version copy for each option; name result with angle/radius intent.

## Prompting Codex for this workflow

Good user requests that should trigger this skill:

- “把这个直线格栅变成弧形背景墙，保持长度。”
- “我想用 SU 做一个 90 度弯曲线脚，怎么准备模型？”
- “TrueBend、SketchyFFD、Artisan 这几个弯曲工具应该用哪个？”
- “给我一个曲面柜台前脸的 SU 建模步骤。”
- “白模里这条线性体块需要弯成半圆拱。”
