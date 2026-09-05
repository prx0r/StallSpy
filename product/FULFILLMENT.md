# Dogcasso — Fulfillment Pipeline

## Digital Delivery (Primary)

```text
Customer completes purchase
        ↓
Payment processed (Stripe)
        ↓
Job queued with priority tier
        ↓
GPU renders video (Vast.ai / RunPod)
        ↓
FFmpeg composes final output
        ↓
QA checks pass
        ↓
Gift page created: dogcasso.com/tom-30th-8F4D
        ↓
Delivery email/SMS with link
        ↓
Customer shares link in group chat
```

### Gift Page Contents

- Movie (autoplay on load)
- Card artwork (if purchased)
- Personalized message
- Photos used
- Song (if purchased)
- Download buttons (HD, SD, vertical, horizontal)
- Share to WhatsApp / iMessage / social
- Copy link
- Date stamp: "Tom's birthday — 19 October 2026"

**Permanent retention.** Unlike Moonpig's 6-month limit, Dogcasso gift pages stay live.

---

## Physical Card Delivery (Upsell)

```text
Movie generated
        ↓
AI creates matching card artwork
        ↓
Card PDF generated (front + inside + back)
        ↓
QR code generated (unique gift page URL)
        ↓
QR placed inside card
        ↓
Prodigi API called
        ↓
Prodigi prints + mails (24-72 hrs)
        ↓
Customer receives confirmation + tracking
```

### Prodigi Integration

- **API:** Print-on-demand, no minimum order
- **Card types:** Classic greeting cards, premium, giant
- **Wholesale cost:** ~£0.75-1.10 per card (before VAT/shipping)
- **Turnaround:** 24-72 hours depending on card type
- **Fulfillment:** Prodigi handles printing + shipping globally
- **We don't touch the physical card.**

---

## Storybook Delivery (Future)

```text
Movie generated
        ↓
AI expands story from personalization data
        ↓
AI generates page illustrations (5-10 pages)
        ↓
Layout composed as PDF
        ↓
Lulu Print API called
        ↓
Lulu prints + dropships hardcover
        ↓
Customer receives confirmation + tracking
```

### Lulu Integration

- **API:** Print-on-demand books, global fulfillment
- **Supports:** AI/customer-input personalized books
- **Output:** PDF → printed hardcover/softcover
- **Dropshipping:** Global

---

## QR → AR Path (Future)

### Version 1: QR → Gift Page (Launch)

Scan QR → beautiful mobile gift page → movie autoplay.

Bulletproof. Works everywhere.

### Version 2: WebAR (Later)

Scan QR → browser opens camera → point at card → movie appears spatially attached to the card.

- No app required (WebAR/image tracking runs through mobile browser)
- Card artwork becomes tracking marker
- Santa walks out of printed fireplace
- Birthday person pops out of card

### Version 3: Holographic (Far future)

Same content, different display target. The valuable asset is **the personalized scene**, not its display format.

---

## Unique URL Structure

```
dogcasso.com/tom-30th-8F4D
dogcasso.com/sarah-santa-9K2M
dogcasso.com/dave-retirement-7P1Q
```

- Human-readable prefix
- Random suffix for uniqueness
- Permanent (no expiry)
- Shareable as plain text
- Works in group chats, QR codes, social media

---

## Delivery Channels

| Channel | Use case |
|---------|----------|
| **Email** | Primary delivery, receipt, gift notification |
| **SMS** | Quick share, gift link |
| **WhatsApp** | Group chat sharing (major channel) |
| **iMessage** | Apple users |
| **Direct link** | Any platform |
| **QR code** | Physical card → digital movie |

---

## Quality Assurance

Every output passes:

1. **Face check:** Recipient face visible and recognizable
2. **Audio check:** Speech clear, no artifacts
3. **Timing check:** Punchline lands, no awkward pauses
4. **Brand check:** No offensive content, no IP infringement
5. **Format check:** Correct aspect ratio, resolution, file size

**Reroll policy:** If QA fails, auto-reroll up to 2 times. If still fails, escalate to manual review.
