# Prodigi Print API (v4) — what MogMug uses

Base URLs: live `https://api.prodigi.com/v4.0`, sandbox `https://api.sandbox.prodigi.com/v4.0`.
Auth: `X-API-Key` header. Sandbox and live keys differ; find/reset in dashboard gear menu.
Sandbox never charges or fulfils; keep data-parity doubts toward live.

Order flow (one step): POST `/Orders` with `shippingMethod`, `recipient`, `items[]`.
Validation happens on create — invalid returns feedback, no order created.
Valid orders submit immediately unless the order-pausing edit window is used.
Always set `merchantReference` (our character/order id) and `idempotencyKey`.

Item: `sku` (exact, from Product Details), `copies`, `sizing` (`fillPrintArea` default crop,
`fitPrintArea`, `stretchToPrintArea` — prefer exact-size artwork, never rely on central crop),
`assets[]` with `printArea` (default `default`) + `url` (hosted https JPG/PNG/PDF only),
optional `md5Hash`. Photobooks need `pageCount` (base price covers 24; mismatch puts order on hold).

Pricing without ordering: POST `/Quotes` with SKUs + destination country (+ optional method).
Returns per-method quotes (budget/standard/standardplus/express/overnight) with fulfilment
location, product cost, shipping cost, courier per shipment.

Discovery: GET `/products/{sku}` returns description, dims, attributes, print areas,
per-variant `shipsTo` + `printAreaSizes` (px at 300 DPI). Use it before rendering print assets.

Ops: images kept 30 days then auto-removed. Status via order object (`Ok`/`Invalid`/`NotYetDownloaded`
per item; asset `complete`/`inProgress`/`error`). Callbacks via `callbackUrl`.
