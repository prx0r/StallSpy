# Prodigi import — index

Imported 2026-09-12 from prodigi.com (sources below). Live prices/dims change: treat the **API as truth**
(Product Details + Quote endpoints), these notes as the map.

- `api.md` — environments, keys, order/quote flow, assets, sizing, file rules
- `products.md` — MogMug SKUs: mugs, cards, with print areas + production times
- `pricing-shipping.md` — wholesale model, methods, +1 rates, dispatch, routing
- `etsy-integration.md` — Etsy auto-fulfilment (alternative to API per-order path)

Sources:
- https://www.prodigi.com/faq/print-api/
- https://www.prodigi.com/print-api/docs/ and /print-api/docs/reference/
- https://www.prodigi.com/blog/your-first-print-api-order/
- https://www.prodigi.com/faq/payments-and-pricing/
- https://www.prodigi.com/faq/shipping/
- https://www.prodigi.com/etsy-print-on-demand/
- https://www.prodigi.com/products/home-and-living/drinkware/photo-mugs/
- https://www.prodigi.com/products/cards-and-stationery/greetings-cards/fine-art-greetings-cards/

Live SKU data needs a Prodigi API key (dashboard → gear → Show API key; sandbox and live keys differ).
Key storage: agent-vault `prodigi` vault. Never hardcode keys.
