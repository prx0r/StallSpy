# Seasonal playbook

Seasonality is a first-class concern because gifting demand is seasonal and MythicBee should feel alive throughout the year.

## Principle

**Seasonal inheritance, not seasonal replacement.**

A Christmas session is still MythicBee. Bartholomew does not suddenly become a Christmas-only mascot; the same Hive has entered Christmas operations.

The season may affect:

- phrase pack
- small visual tokens
- ambient environment
- bee wardrobe
- department names
- loading micro-choreography
- product weighting upstream
- email voice
- recipient reveal decoration

It should not change:
- data model
- core recommendation quality
- commerce rules
- accessibility
- trust promises

## Christmas

Visual:
- warm gold
- restrained red/green
- snow outside Hive windows
- scarves / postal satchels

Status language:
- elves
- wrapping
- chimneys
- production rush
- Count Buzz

Avoid:
- every sentence being a Christmas pun
- fake Christmas urgency
- Santa claims that could confuse fulfilment status

## Halloween

Visual:
- violet/orange
- low fog
- tiny candlelight
- Lucifer becomes slightly more prominent

Status language:
- crypts
- trick-or-treaters
- tasteful curses
- fog
- noises under the hive

## Valentine's

Visual:
- warmer rose accents
- restrained hearts

Status language:
- memory
- sentimentality
- trying not to make it too soppy

## Father's / Mother's Day

These should feel more like departmental seasonal operations than costume events.

They can heavily affect upstream product ranking while HiveActivity stays relatively restrained.

## Explicit override

Some holidays have different dates by country (notably Mother's Day).

For those, set `explicitOnly` in the built-in theme and resolve the season upstream based on the customer's locale, then pass `season: "mothers-day"`.
