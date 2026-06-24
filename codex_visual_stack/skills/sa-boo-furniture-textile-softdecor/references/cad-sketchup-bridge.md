# CAD / SketchUp Bridge for Furniture and Soft Decor

Use with `sa-boo-cad-sketchup-bridge`, `sa-boo-sketchup-interior-director`, and `sa-boo-autocad-construction-standard`.

## Source-of-truth rules

```text
Human dimensions and issued drawings → CAD / verified product data
Spatial massing and client visual approval → SketchUp views/renders
Material mood and texture behavior → visual assets + SketchUp/render material tests
Procurement truth → FF&E schedule / supplier documents
```

Do not let a pretty SketchUp model override verified product dimensions or clearances.

## CAD representation

### Layers

Use SA&BOO CAD standard layers where available:

- `I-FURN-FIXD-N` for fixed furniture/millwork outlines.
- `I-FURN-LOOS-N` for loose furniture/FF&E footprints.
- `I-HATCH-MATL` for rug/fabric/material zones when needed.
- `I-ANNO-TAGS` for FF&E tags, material codes, curtain/rug labels.
- `NPLT-GUIDE` for clearance/ergonomic guide circles and pull-out zones.

### 2D block minimum

A furniture CAD block should include:

- accurate footprint, not decorative lines only;
- insertion point and rotation logic;
- main clearance envelope if critical;
- tag field: `F-001`, `CH-001`, `RUG-001`, etc.;
- simple lineweight hierarchy: outline > seams/detail > guide;
- separate simplified plan block and optional elevation/detail block.

### CAD notes to preserve

- product dimensions and verified source;
- custom vs purchased;
- finish/material code;
- plug/wiring if lighting/electric furniture;
- installation/anchoring if built-in or heavy/tall.

## SketchUp component rules

### Component metadata

Name components with:

```text
FFE_Category_Tag_BrandOrSource_Size_LOD
Sofa_F001_Custom_3200x1000_LOD2
Rug_R001_Wool_3000x4000_LOD1
Curtain_CT001_Sheer_RippleFold_LOD2
```

Use tags/layers:

- `FFE_SEATING`, `FFE_TABLES`, `FFE_STORAGE`, `FFE_LIGHTING`, `FFE_RUGS`, `FFE_CURTAINS`, `FFE_DECOR`, `FFE_PROXY`, `FFE_DETAIL`.

### LOD levels

| LOD | Use | Rule |
|---|---|---|
| LOD0 | CAD/SU massing | box/proxy only, accurate footprint |
| LOD1 | white model | simplified silhouette, correct scale |
| LOD2 | design render | visible cushions, seams, legs, material zones |
| LOD3 | close-up/detail | high geometry only for hero shots |

Do not use heavy LOD3 models everywhere. Use proxies for general views.

## Textile and material mapping in SketchUp

- Use real-world texture scale: weave, bouclé, linen, leather grain, rug pile must not be oversized.
- Align wood grain, stone veins, and fabric direction intentionally.
- Separate material slots: frame, cushion body, piping, legs/base, hardware.
- For curtains, model volume and fold rhythm; avoid flat vertical planes unless in LOD0/1.
- For rugs, use thin plane + edge thickness; add pile/fiber only for close views.

## Render checkpoints

For furniture/textile-heavy interiors, produce:

1. plan-like top view showing clearances and rug/furniture relationship;
2. white-model perspective showing object scale before material seduction;
3. material close-up or board for textile/wood/stone relationships;
4. hero render with furniture hierarchy;
5. detail shot only if the construction/material detail is meaningful.

## Common CAD/SU problems

- downloaded models are wrong scale;
- component origin/axis is random;
- model has excessive hidden geometry;
- textures are embedded at low resolution or wrong scale;
- furniture blocks do not match chosen product dimensions;
- curtains/rugs are added after camera composition, causing weak softness;
- CAD tags and FF&E schedule names diverge.

When any problem appears, stop and standardize naming, dimensions, tags, and source links before continuing.
