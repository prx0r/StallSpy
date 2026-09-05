No dedicated GPU needed for **8th Wall / Three.js AR itself**. The phone does the rendering. You host a normal HTTPS web app; the customer's camera + WebGL handle the experience. 8th Wall currently requires WebGL, camera access and WebAssembly SIMD on supported mobile browsers. Its open-source framework includes **image targets**, which is exactly the "point camera at card" primitive. ([8th Wall][1])

Three.js is basically the rendering layer: load a `.glb`, animate it, particles, lighting, interaction, etc. Its WebXR support sits on top of WebGL/WebGPU. ([Three.js][2])

The GPU-heavy bit happens **beforehand** when we make the asset:

**customer pet photos → AI portrait/video/3D model → store asset → customer scans card → phone renders it.**

Meshy already exposes single- and multi-image-to-3D APIs and outputs GLB/FBX/USDZ etc., including topology controls and up-to-8K textures. That gives us a very obvious premium future tier. ([Meshy Docs][3])

### Pokémon/Yu-Gi-Oh/Magic: don't sell direct copies

Yes, direct "custom Pokémon card" is exactly the sort of thing I'd avoid building the company around. Pokémon explicitly says its artwork, graphics, logos etc. are protected; Konami similarly protects Yu-Gi-Oh branding, designs and associated materials. **Top Trumps itself is also a registered trademark owned by Winning Moves.** ([Pokémon][4])

But the underlying idea:

**character + portrait + stats + abilities + rarity + collectible card**

is much broader than Pokémon.

So make **Dogcasso's own collectible universe**.

And this could be really good.

## Dogcasso "Pet Legends"

Imagine:

**JEFF**
*Legendary Food Hound*

❤️ Vitality: 94
⚡ Zoomies: 78
🧠 Intelligence: 41
🍗 Appetite: 999

**SPECIAL: THE VACUUM**
Jeff instantly consumes all edible objects within three metres.

**WEAKNESS:** Bath Time

Then the physical card has holographic foil.

Scan it.

The card shakes.

Particles come out.

Jeff literally leaps out of the card in 3D.

Tap **USE SPECIAL**.

He executes his unique animation.

That has the Pokémon psychological appeal without pretending to be Pokémon.

And **each pet's abilities can come from a little questionnaire**, so personalization goes much deeper than changing a photograph.

---

# There are loads of adjacent concepts

The ones I'd actually investigate:

### 1. **Pet Boss Battle**

Birthday recipient is presented as a video-game boss.

**BIRTHDAY BOSS: DAD**

Jeff is his companion/minion.

HP: 40
Special Attack: Dad Joke
Resistance: Going Out After 9pm

Scan → animated boss-intro sequence.

Extremely giftable.

---

### 2. **Pet RPG Character Sheet**

Not D&D branded.

**JEFF — Level 8 Canine Rogue**

Class: Snack Thief
Alignment: Chaotic Hungry
Inventory:

* one stolen sock
* tennis ball
* unidentified garden object

Scan → little 3D RPG character appears.

This has enormous nerd/fantasy overlap without needing licensed IP.

---

### 3. **Fantasy Familiar**

This might be beautiful rather than jokey.

Your cat becomes:

**Milo, Familiar of the Western Tower**

element
constellation
magical ability
temperament
prophecy

Physical foil card / ornate portrait.

AR makes the familiar appear.

This hits witchy/tarot/fantasy Etsy extremely naturally.

---

### 4. **Pet Tarot / Oracle**

Not generic "your dog on tarot art".

Actually personalized:

**THE DEVOURER**

Meaning:
abundance, enthusiasm, inability to leave unattended sandwiches alone.

Scan → animated mystical version of the pet.

Could sell individual cards or eventually decks.

---

### 5. **Wanted / Bounty Poster**

This one remains extremely strong.

**WANTED**

Jeff

REWARD: £10,000

CRIMES:

* aggravated sock theft
* destruction of sofa
* resisting bath
* impersonating a good boy

Then the **printed photograph starts moving when scanned.**

This might actually be better commercially than full 3D because the AR interaction is obvious.

---

### 6. **Wildlife Field Specimen**

Your Natural Habitat idea extended physically.

**SPECIES:** *Canis Jeffus Maximus*

