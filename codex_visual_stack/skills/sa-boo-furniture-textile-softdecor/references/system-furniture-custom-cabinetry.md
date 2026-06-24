# System Furniture / Full-Home Custom Cabinetry Knowledge

Use this when learning or specifying **全屋定制**, system furniture, kitchens, wardrobes, walk-in closets, wall panels, bookcases, storage systems, modular casegoods, partition/door systems, or professional CAD/SU/Revit/BIM/3D product libraries.

## Scope

System furniture is not “loose furniture enlarged.” It is an architectural layer between interior construction and FF&E:

```text
architecture shell → wall/ceiling/floor constraints → system modules → doors/panels/hardware → appliance/lighting/MEP → finishes/materials → CAD/SU/BIM → procurement/installation
```

Core families:

- kitchens: base units, wall units, tall units, islands, peninsulas, pantries, appliance towers, sink/cooktop zones;
- wardrobes/closets: hinged, sliding, coplanar, walk-in, open closet, glass/metal systems;
- living systems: bookcases, wall systems, media/storage, sideboards, shelving;
- wall/door systems: sliding partitions, wall panels, boiserie, concealed doors;
- modular object systems: USM-like grid systems, modular shelving/casegoods;
- hybrid systems: bath, utility, outdoor kitchen, display/wine/bar systems.

## P0 system furniture brands

| Brand | Learn first | CAD/SU/3D note |
|---|---|---|
| Poliform | wardrobes, systems, sideboards, kitchens, refined finishes | product pages may expose 2D DWG and 3D formats such as 3DM/FBX/MAX |
| USM | modular grid, Haller storage, office/home systems | official architect support lists AutoCAD 2D/3D, SketchUp, Revit/BIM; BIMobject/pCon routes |
| Molteni&C / Dada Engineered | kitchens, Gliss Master, 505/Logos systems, wardrobes | A&D area / BIMobject; DWG drawings, technical sheets, finishes, kitchens |
| Alias | modular systems, tables/seating with downloadable 2D/3D product files | some product pages expose Product Sheet, Collection Sheet, 3D_3DS, 3D_DWG, 3D_FBX, 2D_DWG |
| SieMatic | premium kitchens, product lines, material/color systems, interior fittings | prioritize material/color, product-line and kitchen-planner logic; CAD/downloads may be dealer-led |
| Bulthaup | premium kitchen architecture, b3/b2/b1 language, custom planning | dealer-led planning; official product/catalog/PDF materials teach dimensions, custom sizes, front materials |
| Boffi | kitchens, bathrooms, wardrobes, modular systems, design integration | official downloads/catalogues plus product pages; CAD/BIM may route through professional/library platforms |
| Valcucine | flexible kitchen collections and special elements | professional 3D models/design inspiration page; study modularity and special elements |
| Arclinea | kitchen systems, professional cooking/living logic | official collection/product pages; record dealer/professional access when found |
| Rimadesio | sliding doors, wall panels, walk-in closets, modular living | downloads/catalogues, product systems, materials, track/panel logic |
| Porro | Storage wardrobes, walk-in closets, boiserie, systems | product system pages; strong for wardrobe/boiserie module logic |
| Lema | custom wardrobes, walk-in closets, Selecta/LT40 systems | official product/catalogue pages; study bespoke storage and finishes |
| Modulnova | integrated kitchen/living/bath/systems/outdoor design identity | downloads/reserved area; study architectural material continuity |
| Cesar | kitchen systems, materials, planning guides | official/download/dealer sources; study material system and planning guides |
| Poggenpohl | German kitchen architecture, custom solutions | dealer/pro software ecosystem; record 2020/pCon/catalog routes when official/authorized |

## What to extract from each product/system

```text
brand:
system/product family:
product URL:
room/use:
module types:
standard dimensions / available size range:
custom-size rules:
carcass / frame / panel logic:
door system: hinged / sliding / coplanar / pocket / flap:
handle logic: handle / handleless / groove / push-latch:
hardware: hinges / runners / rails / soft-close / lift systems:
materials: carcass / front / worktop / glass / metal / stone / lacquer / veneer:
finish codes:
lighting / power / appliance integration:
ventilation / plumbing / structural notes:
CAD/SU/Revit/BIM/3D available formats:
login / dealer / A&D requirement:
source files saved:
rights status:
SketchUp LOD strategy:
CAD drawing sheets needed:
FF&E/procurement notes:
installation risks:
SA&BOO aesthetic verdict:
```

