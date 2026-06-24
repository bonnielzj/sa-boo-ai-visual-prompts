# SA&BOO CAD Layer Standard

## Naming pattern

Use ASCII layer names to avoid broken fonts/xrefs across systems:

```text
{DISCIPLINE}-{MAJOR}-{MINOR}-{STATUS}
```

Examples:

```text
I-WALL-FULL-N      interior new full-height wall
I-WALL-DEMO-D      interior demolition wall
I-DOOR-SWNG-N      interior new door swing
I-FURN-FIXD-N      fixed millwork/furniture
I-CEIL-GRID-N      ceiling grid/ceiling outline
E-LITE-FIXT-N      lighting fixture
I-ANNO-DIMS        dimensions
I-REV-CLOUD-R01    revision cloud for R01
```

## Discipline codes

| Code | Meaning | Use |
|---|---|---|
| I | Interior | most SA&BOO interior elements |
| A | Architecture | base building, structure-visible architectural items |
| E | Electrical | lighting, power, switch, low voltage |
| P | Plumbing | water, drain, sanitary fixtures |
| M | Mechanical | HVAC, exhaust, AC coordination |
| F | Furniture/FF&E | loose furniture and styling items if separated from I |
| X | External reference | xrefs, survey/base imports |
| NPLT | Non-plot | construction guides, notes not for issue |

## Status codes

| Code | Meaning | Graphic rule |
|---|---|---|
| N | New/proposed | normal black/plot lineweight |
| E | Existing | lighter/gray or thin |
| D | Demolition | dashed, red/orange in working file, thin when plotted if required |
| F | Future | phantom/dash-dot |
| T | Temporary | dash-dot or special note |
| R | Revision/change | cloud/delta/highlight only |

## Recommended layers

| Layer | Color | Lineweight | Linetype | Plot | Use |
|---|---:|---:|---|---|---|
| I-WALL-FULL-N | 7 | 0.35 | Continuous | Yes | cut walls / main partitions |
| I-WALL-LITE-N | 8 | 0.18 | Continuous | Yes | low partitions / glass / lightweight outlines |
| I-WALL-DEMO-D | 1 | 0.18 | DASHED | Yes | demolition walls |
| I-DOOR-PANL-N | 3 | 0.25 | Continuous | Yes | door panels |
| I-DOOR-SWNG-N | 3 | 0.13 | Continuous | Yes | door swing arcs |
| I-WIND-GLAZ-N | 4 | 0.18 | Continuous | Yes | windows/glazing |
| I-FURN-FIXD-N | 2 | 0.25 | Continuous | Yes | fixed furniture/millwork |
| I-FURN-LOOS-N | 9 | 0.13 | Continuous | Yes | loose FF&E reference |
| I-FLOR-FINI-N | 6 | 0.13 | Continuous | Yes | floor finish boundaries/patterns |
| I-CEIL-EDGE-N | 5 | 0.18 | Continuous | Yes | ceiling edges and soffits |
| I-CEIL-GRID-N | 8 | 0.09 | Continuous | Yes | ceiling grid/light guides |
| E-LITE-FIXT-N | 30 | 0.18 | Continuous | Yes | lighting fixtures |
| E-SWCH-SYMB-N | 30 | 0.18 | Continuous | Yes | switches |
| E-POWR-OUTL-N | 1 | 0.18 | Continuous | Yes | sockets/power/data outlets |
| P-PLMB-FIXT-N | 140 | 0.18 | Continuous | Yes | sanitary fixtures/drains |
| M-HVAC-DIFF-N | 151 | 0.18 | Continuous | Yes | diffusers, vents, AC |
| I-HATCH-CUT | 8 | 0.09 | Continuous | Yes | cut hatches / material hatches |
| I-HATCH-MATL | 9 | 0.09 | Continuous | Yes | material pattern/hatch |
| I-ANNO-DIMS | 2 | 0.18 | Continuous | Yes | dimensions |
| I-ANNO-TEXT | 7 | 0.18 | Continuous | Yes | general notes/text |
| I-ANNO-LEAD | 2 | 0.18 | Continuous | Yes | leaders |
| I-ANNO-TAGS | 4 | 0.18 | Continuous | Yes | room/material/door tags |
| I-ANNO-SYMB | 4 | 0.18 | Continuous | Yes | section/elevation/detail symbols |
| I-AXIS-GRID | 8 | 0.13 | CENTER | Yes | axis/grid lines |
| I-REV-CLOUD-RXX | 1 | 0.25 | Continuous | Yes | revision clouds, rename per revision |
| I-REV-DELT-RXX | 1 | 0.25 | Continuous | Yes | delta triangles/revision marks |
| I-TTLB-LINE | 7 | 0.25 | Continuous | Yes | title block/borders |
| I-TTLB-TEXT | 7 | 0.18 | Continuous | Yes | title block text |
| X-BASE-ARCH | 8 | 0.09 | Continuous | Yes | base building xref geometry |
| X-UNDERLAY | 8 | 0.05 | Continuous | Yes | consultant underlays |
| NPLT-GUIDE | 6 | 0.05 | Continuous | No | guides/construction lines |
| NPLT-VPORT | 6 | 0.00 | Continuous | No | layout viewports |

## Plot hierarchy

- 0.50/0.35: cut objects and most important construction boundaries.
- 0.25: visible object outlines and fixed millwork.
- 0.18: annotations, dimensions, doors, furniture, electrical/plumbing symbols.
- 0.13: light objects, grids, swing arcs, loose furniture, reflected ceiling grid.
- 0.09: hatches, underlays, texture/patterns.

## Layer discipline rules

- Never draw everything on `0` or `Defpoints`.
- Keep xrefs on `X-*` layers and set xref colors/lineweights lighter than active design layers.
- Put temporary construction lines on `NPLT-*` layers and confirm they do not plot.
- Do not use Chinese layer names in issued files unless the project standard requires it.
- Do not explode blocks just to change layer color; fix block content or layer properties.