Habitat: kitchen doorway
Diet: everything
Predators: vacuum cleaner
Average sleep: 17 hours

Looks like an old natural-history specimen card.

Scan → Attenborough-style clip.

I like this a lot because **Dogcasso owns the whole format.**

---

### 7. **Sports Rookie Card**

No league/team trademarks.

**Jeff — 2026 Rookie Season**

Speed: 87
Catching: 32
Ball Possession: NEVER RETURNS BALL

Could be baseball-card / football-card / racing-card aesthetics without copying an actual league's card design.

Scan → sports intro.

---

### 8. **Arcade Fighter Card**

This could be extremely viral.

Portrait of Mum/Dad/dog.

**JEFF**

FIGHTING STYLE:
Unprovoked Barking

Finishing move:
**THE ZOOMIE**

Scan → "READY / FIGHT" → animated move.

Again: generic fighting-game grammar, own visual system.

---

### 9. **Secret Agent Dossier**

**AGENT J-007**

Codename: Biscuit
Specialism: surveillance from sofa
Known aliases: Jeff, Jeffrey, Stop That

Scan → cinematic spy intro.

Birthday/Father's Day version is obvious.

---

### 10. **Movie Character Poster**

This is where the original funny films feed back into commerce.

Not:

> put me in *The Godfather*

but:

> **Make Dad the boss of a 1970s crime family**

Own title.

Own characters.

Own poster.

Then generate a 15-second trailer.

You preserve nearly all the fantasy while building Dogcasso IP instead of somebody else's.

---

## One I think kids would go nuts for: **Evolution Cards**

Not Pokémon evolution.

Their pet has **three life stages**:

**PUP → HERO → LEGEND**

Customer uploads puppy and current photos.

AI invents a fantastical final form based on personality.

Example:

Jeff as puppy
→ Jeff now
→ **JEFF THE ETERNAL SNACK LORD**

Three-card set.

Scan each card and it transforms.

That is a genuinely differentiated personalized gift.

It also creates obvious upselling:

**1 card £7.99**
**3-card evolution set £16.99**
**physical holo set £24.99**
**AR edition +£5**

---

# Another strong category: "real-world person as fictional artifact"

Your Sirius Black instinct points to a broader formula.

Rather than sell fandoms, identify the **artifact people want to exist inside**.

Examples:

* fantasy wanted poster
* magical newspaper
* wizard portrait
* royal oil painting
* superhero dossier
* wrestler entrance card
* football transfer announcement
* 90s wrestling poster
* medieval manuscript
* old newspaper front page
* museum specimen
* adventurer passport
* spy dossier
* tarot card
* RPG inventory screen
* retro videogame character screen
* VHS horror box
* movie poster
* album cover
* action-figure packaging
* cereal box
* magazine cover
* postage stamp
* banknote
* presidential portrait
* ancient coin
* stained-glass saint
* illuminated manuscript

That's probably a much bigger idea than pets alone:

> **Turn somebody you love into an artifact from a world they love.**

Birthday + recognizable obsession + personalized recipient = strong buying motive.

---

## But for Dogcasso right now

I would resist expanding today.

Build the hierarchy:

**1. Perfect portrait**
↓
**2. Perfect 15-sec animation**
↓
**3. Physical card using same portrait**
↓
**4. Scan card → animation anchored to card**
↓
**5. Original collectible card**
↓
**6. Meshy 3D pet comes out of it**
↓
**7. Same persistent pet avatar can eventually enter mini-games**

The cool thing is each step preserves the assets created in the previous step.

And I suspect **step 4 is the sweet spot**, not 3D yet. A convincing moving/escaping portrait can look magical while just using image tracking + transparent/segmented video. That's much lighter, cheaper and more photorealistic than trying to make every customer's bulldog a perfect rigged mesh.

If that sells, then the 3D avatar stops being a speculative feature and becomes the obvious premium upgrade.

[1]: https://8thwall.org/docs/troubleshooting/browser-requirements "Browser Requirements | 8th Wall"
[2]: https://threejs.org/docs/pages/WebXRManager.html "WebXRManager - Three.js Docs"
[3]: https://docs.meshy.ai/en/api/image-to-3d "Image to 3D API | Meshy Docs"
[4]: https://www.pokemon.com/us/legal/copyright "Copyright | Pokemon.com"
