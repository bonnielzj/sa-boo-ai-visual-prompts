# DBS Move Rotate Open Close workflow reference

## Best interior-design uses

- Wardrobe and cabinet door open/close demonstrations.
- Kitchen drawers, pull-out shelves, appliance doors, pantry pull-outs.
- Sliding doors, pocket doors, wardrobe sliding panels.
- Hinged room doors and clearance checks in tight plans.
- Furniture mechanism studies for client review.
- Before/after states for render scenes and presentation screenshots.

## Decision matrix

| Need | Prefer |
|---|---|
| Quick interactive open/close of a group/component | DBS Move Rotate Open Close |
| Parametric size/formula-driven component | SketchUp Dynamic Components |
| Static closed/open visual only | Duplicate groups + SketchUp scenes |
| Full animation timeline/video | Dedicated animation plugin/workflow |
| Check door swing in 2D CAD drawings | CAD arcs/clearance drawings |
| Precise collision/clearance study | DBS test + dimensions/sections |

## Setup rules

- Each moving element must be separate from fixed geometry.
- Put the group/component origin/axes near the hinge/slide reference when possible.
- Name the part before configuring the motion.
- Keep a closed backup state. For important projects, duplicate the full cabinet/room first.
- If there are nested components, test whether DBS moves the intended level; if not, regroup/restructure.

## Recipes

### Hinged cabinet or room door

1. Group the door leaf only, excluding frame and handle if the handle must remain attached then include it inside the leaf group.
2. Place or mentally define hinge edge as rotation axis.
3. Configure closed state at actual installed position.
4. Rotate to open position, usually 90° to 110° depending on clearance.
5. Test collision with adjacent wall/cabinet/handle.
6. Save scenes: `Door Closed`, `Door Open`.

### Drawer / pull-out shelf

1. Group drawer box/front/handle as one moving unit.
2. Define movement vector along the drawer slide.
3. Configure closed state flush with cabinet front.
4. Configure open state at real pull-out distance.
5. Check knee/circulation clearance and adjacent doors.

### Sliding door / wardrobe panel

1. Group each sliding panel separately.
2. Define track direction.
3. Configure closed and open positions with real overlap.
4. Check if handles and panel thickness collide.
5. Use scenes or camera to communicate the slide path.

## QA checklist

- **Geometry:** movable part separated; no fixed carcass accidentally inside moving group.
- **Pivot:** hinge/axis correct; rotation looks physically plausible.
- **Movement:** open/close state returns accurately; no offset drift.
- **Clearance:** no collision with walls, counters, adjacent doors, handles, appliances, user circulation.
- **Presentation:** saved scenes and camera angles show motion clearly.
- **Fallback:** if plugin behavior is unstable, create duplicate closed/open states manually and save scenes.

## Good trigger requests

- “用 DBS 做柜门开合演示。”
- “这个抽屉拉出距离和通道会不会冲突？”
- “帮我规划一个移门开合状态设置。”
- “这个衣柜门怎么设置 90 度打开和关闭？”
- “判断这类开合用 DBS 还是动态组件。”
