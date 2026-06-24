# SA&BOO Annotation and Dimension Standard

## Units and scale

- Model space: draw real size, 1:1, millimeters.
- Layout space: arrange sheets and viewports; lock viewport scale.
- Use annotative text/dim styles when possible.
- If not annotative, model text height = paper text height × drawing scale.

Examples:

| Printed height | 1:20 | 1:50 | 1:100 |
|---:|---:|---:|---:|
| 2.5mm body/dim | 50 | 125 | 250 |
| 3.5mm subtitle | 70 | 175 | 350 |
| 5.0mm title | 100 | 250 | 500 |

## Text styles

| Style | Printed height | Use |
|---|---:|---|
| SABOO-TEXT-BODY | 2.5mm | notes, material names, room names |
| SABOO-TEXT-SMALL | 2.0mm | dense detail notes only |
| SABOO-TEXT-SUBTITLE | 3.5mm | drawing subtitles, elevation labels |
| SABOO-TEXT-TITLE | 5.0mm | drawing title under views |
| SABOO-TEXT-SHEET | 7.0mm | sheet title/title block emphasis |

Font recommendation:

- Chinese: SimSun / Songti SC / Noto Sans CJK SC / 仿宋 as project permits.
- English/numbers: Arial / Helvetica / Inter-like sans.
- Keep issued PDF legible; if font substitution occurs, convert/check before issue.

## Dimension rules

- Use associative dimensions (`DIMASSOC=2`).
- Use consistent dimension hierarchy:
  1. Overall dimension
  2. Axis/main wall dimension
  3. Opening/door/window dimension
  4. Detail/local dimension
- Avoid duplicate or conflicting dimensions.
- Dimensions should not cross important geometry when avoidable.
- Use millimeters, typically no decimals for interior construction unless detail requires.
- For cabinetry/joinery, dimension finished face, opening, clearances, and critical install heights.

Suggested dimension style:

```text
Text printed height: 2.5mm
Arrow size: 2.5mm
Extension line offset: 1.0mm printed
Extension beyond dimension line: 2.0mm printed
Dimension line spacing: 7-10mm printed
Precision: 0 for mm general drawings; 0.0 only for special details
```

## Leaders and notes

- Use multileaders for material notes and construction notes.
- Leader landing line should be short and aligned.
- Note format: `编号 + 材料/做法 + 关键规格 + 参见详图/清单`.
- Example: `W-01 艺术涂料，暖灰色，哑光，基层找平后施工，详见材料表`.

## Common symbols

- Section/elevation/detail symbols on `I-ANNO-SYMB`.
- Material tags on `I-ANNO-TAGS`.
- Door/window/furniture tags must match schedules.
- North arrow/scale bar where relevant; interior plan often depends on title/scale instead.

## Sheet title rule

Each view must have:

```text
图名 + 比例 + 索引/详图编号（如需要）
```

Example:

```text
一层平面布置图  1:50
客厅电视背景立面图  1:30
收口节点详图  1:5
```
