# Budget Workflow

## Budget levels

1. **Target Budget**: client or design strategy target.
2. **Concept Estimate**: early estimate by category/area.
3. **Design Estimate**: line-item estimate after selections.
4. **Quoted Budget**: supplier quotes.
5. **Approved Budget**: client-approved purchase/contract amount.
6. **Actual Cost**: invoice/final paid.

## Formula basics

For each line item:

```text
Base = Quantity × Unit Price
Subtotal = Base + Freight + Install
Contingency = Subtotal × Contingency %
Tax = (Subtotal + Contingency) × Tax Rate
Total = Subtotal + Contingency + Tax
Variance = Total - Target Budget
Variance % = Variance / Target Budget
```

## Contingency guide

| Certainty | Contingency |
|---|---:|
| fixed supplier quote, valid, spec approved | 0-3% |
| known item but no final quote | 5-8% |
| custom / imported / site-dependent | 10-15% |
| major unknown or volatile category | 15-25% |

## Budget views

Create these views:

- By Room: living, kitchen, bedroom, bathroom, lobby.
- By Package: hard finish, lighting, furniture, art, equipment.
- By Status: pending approval, approved, ordered, delivered, installed.
- By Risk: high cost variance, long lead, approval missing.
- By Supplier: outstanding quotes/orders/payments.

## Client-facing budget hygiene

- Show approved totals and options clearly.
- Do not expose internal supplier margins/discounts unless intended.
- Mark assumptions: tax, freight, installation, exchange rate, validity date.
- Use change orders for client-requested additions/substitutions.

## Red flags

- Unit mismatch: m2 vs pcs vs set.
- Freight/installation forgotten.
- Quote expired.
- Imported item exchange-rate risk.
- Color/finish not approved.
- Long lead item required before design signoff.
