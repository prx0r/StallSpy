# Prodigi API Reference
**Source:** https://www.prodigi.com/print-api/docs/reference/
**Auth:** X-API-Key header
**Live API:** api.prodigi.com
**Sandbox:** api.sandbox.prodigi.com

## Key Endpoints

### Create Order
POST /v4.0/orders
```json
{
  "merchantReference": "string",
  "shippingMethod": "Budget|Standard|StandardPlus|Express|Overnight",
  "recipient": {
    "name": "string",
    "address": {
      "line1": "string",
      "postalOrZipCode": "string",
      "countryCode": "ISO-3166",
      "townOrCity": "string"
    }
  },
  "items": [{
    "sku": "string",
    "copies": 1,
    "sizing": "fillPrintArea|fitPrintArea|stretchToPrintArea",
    "assets": [{
      "printArea": "default",
      "url": "https://your-cdn/image.png"
    }]
  }]
}
```

### Get Order
GET /v4.0/orders/{id}

### Get Quote
POST /v4.0/quotes

### Product Details
GET /v4.0/products/{sku}

## Key SKUs
- GLOBAL-POSTCARD-4X6 (postcard)
- GLOBAL-FC-5X7 (folded card)
- GLOBAL-FAP-8X10 (fine art print)
- GLOBAL-ACRYLIC-4X6 (acrylic prism)
- GLOBAL-MUG-11OZ (mug)

## Image Requirements
- URL must be publicly accessible
- PNG/JPEG for resizable, PDF for exact size
- sizing: fillPrintArea (default), fitPrintArea, stretchToPrintArea