## Module intelligence

### Kitchen modules

Inspect:

- base, wall, tall, corner, open shelf, island and appliance modules;
- worktop thickness, overhang, waterfall sides, backsplash, end panels;
- sink/cooktop/dishwasher/fridge/oven/wine-storage integration;
- plinth/toe-kick or shadow-gap expression;
- filler/scribe panels at walls and columns;
- lighting under wall units, inside cabinets, toe-kick, shelves;
- ventilation and heat/moisture clearances;
- handleless grooves vs push-latch vs exposed handle;
- drawer organization and internal accessories.

### Wardrobe / walk-in closet modules

Inspect:

- carcass vs open pole system vs wall-panel system;
- hinged, sliding, coplanar, glass, pocket, open closet door logic;
- hanging, folded, drawers, shoe, luggage, accessories, vanity zones;
- internal lighting, sensors, power, mirror, ventilation;
- panel/rail/jamb tracks and ceiling/floor tolerances;
- glass transparency, reflection, fingerprint/maintenance risk;
- island chest and bench relations in walk-in closets.

### Wall systems / bookcases / partitions

Inspect:

- vertical module rhythm and bay width;
- load, shelf thickness, deflection, backing/panel anchoring;
- TV/media/cable management;
- sliding track, concealed guides, floor/ceiling fixings;
- open/closed storage ratio;
- alignment with ceiling, doors, wall panels, lighting and art.

## CAD drawing requirements

System furniture needs more than a plan symbol. Produce or request:

1. plan footprint with clearances and appliance/door swing zones;
2. elevations for each wall/system run;
3. sections through worktop, plinth, wall unit, tall unit, wardrobe, rail/track;
4. module schedule with widths/heights/depths and finish codes;
5. hardware/accessory schedule;
6. power/plumbing/lighting coordination plan;
7. installation tolerance and site-measure notes.

Use SA&BOO CAD layers:

- `I-FURN-FIXD-N` for built-in/system furniture;
- `I-FURN-LOOS-N` for movable modular systems when not fixed;
- `I-ANNO-TAGS` for module/material tags;
- `I-HATCH-MATL` for panel/material zones;
- `E-LITE-FIXT-N`, `E-POWR-OUTL-N`, `P-PLMB-FIXT-N`, `M-HVAC-DIFF-N` for service coordination.

## SketchUp / CAD / 3DS model hygiene

- Keep official model source path and terms next to the file.
- Verify units immediately after import.
- Separate proxy LOD and hero-detail LOD.
- Convert heavy 3DS/MAX/FBX imports into clean grouped components with tags.
- Create proxy modules for repeated cabinets; do not copy heavy meshes 100 times.
- Preserve material slots for front, carcass, worktop, metal, glass, internal finish, handles.
- Align textures: veneer grain, stone veining, brushed metal, glass opacity, lacquer roughness.
- Name components by system and module: `POLIFORM_WARDROBE_TALL_600x600x2600_LOD1`.

## Quality cannot be sacrificed for speed

For system furniture, never use a lightweight workflow to skip module verification, site tolerances, hardware, materials, service coordination, CAD elevations/sections, or SketchUp model hygiene. A fast cabinetry answer without these checks is not SA&BOO quality.

## Design quality gate

A system furniture solution is weak if:

- it ignores wall/ceiling/floor tolerances;
- every door/module is visually equal and lacks rhythm;
- appliance, plumbing, lighting, ventilation, or power coordination is missing;
- material transitions do not align with module seams;
- imported models are pretty but cannot be dimensioned or installed;
- storage logic does not match the client’s ritual;
- it copies a brand image without understanding module, proportion, or detail.

A strong SA&BOO system furniture solution should feel architectural, precise, tactile, and calm: it integrates storage and living behavior while making materials and shadow gaps look intentional.
