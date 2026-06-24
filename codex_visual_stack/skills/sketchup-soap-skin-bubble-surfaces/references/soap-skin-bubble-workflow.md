# Soap Skin Bubble workflow reference

## Best interior-design uses

- Tensile fabric canopies and sail-like interior installations.
- Soft curved ceilings, acoustic clouds, membrane ceiling features.
- Bubble/dome forms for reception features, display niches, kids-space elements, spa/relaxation rooms.
- Curved wall panels, soft padded panels, organic room dividers.
- Furniture shell studies: lounge chair shells, curved headboards, cushion-like forms.
- White-model concept studies where a boundary loop needs to become a soft surface.

## Decision matrix

| Need | Prefer |
|---|---|
| Skin from a closed boundary loop | Soap Skin Bubble |
| Bubble/inflated membrane from a boundary | Soap Skin Bubble |
| Sculpt and smooth an existing mesh | Artisan |
| Bend a straight object precisely | TrueBend |
| Free-form deform an existing grouped object | SketchyFFD |
| Generate repeatable hard strips/profiles | Profile Builder or MyPanelGrid |
| Clean broken boundary/CAD edges first | Edge Tools² |
| Diagnose closed solid after adding thickness | Solid Inspector |
| Fix fabric/wood/stone texture direction | Eneroth Texture Positioning |

## Boundary preparation

- The input should be a clean closed loop or a well-controlled boundary curve set.
- If imported from CAD, run cleanup first: remove duplicates, close gaps, simplify overly segmented curves.
- Make boundaries larger and simpler for first tests; refine after the form direction is approved.
- Store a backup group named `SRC_SSB_Boundary_*`.
- Create generated surfaces as separate groups named `SSB_Surface_*`.

## Mesh density guidance

- **Concept preview:** low density; fastest, good for choosing direction.
- **Client white-model/render study:** medium density; enough smoothness from normal camera distances.
- **Final render/detail:** higher density if needed, but check performance.
- Avoid high-density surfaces inside repeated components or heavy rooms unless the camera needs it.

## Typical recipes

### Stretched fabric ceiling cloud

1. Draw an organic closed boundary on/near the ceiling plane.
2. Backup the boundary group.
3. Generate soap skin with low/medium density.
4. Apply slight pressure/relaxation for a soft sag or lift.
5. Smooth/soften edges.
6. Add thin edge frame separately with Profile Builder or native modeling.
7. Apply translucent fabric/acoustic felt material and fix UV direction if needed.
8. Create camera scenes for underside and perspective view.

### Bubble niche or dome feature

1. Draw circular/oval/arched boundary.
2. Generate skin.
3. Increase pressure for dome/bubble effect.
4. Check from front and side elevations.
5. Add thickness manually or via offset/solid workflow if construction detail is needed.
6. Use Solid Inspector only after closing the surface into a volume.

### Soft padded wall panel

1. Draw rectangular/arched panel boundary.
2. Divide boundary into enough segments for smooth bulge.
3. Generate and inflate mildly.
4. Duplicate for panel options with different pressure values.
5. Add seams/frames separately; do not rely on the bubble mesh for crisp construction edges.
6. Apply leather/fabric material, then use Texture Positioning to align grain/weave.

## QA checklist

- **Boundary:** closed, no duplicate edges, no tiny gaps, source backup exists.
- **Mesh:** density appropriate, no chaotic triangulation, no self-intersections.
- **Form:** pressure direction correct, silhouette reads well from main camera.
- **Integration:** edge frames, supports, seams, or thickness are modeled separately if needed.
- **Performance:** high-poly surfaces are isolated and named; unused experiments are hidden or purged.
- **Buildability:** label as concept membrane or develop a realistic construction layer strategy.

## Good trigger requests

- “用 Soap Skin Bubble 做一个张拉膜天花。”
- “这个闭合边界怎么生成柔和鼓起的软包面？”
- “我想做一个泡泡感穹顶/壁龛，SU 里怎么建？”
- “这个曲面应该用 Soap Skin Bubble、Artisan 还是 SketchyFFD？”
- “给我一个曲面天花白模到渲染的建模流程。”
