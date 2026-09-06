# The Game Crafter (Wing API) Reference
**Source:** https://www.thegamecrafter.com/developer/
**Auth:** session_id cookie or query param
**Base:** https://www.thegamecrafter.com/api/

## Key Features
- RESTful API (JSON)
- Create games, cards, decks, tuck boxes
- Commerce API (cart, checkout with account credit)
- 240 requests/minute rate limit

## Game Component APIs
- Deck & Card (trading cards)
- TuckBox (card packaging)
- Booklet & BookletPage
- PerfectBoundBook
- AcrylicShape
- CustomPrintedMeeple

## Commerce APIs
- Cart (create, add items, checkout)
- Shipment
- Receipt

## Authentication
- session_id cookie or query param
- Get session: POST /api/session

## Key for MythicBee
- Programmable collectible cards
- Custom tuck boxes
- Booster packs
- GameWinnerz card packs
- Family collectible sets
- No MOQ for experimentation

## Workflow
1. Create account, get API key
2. Create Deck/Card objects
3. Create Cart
4. Add items to cart
5. Assign shipping address
6. Checkout with account credit
