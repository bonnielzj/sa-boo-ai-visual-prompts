# R16 Outlier / Overlap QA
- Model: `/Users/bonnie/Documents/设计项目/logicat_popup_su/03_SketchUp_Model/LOGICAT_popup_ASTRONAUT_CAT_UFO_R15_white_bg_ceiling_enscape.skp`
- Full model bbox: **8002400.0 × 8235.0 × 10850000.0 mm**
- Root entities: 461
- Outlier root entities >50m or size >50m: **1**
- Suspected top-level overlap pairs: **990**; design-relevant after helper filter: **517**
- Near-duplicate top-level bbox pairs: **0**

## Outlier root entities
1. Group `LOCKED_IMPORTED_CAD_REF_PLAN_DXF` | layer `CAD_REF_PLAN` | bbox size 8000000.0 × 0.0 × 10850000.0 mm | min 0.0, -1850000.0, 0.0 | max 8000000.0, 9000000.0, 0.0

## Largest root entities
1. Group `LOCKED_IMPORTED_CAD_REF_PLAN_DXF` | layer `CAD_REF_PLAN` | size 8000000.0 × 0.0 × 10850000.0 mm | max_abs 9000000.0mm
2. Group `R14_WHITE_STUDIO_right_white_floor_apron` | layer `00_R14_white_studio_background` | size 1850.0 × 8.0 × 15550.0 mm | max_abs 11350.0mm
3. Group `R14_WHITE_STUDIO_left_white_floor_apron` | layer `00_R14_white_studio_background` | size 1850.0 × 8.0 × 15550.0 mm | max_abs 11350.0mm
4. Group `R15_WHITE_STUDIO_extra_high_left_sky_blocker` | layer `00_R15_white_studio_ceiling_background` | size 120.0 × 5200.0 × 13100.0 mm | max_abs 11500.0mm
5. Group `R15_WHITE_STUDIO_extra_high_right_sky_blocker` | layer `00_R15_white_studio_ceiling_background` | size 120.0 × 5200.0 × 13100.0 mm | max_abs 11500.0mm
6. Group `R15_WHITE_STUDIO_extra_high_rear_sky_blocker` | layer `00_R15_white_studio_ceiling_background` | size 12800.0 × 4900.0 × 120.0 mm | max_abs 10710.0mm
7. Group `R15_WHITE_STUDIO_overhead_white_diffuser_ceiling_hides_sky` | layer `00_R15_white_studio_ceiling_background` | size 12100.0 × 100.0 × 12700.0 mm | max_abs 11500.0mm
8. Group `R14_WHITE_STUDIO_right_side_bounce_wall_starts_after_camera` | layer `00_R14_white_studio_background` | size 85.0 × 3900.0 × 12350.0 mm | max_abs 11350.0mm
9. Group `R14_WHITE_STUDIO_left_side_bounce_wall_starts_after_camera` | layer `00_R14_white_studio_background` | size 85.0 × 3900.0 × 12350.0 mm | max_abs 11350.0mm
10. Group `R15_WHITE_STUDIO_rear_upper_fill_above_backwall` | layer `00_R15_white_studio_ceiling_background` | size 12100.0 × 100.0 × 3300.0 mm | max_abs 11500.0mm
11. Group `R14_WHITE_STUDIO_rear_cyclorama_sweep_visible_not_blocking` | layer `00_R14_white_studio_background` | size 11800.0 × 760.0 × 760.0 mm | max_abs 10450.0mm
12. Group `R14_WHITE_STUDIO_rear_high_white_background_wall` | layer `00_R14_white_studio_background` | size 11800.0 × 4600.0 × 85.0 mm | max_abs 10492.5mm
13. Group `R14_WHITE_STUDIO_rear_white_floor_apron` | layer `00_R14_white_studio_background` | size 11700.0 × 8.0 × 2350.0 mm | max_abs 11350.0mm
14. Group `R14_WHITE_STUDIO_front_open_white_floor_apron_no_wall` | layer `00_R14_white_studio_background` | size 11700.0 × 8.0 × 4200.0 mm | max_abs 9850.0mm
15. Group `CAD_SCALE_GRID_1000MM` | layer `CAD_REF_PLAN` | size 8000.0 × 0.0 × 9000.0 mm | max_abs 9000.0mm
16. Group `8m x 9m field from CAD - R08` | layer `01_floor_and_decal` | size 8000.0 × 35.0 × 9000.0 mm | max_abs 9000.0mm
17. Group `VISIBLE_CAD_TRACE_FROM_PREVIOUS_DXF` | layer `CAD_REF_PLAN` | size 8000.0 × 0.0 × 9000.0 mm | max_abs 9000.0mm
18. Group `soft blue backwall with storage base` | layer `04_backwall_storage_fitting` | size 7200.0 × 2650.0 × 90.0 mm | max_abs 8795.0mm
19. Group `continuous bottom storage under backwall` | layer `04_backwall_storage_fitting` | size 6900.0 × 720.0 × 600.0 mm | max_abs 8700.0mm
20. Group `R12 left side slim lighting rail / cable route` | layer `10_visible_commercial_lighting_fixtures` | size 36.0 × 176.0 × 6740.7 mm | max_abs 7860.4mm

