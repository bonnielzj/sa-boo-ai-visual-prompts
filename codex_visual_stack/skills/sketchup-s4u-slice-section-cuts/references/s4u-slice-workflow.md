# s4u Slice workflow reference

## Best interior-design uses

- Exploded axonometric views showing wall/floor/ceiling/furniture construction layers.
- Physical section cuts through cabinets, walls, counters, stairs, built-ins, and white-model masses.
- Detaching part of a model for editing, option studies, or material separation.
- Creating grouped section geometry for proposal diagrams.
- Cutting openings or display slices where native visual section planes are not enough.
- Model diagnosis: reveal hidden intersections or nested construction issues.

## Decision matrix

| Need | Prefer |
|---|---|
| Non-destructive visual section only | Native Section Plane |
| Actual split/cut/detach geometry | s4u Slice |
| Boolean subtract/union on clean solids | Solid Tools / BoolTools |
| Repair or clean imported edges before cutting | Edge Tools² |
| Check manifold pieces after slicing | Solid Inspector |
| Add section caps, trims, frames | Profile Builder / native modeling |
| Create presentation camera/orthographic view | Curic Align View / Advanced Camera Tools |
| Standardize cut-face material | TT Material Replacer |

## Cut strategy recipes

### Interior construction cutaway

1. Duplicate the target room or wall assembly.
2. Group the duplicate as `SRC_Cutaway_Room_01` and keep an untouched hidden backup.
3. Decide the camera first: what should be revealed?
4. Use s4u Slice to cut away a corner or plane section.
5. Name pieces: `CUT_Wall_Left`, `CUT_Ceiling_Reveal`, `CUT_Floor_Layer`.
6. Assign simple proposal materials: clay exterior, red/gray cut faces, highlighted construction layers.
7. Create a saved scene with section/cut view.

### Cabinet / built-in detail section

1. Group the cabinet/built-in and duplicate it.
2. Define a vertical or horizontal cut plane through the detail of interest.
3. Slice or detach the front/side piece.
4. Inspect board thickness, shelves, hidden collisions, and cut faces.
5. Add annotations/dimensions separately in Layout/CAD if needed.

### Exploded layer study

1. Slice the object into logical layers or components.
2. Move detached pieces apart along one axis.
3. Use consistent naming and material colors.
4. Save a scene for proposal or social media diagram.
5. Keep a compact unsliced original in the file.

## Geometry preparation notes

- Slicing old imported assets can produce many small fragments; clean first.
- Nested components may slice differently depending on plugin mode; test on a copy.
- Avoid slicing entire heavy models at once; isolate target groups.
- If cutting must be dimensionally precise, place guide faces/planes first rather than eyeballing.
- Cut faces may need manual repair or face reversal after the operation.

## QA checklist

- **Backup:** untouched source exists and is hidden/tagged.
- **Selection:** only intended groups/components were affected.
- **Geometry:** no accidental missing faces, duplicate faces, micro-fragments, or reversed faces.
- **Organization:** generated pieces are grouped, named, and optionally tagged.
- **Presentation:** cut materials and camera scenes clearly explain the design.
- **Performance:** delete failed cut fragments; purge unused geometry/materials if needed.

## Good trigger requests

- “用 s4u Slice 做一个墙体构造剖切图。”
- “把这个柜体切开，做内部结构展示。”
- “这个模型需要实际切掉一角，不只是剖切显示。”
- “做一个爆炸轴测，把构造层切出来并分开。”
- “判断这个剖切该用 Section Plane、s4u Slice 还是 Solid Tools。”
