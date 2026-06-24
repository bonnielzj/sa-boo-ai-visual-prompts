# Official Furniture Brand Study Cycle

Use this when Bonnie says to learn from major furniture brands, product websites, official downloads, CAD/SKP/DWG/Revit/BIM files, high-resolution product images, scenes, materials, or trend language.

## Priority

Treat official high-end furniture websites as **P0 learning sources** before generic model libraries, museum archives, or forums for current project delivery.

Why:

- real product dimensions and configuration logic;
- official scene images and styling systems;
- material/finish options and care notes;
- CAD/SKP/DWG/Revit/BIM/3D downloads or professional libraries;
- brand trend language and catalogue hierarchy;
- specification and procurement relevance.

## P0 brand set

Start with:

1. Baxter — leather, modular sofas, Italian tactile luxury.
2. Cassina / Cassina Pro — design icons, iMaestri, data sheets, 2D/3D, contract language.
3. Minotti — contemporary luxury proportions, sofa systems, BIM/Revit, scene styling.
4. Vitra — design classics, office/residential systems, 2D/3D CAD data, product factsheets.
5. Artek — Aalto/Nordic modernism, bentwood, stools/chairs/tables, textiles/patterns, care culture.
6. B&B Italia / Maxalto — Italian systems, sofas, product drawings/images, refined warm luxury.
7. Poliform — systems, wardrobes, sideboards, 2D DWG and 3D formats where available, finishes.

P1 additions: Molteni&C, Flexform, Giorgetti, Living Divani, Porro, Lema, HAY, Muuto, Knoll, MillerKnoll, Flos, Louis Poulsen, Artemide.

## System furniture / 全屋定制 cycle

When the brand is Poliform, USM, Molteni&C/Dada, SieMatic, Bulthaup, Boffi, Valcucine, Arclinea, Rimadesio, Porro, Lema, Modulnova, Cesar, Poggenpohl, or another system-furniture brand, read `references/system-furniture-custom-cabinetry.md` before evaluating products.

Prioritize:

1. module dimensions and size ranges;
2. carcass/front/panel/worktop/hardware construction;
3. finish/material codes and maintenance;
4. CAD/SU/Revit/BIM/3D formats;
5. elevation/section/detail implications;
6. installation tolerances and service coordination;
7. proxy vs detailed SketchUp component strategy.

## Per-brand weekly cycle

For each selected brand, collect and record:

```text
Brand:
Official URL:
Product family studied:
3-5 representative products:
Designer / year / collection:
Dimensions and modules:
Available downloads: DWG / SKP / Revit / BIM / 3DM / FBX / MAX / PDF / images
Login / access requirement:
Materials / finishes / textile / leather options:
Scene styling logic:
CAD footprint and clearance implication:
SketchUp component and LOD implication:
Render texture / camera / lighting implication:
FF&E procurement notes:
Rights status:
SA&BOO aesthetic verdict:
Rejected/generic details to avoid:
```

## Output after one brand cycle

Produce four artifacts:

1. **Brand source record** in `sources.csv`.
2. **3-10 visual asset records** through `sa-boo-visual-asset-index` when private study caching is appropriate.
3. **Object cards** in `objects.csv` for key sofas/chairs/tables/systems.
4. **Aesthetic note** explaining what SA&BOO should learn from the brand and what not to copy.

## CAD / SketchUp download hygiene

- Prefer official brand downloads over random 3D Warehouse models.
- Record source URL and access date next to every file.
- Verify units and scale after import.
- Store heavy detailed models separately from proxy/LOD versions.
- Make a lightweight CAD/SU proxy if the official model is too heavy.
- Never use login-gated or copyrighted files outside permitted contexts.

## Rights rule

Brand images, CAD, SKP, Revit, BIM, catalogues, and material images are usually copyright or supplier-controlled. Mark them as `supplier-reference` or `reference-only` unless the brand terms explicitly permit broader use. Use them for private learning, specification, and authorized project workflow; do not reuse publicly without permission.
