# BeeSession — The Gift Mission Abstraction
**Date:** 2026-09-06 04:25 UTC
**Status:** CANONICAL — every gift gets a bee, every bee has a mission

---

This is better than a normal basket because it turns what is usually disposable ecommerce state into a **character with memory and narrative continuity**.

The clean abstraction is:

> **A bee is a gift mission.**

Not a user. Not an account. Not merely a cart.

A user can have multiple bees, each carrying one evolving idea/package for one recipient or occasion.

## Canonical model

```text
USER
 │
 ├── Bee: Bartholomew the III
 │      Dad / 60th birthday
 │      GameWinners + mug + card
 │      340 Honey
 │      status: ACTIVE
 │
 ├── Bee: Lucifer von Sting
 │      Girlfriend / anniversary
 │      Movie trailer + acrylic
 │      status: SLEEPING
 │
 └── Bee: Gerald
        Mum / Christmas
        storybook concept
        status: DELIVERED
```

That is much more memorable than:

```text
Saved cart #48372
```

And crucially, it gives us a natural unit for the backend too.

---

# `BeeSession` should become a first-class entity

```json
{
  "bee_id": "bee_83af",
  "user_id": "user_123",
  "state": "active",
  "bee": {
    "name": "Bartholomew the Third",
    "archetype": "pompous",
    "voice": "formal_british",
    "visual_seed": "gold-red-03",
    "traits": ["overconfident", "ceremonial", "fond_of_football"]
  },
  "mission": {
    "recipient_id": "dad_01",
    "occasion": "60th_birthday"
  },
  "gift_state_id": "gs_9182",
  "basket_id": "basket_7291",
  "experience_manifest_ids": [],
  "honey_balance": 120,
  "created_at": "...",
  "last_active_at": "..."
}
```

---

# The random bee generator

Procedurally compose from a controlled system.

### Base body (8-12 canonical rigs)

knight, scholar, postman, eccentric, tiny bureaucrat, explorer, artist, sports commentator, wizard, detective, ordinary Gerald

### Visual modifiers

cape, bow tie, monocle, tiny glasses, helmet, satchel, scarf, waistcoat, clipboard, crown that's slightly too large

### Personality vectors

pomposity, sentimentality, chaos, curiosity, brevity, confidence

### Naming generator

Templates:
- [first name] [ordinal]
- [first name] von [absurd noun]
- Professor [surname]
- Brother [name]
- [name], Keeper of [department]
- [name] the [adjective]

---

# Five bee lifecycle states

### 1. ACTIVE
Bee is currently assigned to the user.

### 2. RESTING
Session stale, nothing discarded.

### 3. PACKED
Customer selected package, near checkout.

### 4. IN_HIVE
Checkout complete, production begins.

### 5. DELIVERED
Mission complete. Bee archived.

---

# The basket becomes a literal satchel

As products are added, tiny items go into bee's satchel.

Click the satchel:

### What Bartholomew is carrying

```text
Dad's GameWinners card
Legend mug
Stadium reveal
Personal message

£31
120 Honey available
```

---

# Checkout becomes narratively excellent

Bartholomew closes his satchel.

> "Right. I believe that's everything."

He checks a tiny clipboard.

> "One GameWinners card, one wholly unnecessary mug, one stadium entrance. Correct."

Customer pays.

> "Excellent. I'll take this back to the hive."

He flies off.

### THE HIVE HAS IT

```text
Artwork being prepared ○
Print queued ○
Packed ○
On its way ○
```

---

# Abandoned baskets become "sleeping bees"

After 24 hours:

> **Bartholomew is still holding Dad's GameWinners idea.**

After a week:

> **Bartholomew has gone back to the hive, but your Dad project is safe.**

---

# The bee becomes a perfect reminder object

Three weeks before Dad's next birthday:

> **Bartholomew has resurfaced.**
> "I regret to inform you that your father is becoming older again."

Tap.

> "Last year we made him Arsenal's greatest-ever striker. Repetition would be lazy. I have three alternatives."

---

# Honey can attach to bees

Each bee can have a Honey allowance:

> Give Bartholomew 50 Honey to experiment.

Bartholomew autonomously spends within budget:

```text
-10 tried alternate portrait
-20 generated stadium sample
-5 asked Lucifer for an opinion
```

---

# The complete lifecycle

```text
        A BEE ARRIVES
              │
              ▼
          NEW MISSION
              │
              ▼
            RAMBLE
              │
              ▼
       BEE LEARNS PERSON
              │
              ▼
         HIVE CONSULTED
              │
              ▼
       CONCEPTS GENERATED
              │
              ▼
        SATCHEL BUILT
              │
        ┌─────┴─────┐
        │           │
      leave       checkout
        │           │
        ▼           ▼
    BEE SLEEPS   BEE RETURNS
    IN HIVE       TO HIVE
        │           │
     reminder       ▼
        │       PRODUCTION
        │           │
        │           ▼
        └──────  DELIVERY
                    │
                    ▼
               MISSION DONE
                    │
                    ▼
               BEE ARCHIVED
```

The bee represents:

**session identity + conversational agent + saved project + basket + recommendation policy + generation budget + order status + retention handle.**

> **Every gift gets a bee. Every bee has a mission.**
