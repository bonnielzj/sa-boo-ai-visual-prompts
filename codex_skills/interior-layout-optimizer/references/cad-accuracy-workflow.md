# CAD Accuracy Workflow for Interior Layout Optimization

Use this reference when a residential layout optimization depends on DWG, DXF, PDF, screenshot, CAD/MCP tools, measurable dimensions, or downstream SketchUp modeling.

## Prime rule

```text
measure first → diagnose → retrieve precedents → propose options → verify clearances → prepare CAD/SU next artifact
```

Do not produce precise layout changes from a blurry image. If the baseline is not measurable, label the work as conceptual.

## Evidence levels

| Level | Input | What is allowed |
|---|---|---|
| L0 | no plan | ask for plan/CAD/PDF/screenshot and client requirements |
| L1 | blurry image | high-level diagnosis only; no exact clearances or wall moves |
| L2 | clear image + one known dimension | approximate planning; mark uncertainty |
| L3 | scaled PDF or measured plan | reliable layout options with dimension checks |
| L4 | DWG/DXF/CAD | CAD/MCP-backed optimization, redline, dimensioning, SU handoff |

## CAD/MCP route

### DWG/DXF

- Use `cadq` when semantic/spatial facts are needed: layers, features, areas, labels, nearest/adjacent relations, or evidence handles.
- Use AutoCAD MCP through `autocad-drafting` when opening, editing, annotating, redrawing, dimensioning, saving, or exporting a CAD drawing.
- Preserve the original file. Save optimized/redline outputs as a new revision.

### PDF

- Use the PDF as a visual/measured baseline only if scale or known dimensions are available.
- Convert/trace to CAD if the work will proceed to SketchUp or construction-level coordination.

### Image/screenshot

- Use for discussion, not precision.
- Ask for one known dimension and fixed-constraint notes.
- Do not claim exact cabinet depths, aisle widths, or fixture clearances unless verified.

## Baseline checklist

Extract or request:

```text
Project type / area / household
Units / scale / one known dimension
External boundary / usable area
Structural walls / columns / beams
Shafts / plumbing / wet areas
Door and window openings / swing directions
Kitchen/bath/core locations
Existing furniture or client must-keeps
Daylight/ventilation conditions
Storage requirements
```

## Practical clearance checklist

Use local code/project standards when provided. Otherwise flag these as dimensions to verify rather than invent:

```text
Main circulation width
Entry storage depth
Wardrobe depth
Kitchen counter depth and aisle
Dining chair pull-out clearance
Sofa / coffee table / TV distance
Bedside clearance
Toilet / shower / vanity clearance
Door swing conflicts
Washer/dryer/service access
```

## Output evidence block

```text
准确性状态：L0/L1/L2/L3/L4
已确认：
未确认：
CAD/MCP evidence：tool used / file / layer / handle / dimension / screenshot path
不能推断：
下一视觉检查点：CAD top-view proof / dimensioned plan / redline overlay / SU white-model reference
```

## When to stop

Stop before proposing construction-like changes when:

- no scale or known dimension exists;
- structural/wet-area constraints are unknown;
- the plan image is unreadable;
- CAD and screenshot conflict;
- a proposed move depends on plumbing/structure not yet verified.

Give Bonnie a precise data request or produce only conceptual options.
