# SA&BOO Version and Revision Standard

## Folder structure

```text
00_RECEIVED/        client/architect/consultant inputs, never edit directly
01_WIP/             internal working DWG files
02_XREF/            relative-path xrefs and underlays
03_ISSUE/           issued packages by date/revision
04_PDF/             plotted PDFs
05_EXPORT/          DWG/DXF/transmittal/export packages
06_ARCHIVE/         superseded files
07_CHANGELOG/       issue records, redlines, RFI/design change logs
```

## File naming

Use a name that sorts and explains itself:

```text
YYYYMMDD_ProjectCode_Discipline_SheetNo_Title_Stage_R00.dwg
```

Examples:

```text
20260622_SABOO-VILLA01_I_A101_Plan-CD_R00.dwg
20260622_SABOO-VILLA01_I_A301_Elevations-CD_R01.dwg
20260622_SABOO-VILLA01_I_A801_Details-IFC_R02.pdf
```

## Stage codes

| Code | Meaning |
|---|---|
| SD | Schematic / 方案 |
| DD | Design development / 深化 |
| CD | Construction drawing / 施工图 |
| IFC | Issued for construction / 施工签发 |
| SK | Sketch / 洽商草图 |
| AB | As-built / 竣工图 |

## Version vs revision

- `v0.1`, `v0.2` = internal WIP versions, not issued to site.
- `R00` = first formal issue.
- `R01`, `R02` = formal issued revisions.
- Never use filenames like `final.dwg`, `final2.dwg`, `latest.dwg`.

## Issue package rule

Each formal issue should include:

- DWG if contract requires.
- Flattened PDF set.
- Sheet index.
- Change log / transmittal.
- Xref/package folder if sending editable CAD.

Never overwrite an issued package. Create a new dated revision folder.

## Revision graphics

Use these layers:

```text
I-REV-CLOUD-R01
I-REV-DELT-R01
I-REV-CLOUD-R02
I-REV-DELT-R02
```

Graphic rules:

- Cloud the changed area only, not the whole drawing.
- Add delta triangle/revision mark near the change.
- Add revision note in title block table.
- Current issue usually shows only current revision clouds; archive earlier clouds unless contract requires cumulative clouds.

## Revision table fields

```text
Rev | Date | Description | Drawn | Checked | Approved
R00 | 2026-06-22 | First issue for construction | initials | initials | initials
R01 | 2026-07-05 | Revised living room ceiling and lighting layout | initials | initials | initials
```

## Change request workflow

1. Receive change request/redline/RFI.
2. Log it in change log before drawing.
3. Update affected DWGs and schedules.
4. Add revision clouds/delta marks.
5. Update sheet revision table.
6. Plot PDF and compare with previous issue.
7. Issue with transmittal and archive superseded files.

## As-built rule

For as-built drawings:

- Remove design-intent clouds unless documenting final change history is required.
- Update dimensions/materials based on site-verified information.
- Mark stage as `AB` and revision as final issued revision.
- Keep the source of as-built changes in the change log.
