# Prodigi pricing + shipping model

Model: Prodigi charges wholesale (product + shipping + tax); we set retail, keep the spread.
Site prices exclude VAT. Exact numbers live behind login — dashboard pricing/shipping tool
(filters by category + destination) and the Quote endpoint are truth, not this file.
Prodigi Pro saves ~15% catalogue-wide (mugs/cards cited) plus insert discounts.

Methods: Budget / Standard / StandardPlus / Express / Overnight (FAQ lists four, API five —
request the quote and read what comes back). Shipping covers pick/pack/handle/packaging.

Multi-item: consolidated, not per-item full rate. Frames/canvases: largest sets full charge,
others add small +1 (e.g. A1 + A5 UK standard = £11.50 + £3.00). Rolled prints: flat rate in
most regions, no +1. Split facilities combine per-facility costs.

Dispatch (production) mostly 1–4 days; global wall-art lines 24–48h. Mugs 48–72h, cards 24–72h.
Shipping time adds on top — overnight means next day after dispatch, not after order.
Routing is automatic to the nearest lab (shorter distance, lower footprint).

For MogMug pricing: quote every portal SKU × destination at order time; never cache prices.
