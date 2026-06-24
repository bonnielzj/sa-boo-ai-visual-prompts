# SA&BOO Starter Token Schema

Use this as a starting point. Replace values with official SA&BOO brand specs when available.

## Color logic

### Primitives

```text
ivory/50      #F7F3EA
ivory/100     #EFE7D8
ink/900       #111111
ink/700       #2A2926
warmgray/100  #E6DFD4
warmgray/300  #B9AEA0
stone/500     #8A8177
champagne/400 #C8AA73
bronze/600    #8B6438
silver/200    #D8D8D6
silver/500    #9B9B9A
accent/red    #8A1F2D
```

### Semantics

```text
color/bg/deep        → ink/900
color/bg/ivory       → ivory/50
color/surface/paper  → ivory/100
color/text/primary   → ink/900
color/text/inverse   → ivory/50
color/text/muted     → stone/500
color/border/subtle  → warmgray/100
color/accent/gold    → champagne/400
color/accent/bronze  → bronze/600
color/accent/silver  → silver/500
color/accent/red     → accent/red
```

## Typography logic

Recommended fallbacks if exact fonts are unavailable:

- Chinese display: `Noto Serif SC` or `Songti SC`
- Chinese body: `Noto Sans SC` or `PingFang SC`
- English display: `Cormorant Garamond`, `Bodoni 72`, or `Playfair Display`
- English/body UI: `Inter`, `Helvetica Neue`, `Arial`

Styles:

```text
text/display/hero       72 / 80 / -2%
text/title/page         40 / 48 / -1%
text/title/section      28 / 36 / -0.5%
text/subtitle           20 / 30 / 0%
text/body               16 / 26 / 0%
text/body/small         14 / 22 / 0%
text/caption            12 / 18 / 2%
text/label              11 / 14 / 8% uppercase
text/quote              24 / 36 / 0%
```

## Spacing and layout

```text
spacing/2xs  4
spacing/xs   8
spacing/sm   12
spacing/md   16
spacing/lg   24
spacing/xl   32
spacing/2xl  48
spacing/3xl  64
spacing/4xl  96
```

## Radius

```text
radius/none 0
radius/sm   4
radius/md   8
radius/lg   16
radius/full 999
```

## CSS syntax convention

Use CSS custom property names like:

```css
--samboo-color-bg-deep
--samboo-color-text-primary
--samboo-spacing-md
--samboo-radius-lg
```
