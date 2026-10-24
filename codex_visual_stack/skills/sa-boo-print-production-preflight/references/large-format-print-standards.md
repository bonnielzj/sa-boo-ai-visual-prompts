# Large-Format Print Standards

## Size Language

Always name which size you mean:

- **Hero artwork size**: the designed visual area, often the client-approved composition.
- **Installed visible face**: the physical area visible after installation.
- **CAD unfolded perimeter**: total measured construction boundary, which may include returns, corners, door conditions, or non-graphic runs.
- **Panel trim size**: each printed piece before bleed.
- **Bleed size**: trim plus extra image beyond all edges.
- **Proof size**: reduced review image or PDF, not final print scale.

Never assume CAD unfolded length equals the hero artwork size.

## Ratio Rules

Calculate:

```text
source_ratio = source_width_px / source_height_px
target_ratio = target_width_mm / target_height_mm
output_ratio = output_width_px / output_height_px
```

Preflight judgment:

- `<= 0.5%` mismatch: pass.
- `0.5%-1%` mismatch: warning; explain crop/bleed/source reason.
- `> 1%` mismatch: fail unless explicitly approved.

These are inspection judgments. `scripts/preflight_image.py` defaults to failing
above its `--ratio-tolerance 0.005`; it does not implement this warning band.
For a specifically accepted warning-range ratio, document the crop/bleed reason
and choose the corresponding tolerance explicitly. Never silently stretch or use
`--warn-only` to approve production. Interpret the measured ratio with the actual
source lock and print contract rather than treating the script label as the decision.

Allowed mismatch strategies:

- **Crop**: remove edge content while preserving scale.
- **Extend**: add visual continuation without moving locked key details.
- **Tile**: repeat a designed module intentionally.
- **Panelize**: split without changing global art.
- **Rebuild**: recreate as vector/native art when AI source is not print-safe.

Forbidden:

- silent stretch;
- mirrored text/logos;
- regenerated image that changes approved layout;
- door/cut/trim marks baked into clean print master;
- using perspective mockups as final print art.

## Resolution Rules

Useful formulas:

```text
pixels = physical_mm * dpi / 25.4
full_size_dpi = pixels / physical_mm * 25.4
1:10_dpi_needed = full_size_dpi * 10
```

Common presets:

- Full-size `72dpi`: large hoarding, street distance, good default.
- Full-size `100dpi`: closer viewing distance or very detailed graphics.
- Full-size `150dpi`: premium close-view wall covering, heavy file size.
- `1:10 / 300dpi`: equals full-size `30dpi`, often proof-level for huge hoardings.
- `1:10 / 720dpi`: equals full-size `72dpi`.
- `1:10 / 1000dpi`: equals full-size `100dpi`.

Judge actual detail from pixel count at the target physical size and the expected
viewing distance. The helper reports `effective_full_size_dpi_for_target` but has
no effective-DPI quality gate; compare that value separately with the chosen
requirement. `--expected-dpi` verifies embedded metadata only. Changing metadata
or interpolating more pixels does not prove restored detail or print suitability.

## Panelization

For each panel record:

```text
panel_id
trim_start_mm
trim_width_mm
trim_height_mm
bleed_mm
pixel_size_with_bleed
print_file
guide_preview_file
```

Panel contact sheets should show split order and approximate continuity, but should be labeled proof-only.

## Vendor Handoff Checklist

Match the actual handoff contract. An inspection returns findings; a single-file
handoff supplies the requested file with necessary size/scale information. For a
panelled vendor package, include the applicable items:

- clean and/or bleed print master as required;
- divided panels when panelization is requested;
- proof-only guide overview and panel contact sheet when useful for continuity or requested;
- production specs with size, DPI, applicable bleed and panel count; separate spec JSON/README only when needed;
- source/crop metadata.

Confirm the vendor decisions relevant to the actual production scope:

- CMYK ICC profile and black density;
- print material and lamination;
- bleed/overlap preference;
- whether panels need crop marks;
- installation order and corner/return logic;
- final QR/text/vector overlay needs;
- physical sample proof before full print.
