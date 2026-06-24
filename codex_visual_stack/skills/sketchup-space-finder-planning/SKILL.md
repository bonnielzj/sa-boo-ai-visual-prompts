---
name: sketchup-space-finder-planning
description: SketchUp Space Finder workflow for SketchUp 2025 space, room, floor-area, and planning analysis. Use when Codex needs to plan, prepare, audit, or guide identifying spaces in SketchUp models, generating room/area overlays, checking apartment/residential/commercial zones, comparing floor plan options, validating enclosed rooms from walls/openings, preparing area schedules, using visible geometry scenes for space detection, IFC/TrimBIM-oriented space workflows, or connecting SketchUp space data to interior-layout-optimizer, CAD drawings, proposal decks, and material/budget schedules.
---

# SketchUp Space Finder Planning

Use this skill to turn a SketchUp model into recognizable room/space information for interior planning, area checking, and proposal communication. Space Finder is useful after walls/floors have been modeled enough to form readable enclosed or semi-enclosed spaces.

Codex usually cannot operate the Space Finder UI directly; prepare model visibility, scene states, wall/floor geometry, naming strategy, and manual operation steps. Use SketchUp MCP for model cleanup, tag/scene setup, and read-only verification when useful.

## Installed environment

- SketchUp target: SketchUp 2025 on macOS.
- Space Finder source package: `/Users/bonnie/Downloads/SketchUpSpaceFinder.rbz`.
- Installed plugin paths:
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/habitat_space_use_plugin.rb`
  - `/Users/bonnie/Library/Application Support/SketchUp 2025/SketchUp/Plugins/habitat_space_use_plugin/`
- Installed version from loader: `0.31.2`.
- Creator: SketchUp.
- Description from loader: `Support the identification of spaces in SketchUp models.`
- Package contents: Ruby loader, encrypted `.rbe`, style, icons/images; no `.exe`, `.dll`, `.bundle`, `.dylib`, or `.so` found.

Read `references/space-finder-workflow.md` when preparing model scenes, running room/space analysis, or converting results into area schedules/proposals.

## Core workflow

1. **Define the analysis goal**
   - Quick room/space recognition.
   - Residential layout area check.
   - Option A/B floor plan comparison.
   - Commercial/office zoning and space schedule.
   - Proposal overlay showing public/private/service/storage zones.
   - IFC/TrimBIM-style space export or documentation support.

2. **Prepare visible geometry**
   - Space Finder responds to the model/visible geometry; create a clean analysis scene.
   - Show walls, floors/slabs, major openings, and boundaries.
   - Hide furniture clutter, decor, high-poly assets, landscape scatter, and irrelevant entourage.
   - Ensure walls/partitions connect cleanly enough to imply spaces.
   - Use section cuts or floor-isolation scenes for multi-story models.

3. **Run Space Finder manually**
   - Open the Space Finder/SketchUp Spaces tool.
   - Run space detection on the clean scene/floor.
   - Review detected spaces and correct model gaps if rooms are missing/merged.
   - Save or export/report detected area information where available.

4. **Translate into design decisions**
   - Name spaces by function: entry, living, dining, kitchen, master, bath, laundry, storage.
   - Group into zones: public, private, service, circulation, storage, outdoor/terrace.
   - Compare net/gross area, circulation efficiency, adjacency, and furniture feasibility.
   - Hand off to `interior-layout-optimizer` for layout critique and improvement.

5. **QA**
   - Rooms should not merge through unclosed wall gaps unless intentionally open-plan.
   - Door openings should not destroy intended space boundaries if a room should still count.
   - Multi-floor spaces should be analyzed floor by floor.
   - Area units must match the project standard.

## Output pattern

```text
Space Finder 目标：
分析场景/楼层：
需要显示的几何：
需要隐藏的几何：
空间命名规则：
运行步骤：
面积/分区检查：
问题与修模建议：
交付输出：
下一步 handoff：
```

## SA&BOO planning rules

- Space detection is a planning aid, not a substitute for dimensioned CAD/施工图 verification.
- Use visual overlays first: room colors, labels, zone diagrams, and area tables support client communication.
- For residential interiors, always check circulation and storage quality, not only area numbers.
- For proposal use, export clean before/after or option A/B space plans with identical camera/scene settings.
