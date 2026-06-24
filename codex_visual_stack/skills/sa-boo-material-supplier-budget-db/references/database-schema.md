# Database Schema

## Relationship map

```text
Suppliers 1---n Materials
Materials 1---n Price History
Materials n---n Projects through Project Budget / FF&E Schedule
Project Budget 1---n Procurement Tracker
Project Budget 1---n Approvals / Substitutions
```

## Table: Materials

| Field | Type | Notes |
|---|---|---|
| Material ID | text | MAT-0001 |
| Category | select | floor, wall, stone, wood, metal, textile, lighting, furniture... |
| Subcategory | text | marble, veneer, paint, pendant, sofa... |
| Brand | text | manufacturer/brand |
| Product Name | text | official name |
| Model / SKU | text | code |
| Color / Finish | text | finish, color, texture |
| Size / Spec | text | dimensions/thickness/wattage/etc. |
| Unit | select | m2, m, pcs, set, roll, liter |
| Unit Price Low | currency | min observed price |
| Unit Price High | currency | max observed price |
| Currency | select | CNY, USD, EUR... |
| Default Supplier ID | relation | preferred supplier |
| Lead Time Days | number | typical lead time |
| MOQ | text/number | minimum order |
| Sample Available | checkbox | sample library status |
| Certification | text | VOC, fire rating, FSC, CE, GB, etc. |
| Maintenance | text | cleaning/repair notes |
| Sustainability Notes | text | low VOC/recycled/FSC only if proven |
| Image URL / File | attachment/url | product/material photo |
| Source URL | url | supplier page/catalog |
| Status | select | active, preferred, watch, discontinued |
| Risk Notes | text | color batch, fragile, long lead, install complexity |
| Last Verified | date | price/spec verification date |

## Table: Suppliers

| Field | Type | Notes |
|---|---|---|
| Supplier ID | text | SUP-0001 |
| Supplier Name | text | company/contact name |
| Category | multi-select | stone, wood, furniture, lighting... |
| Contact Person | text | primary contact |
| Phone / WeChat | text | private; protect when sharing |
| Email | text |  |
| City / Region | text | service area |
| Website / Shop | url |  |
| Price Level | select | low, mid, high, luxury |
| Quality Score | number | 1-5 |
| Reliability Score | number | 1-5 |
| Service Score | number | 1-5 |
| Lead Time Score | number | 1-5 |
| Documentation Score | number | 1-5 |
| Overall Score | formula | weighted average |
| Payment Terms | text | deposit, balance, credit |
| Warranty / After-sales | text |  |
| Cooperation Notes | text |  |
| Status | select | preferred, backup, trial, avoid |
| Last Contact | date |  |

## Table: Price History

| Field | Type | Notes |
|---|---|---|
| Price ID | text | PRICE-0001 |
| Material ID | relation |  |
| Supplier ID | relation |  |
| Date | date | quote date |
| Unit Price | currency | typed number |
| Currency | select |  |
| Tax Included | checkbox |  |
| Freight Included | checkbox |  |
| Install Included | checkbox |  |
| Quote Valid Until | date |  |
| Source | text/url | quote/file/source |
| Notes | text | conditions |

## Table: Project Budget / FF&E Schedule

| Field | Type | Notes |
|---|---|---|
| Line ID | text | PB-0001 |
| Project | text/relation | project name/id |
| Area / Room | text | living room, bath, lobby... |
| Package | select | hard finish, lighting, furniture, art, sanitary... |
| Item | text | item description |
| Material ID | relation | optional |
| Supplier ID | relation | optional |
| Spec | text | model/finish/size |
| Quantity | number |  |
| Unit | select | m2, pcs, set... |
| Unit Price Estimate | currency | initial estimate |
| Quote Unit Price | currency | supplier quote |
| Approved Unit Price | currency | client approved |
| Tax Rate | percent | use formula |
| Freight | currency |  |
| Install Cost | currency |  |
| Contingency % | percent | 5-15% typical depending uncertainty |
| Estimated Total | formula | qty × estimate + extras |
| Quoted Total | formula | qty × quote + extras |
| Approved Total | formula | qty × approved + extras |
| Target Budget | currency | optional per line/room/package |
| Variance | formula | approved/quoted - target/estimate |
| Approval Status | select | pending, approved, rejected, revise |
| Procurement Status | select | not started, quoted, ordered, paid, shipped, delivered, installed, closed |
| Required Date | date | site schedule |
| Risk Level | select | low, medium, high |
| Notes | text |  |

## Table: Approvals

| Field | Type | Notes |
|---|---|---|
| Approval ID | text | APR-0001 |
| Project | relation/text |  |
| Line ID | relation | project budget line |
| Decision | select | approved, rejected, pending, conditional |
| Approved By | text | client/person |
| Date | date |  |
| Evidence | url/file | screenshot, signed PDF, email |
| Notes | text |  |

## Table: Substitutions

| Field | Type | Notes |
|---|---|---|
| Substitution ID | text | SUB-0001 |
| Project | relation/text |  |
| Original Material ID | relation |  |
| Replacement Material ID | relation |  |
| Reason | select | budget, stock, lead time, quality, client change |
| Cost Impact | currency | +/- |
| Schedule Impact Days | number |  |
| Design Impact | text | visual/quality impact |
| Approval Status | select | pending, approved, rejected |
| Notes | text |  |
