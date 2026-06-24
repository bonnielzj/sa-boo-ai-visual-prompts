---
name: sketchup-dbs-move-rotate-open-close
description: SketchUp DBS Move Rotate Open Close 3.10 workflow for SketchUp 2025 movable furniture and interior component interaction. Use when Codex needs to plan, prepare, audit, or guide configuring open/close states, move/rotate joints, cabinet doors, wardrobe doors, drawers, sliding doors, hinged room doors, appliance doors, furniture mechanisms, client demo scenes, clearance checks, or when deciding between DBS Move Rotate Open Close, SketchUp Dynamic Components, native scenes, Fredo/Animator-style animation, or manual duplicated states.
---

# SketchUp DBS Move Rotate Open Close

Use this skill to guide interactive move/rotate/open/close workflows in SketchUp with DBS Move Rotate Open Close. The plugin helps configure movable joints and quickly toggle between closed and open states, useful for interior furniture and door clearances.

Codex usually cannot click DBS tools directly; prepare object grouping, pivot/joint placement, open/close positions, clearance checks, scene strategy, and QA. Use SketchUp MCP for file checks, grouping/naming, simple scene setup, or model inspection where useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Source package: `/Users/bonnie/Downloads/dbs_move_rotate_open_close_v3_10.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/dbs_move_rotate_open_close.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/dbs_move_rotate_open_close/`
- Extension name after restart: `DBS Move Rotate Open Close`.
- Version: `3.10`.
- Creator: `DBS` / Daniel Bieńkowski Solutions.
- Extension Warehouse ID: `d0792e84-8217-4158-a093-5c6b6f325084`.
- Version ID: `45b05112-26cb-4c72-87df-7dfe2c269521`.
- Package contents: Ruby loader, encrypted `.rbe` implementation files, HTML dialogs, icons; no `.exe`, `.dll`, `.bundle`, `.dylib`, `.so`, shell script, app, or installer binary found.
- Package history notes in loader say it became free in v3.4 and includes Mac fixes; still treat `.rbe` code as not fully auditable.
- MCP install check confirmed SketchUp `25.0.659`, Ruby `3.2.2`, plugin files present. If the extension is not listed, fully quit and reopen SketchUp after file install.

Read `references/dbs-open-close-workflow.md` for detailed setup recipes, pivot rules, and QA.

## Core workflow

1. **Decide if DBS is the right tool**
   - Use DBS for interactive open/close demos: hinged cabinet doors, room doors, wardrobe doors, drawers, sliding panels, pull-out shelves, appliance doors.
   - Use SketchUp Dynamic Components when the component needs parametric dimensions, formulas, or distributable dynamic behavior.
   - Use native scene duplicates when a simple before/after comparison is enough.
   - Use advanced animation tools only when timeline/keyframe output is required.

2. **Prepare geometry**
   - Make each movable part its own group/component: `DOOR_Wardrobe_Left`, `DRAWER_Kitchen_01`, etc.
   - Separate fixed frame/carcass from moving leaf/drawer/panel.
   - Set axes/origin/pivot close to the actual hinge, slide, or rotation center when possible.
   - Keep a closed-state backup scene or duplicate before configuration.
   - Clean nested components and avoid loose raw geometry inside the moving part when possible.

3. **Configure open and close states manually**
   - Select the moving object and use DBS configuration to define closed and open positions.
   - For hinged doors: rotate around hinge edge; typical tests are 90°, 105°, or project-specific opening angles.
   - For drawers/sliding doors: move along a straight vector; test actual pull-out or slide clearance.
   - Set animation time if the dialog provides it; keep client demos slow enough to read.

4. **Check clearances and presentation**
   - Test collision with walls, handles, adjacent cabinet doors, furniture, appliances, and circulation paths.
   - Save scenes: closed, open, partially open if needed.
   - Use camera tools to show the opening path clearly.
   - Use dimensions/annotations outside DBS if presenting construction decisions.

5. **QA before relying on the setup**
   - Moving part has correct pivot/axis and returns to closed state cleanly.
   - Open state does not clip through surrounding geometry unless intentionally ignored.
   - Components are named and grouped; no accidental movement of fixed carcass or room geometry.
   - Client-facing scenes are saved and labeled.

## Output pattern

```text
开合目标：
对象类型：房门 / 柜门 / 抽屉 / 移门 / 家具机构 / 电器门 / 其他
建议工具：DBS Move Rotate Open Close / Dynamic Components / Scene duplicates / 其他
准备工作：分组、轴心、闭合备份、固定/移动部件分离
运动方式：旋转 / 平移 / 旋转+平移，角度/距离，动画时间
操作步骤：
检查：碰撞 / 净空 / 回位 / 场景 / 命名
```
