# Unit Economics and CAC Reality

## The mistake to avoid

“Prodigi card costs £1.10 and Moonpig charges £3.99, therefore ~£2.89 profit.”

Wrong.

Real contribution includes:
- product;
- shipping subsidy;
- payment fees;
- AI generation;
- storage/rendering;
- customer service;
- reprints;
- refund leakage;
- discounts;
- marketplace fee (if applicable);
- paid acquisition.

## Contribution formula

```
net_revenue
- production
- fulfilment/shipping subsidy
- payment/platform fee
- AI/render cost
- expected support/reprint/refund cost
= contribution before acquisition
```

Then:

```
allowable_CAC =
contribution_before_acquisition
× desired_first_order_CAC_share
```

Long-term you can spend more if repeat value is proven, but do not borrow imagined LTV.

## Cards

Cards are strategically excellent and economically dangerous.

At low retail prices, a few pounds of ad CAC can erase the order.

Therefore:
- acquire organically;
- sell multi-card packs;
- attach gift;
- sell subscription/free-shipping membership;
- capture reminder;
- email next occasion;
- use referral.

## Higher-AOV products

Puzzles, books/magazines, sets and premium prints are much more capable of carrying:
- creator affiliate payout;
- search ads;
- retargeting.

## Price positioning

Do not anchor the whole brand to “cheapest.”

Possible card tests:
- value: £2.49;
- core: £2.99;
- premium: £3.49;
- bundle: card becomes effectively cheap/free attached to £25+ gift.

The right answer is determined by conversion and contribution, not ideology.

## Gross margin target heuristic

For DTC products that may require paid discovery, prefer a modeled pre-acquisition gross/contribution margin that leaves substantial room—often **55–65%+** is much more comfortable than 30%.

This is a strategic heuristic, not a universal accounting rule.

## Sensitivity example

A £29.00 puzzle:
- production: £10.00
- shipping subsidy: configurable
- payment: configurable
- AI/render: typically low relative to physical cost
- support/reprint reserve: configurable

Could plausibly support meaningful CAC.

A £2.99 card cannot.

## The key blended metric

Track:
**contribution per recipient acquired**, not merely per SKU.

If a customer:
1. buys card;
2. saves Mum's birthday;
3. buys Christmas ornament;
4. receives reminder;
5. buys next birthday gift;

the first card can be strategically valuable.

But prove this with cohorts.

## Files

Use `scripts/unit_economics.py` with your actual supplier and marketing numbers.