## Design-relevant overlap samples
1. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `flush recessed outer floor orbit track - dark channel` [01_floor_and_decal], overlap ratio 1355.0
2. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `flush embedded ice-blue LED orbit guide outer line` [01_floor_and_decal], overlap ratio 1666.667
3. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `flush embedded ice-blue LED orbit guide inner line` [01_floor_and_decal], overlap ratio 1490.0
4. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `flush 2m island footprint / recessed bearing service zone` [01_floor_and_decal], overlap ratio 530.0
5. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `2m round-oval main plinth for cat UFO installation` [02_cat_ufo_visual_installation], overlap ratio 10.103
6. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `transparent acrylic product display halo around cat plinth` [02_cat_ufo_visual_installation], overlap ratio 17.294
7. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `slow rotary cat display turntable disk - optional motorized` [02_cat_ufo_visual_installation], overlap ratio 20.476
8. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `recessed rotary bearing track around cat turntable` [02_cat_ufo_visual_installation], overlap ratio 56.111
9. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `warm LED ring inside rotary track at cat turntable base` [02_cat_ufo_visual_installation], overlap ratio 59.375
10. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `bottom clear PVC beam hoop` [02_cat_ufo_visual_installation], overlap ratio 192.5
11. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 hidden waist crossbar to rear spine` [02_cat_ufo_visual_installation], overlap ratio 1.026
12. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 LOGICAT smart cat head FRP shell` [02_cat_ufo_visual_installation], overlap ratio 0.809
13. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 astronaut utility belt ring` [02_cat_ufo_visual_installation], overlap ratio 15.833
14. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 glowing oxygen tube left` [02_cat_ufo_visual_installation], overlap ratio 3.926
15. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 glowing oxygen tube right` [02_cat_ufo_visual_installation], overlap ratio 3.926
16. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 left shoulder joint sphere` [02_cat_ufo_visual_installation], overlap ratio 0.774
17. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 left smart glove` [02_cat_ufo_visual_installation], overlap ratio 0.871
18. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 left magnetic moon boot` [02_cat_ufo_visual_installation], overlap ratio 1.164
19. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 right shoulder joint sphere` [02_cat_ufo_visual_installation], overlap ratio 0.774
20. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 right smart glove` [02_cat_ufo_visual_installation], overlap ratio 0.871
21. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 right magnetic moon boot` [02_cat_ufo_visual_installation], overlap ratio 1.164
22. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 glowing data cable tail tip` [02_cat_ufo_visual_installation], overlap ratio 0.815
23. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 mini satellite product drone body 1` [02_cat_ufo_visual_installation], overlap ratio 1.115
24. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 transparent satellite safety tether 1` [02_cat_ufo_visual_installation], overlap ratio 0.999
25. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 mini satellite product drone body 2` [02_cat_ufo_visual_installation], overlap ratio 1.115
26. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R05 transparent satellite safety tether 2` [02_cat_ufo_visual_installation], overlap ratio 0.999
27. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `small product asteroid display pod 1` [02_cat_ufo_visual_installation], overlap ratio 1.289
28. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `small product asteroid display pod 2` [02_cat_ufo_visual_installation], overlap ratio 1.289
29. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `small product asteroid display pod 3` [02_cat_ufo_visual_installation], overlap ratio 1.289
30. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `small product asteroid display pod 4` [02_cat_ufo_visual_installation], overlap ratio 1.289

## Helper/background overlap samples
1. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `warm transparent UFO projection light beam / high-clear PVC` [02_cat_ufo_visual_installation], overlap ratio 8.251
2. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `top UFO saucer shell - segmented FRP/PVC panels` [07_lighting_orbit], overlap ratio 19.264
3. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `top UFO silver dome FRP shell` [07_lighting_orbit], overlap ratio 4.438
4. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `underside UFO warm spotlight ring` [07_lighting_orbit], overlap ratio 26.667
5. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `UFO shell radial hanger / carbon rod 2` [07_lighting_orbit], overlap ratio 2.251
6. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `UFO shell radial hanger / carbon rod 3` [07_lighting_orbit], overlap ratio 2.251
7. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `UFO shell radial hanger / carbon rod 5` [07_lighting_orbit], overlap ratio 2.251
8. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `UFO shell radial hanger / carbon rod 6` [07_lighting_orbit], overlap ratio 2.251
9. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible front commercial lighting track - 40mm black aluminum` [10_visible_commercial_lighting_fixtures], overlap ratio 1.149
10. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible backwall wallwash lighting track - black aluminum` [10_visible_commercial_lighting_fixtures], overlap ratio 1.149
11. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible track spot 3800K wide 1 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.276
12. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible track spot 3800K wide 2 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.276
13. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible track spot 3800K wide 3 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.276
14. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible track spot 3800K wide 4 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.276
15. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible warm cat-UFO accent spot 3000K narrow 1 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.113
16. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible warm cat-UFO accent spot 3000K narrow 2 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.113
17. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible warm cat-UFO accent spot 3000K narrow 3 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.093
18. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 visible warm cat-UFO accent spot 3000K narrow 4 adjustable cylinder body` [10_visible_commercial_lighting_fixtures], overlap ratio 1.093
19. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 shelf linear lens / task strip 3200K 1` [10_visible_commercial_lighting_fixtures], overlap ratio 0.875
20. `8m x 9m field from CAD - R08` [01_floor_and_decal] ↔ `R12 shelf linear lens / task strip 3200K 2` [10_visible_commercial_lighting_fixtures], overlap ratio 0.875