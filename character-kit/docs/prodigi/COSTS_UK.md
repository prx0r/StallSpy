# UK supply + ship costs (model v1 — read the flags)

Wholesale = verified on prodigi.com 2026-09-12. UK shipping = NOT public; pull per-SKU live numbers
from dashboard pricing tool or Quote endpoint before locking retail. Anything marked EST is an
assumption to replace, not a fact. Prices exclude VAT (see Taxation FAQ before margin lock).

## Per-unit wholesale (verified)

| Product | SKU | Wholesale |
|---|---|---|
| Photo mug | GLOBAL-MUG-W | from £3.64 |
| Magic mug | H-MUG-MAGIC-B | from £9.00 |
| Cards (either) | GLOBAL-GRE-* | from £0.75 |
| Cushion 12" | GLOBAL-CUSH-12X12-CAN | from £9.00 |
| Bandana M | PET-BANDANA-MED | from £6.00 |
| Sticker M | M-STI-5_5X5_5 | from £0.80 |
| Print 16x24 | GLOBAL-FAP-16x24 | quote (not listed) |
| Ornament | XMAS-PORC-BAUB | from £8.00 |
| Bauble | XMAS-PLAS-BAUB | from £5.00 |
| Video (any) | — | ~£0.20 generation |

## UK shipping — pull live, do not guess retail on this

Method: Quote endpoint per SKU × destination at order time (returns courier + cost per method:
budget/standard/express). Known Prodigi mechanics: multi-item consolidates (+1 rates, e.g. second
frame adds fraction); nearest-lab routing; dispatch 1–4 days usually, mugs 48–72h, cards 24–72h,
ornaments up to 120h. 100-shop study: keep charged shipping under $6 where possible, 81% of top
shops charge shipping, median $5.70.

## Fee stack per Etsy order (GB)

£0.17 listing + 6.5% transaction + ~3% + £0.25 processing. On £12.99 ≈ £1.55. On £1.99 ≈ £0.55.

## Worked examples (shipping = EST placeholders)

| Bundle | Retail | Wholesale | Ship EST | Fees | Margin EST |
|---|---|---|---|---|---|
| £1.99 clip (digital) | £1.99 | £0.20 | £0 | £0.55 | ~£1.24 |
| Video + direct card £12.99 | £12.99 | £0.95 | £2.00 | £1.55 | ~£8.49 |
| Mug portal £19.99 | £19.99 | £3.64 | £3.50 | £2.22 | ~£10.63 |
| Cushion £29.99 | £29.99 | £9.00 | £4.00 | £3.17 | ~£13.82 |

## To finalize (needs Prodigi login)

1. Dashboard pricing tool → UK standard/budget per each of the 10 SKUs.
2. Confirm VAT treatment on wholesale for UK orders.
3. Replace EST column, lock retails, then set the ~25% shop sale (100-shop tactic) against margin, not hope.
