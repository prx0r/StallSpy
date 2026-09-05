# MythicBee — Product Templates

## Template-Driven Architecture

Each template specifies its own input contract. Customer uploads exactly what's needed. No prompt box. No guesswork.

---

## Template: Birthday Roast — Family Intervention

**Slug:** `ROAST_FAMILY_V1`

**Upload:**
- recipient face (required)
- Mum face (required)
- Dad face (required)
- dog photo (optional)

**Tell us:**
- age
- 3 embarrassing facts
- one running joke
- roast intensity (gentle / savage / brutal)

**Output:**
- 20-second mock intervention
- Mum, Dad and the dog roast them
- Birthday sting ending

---

## Template: Nature Documentary

**Slug:** `NATURE_DOC_V1`

**Upload:**
- 3-5 photos of recipient

**Tell us:**
- habits
- job
- hobbies
- any running gags

**Output:**
- David Attenborough-style format (original narrator, no impersonation)
- Serious documentary observing "Tom in his natural habitat"
- 15-20 seconds

---

## Template: Breaking News

**Slug:** `BREAKING_NEWS_V1`

**Upload:**
- face

**Tell us:**
- age
- funny fact

**Output:**
- Studio anchor intro
- Field reporter on scene
- Ridiculous reconstruction
- Birthday sting
- 15 seconds

---

## Template: The Trial of [NAME]

**Slug:** `TRIAL_V1`

**Upload:**
- recipient face (required)
- 2 friends' faces (required)
- pet photo (optional)

**Tell us:**
- their "crimes" (3 charges)
- one mitigating circumstance

**Output:**
- Courtroom drama
- Everyone testifies against them
- Judge delivers verdict
- 20 seconds

---

## Template: Meet [NAME]

**Slug:** `MEET_BIO_V1`

**Upload:**
- 5 photos of recipient

**Tell us:**
- personality
- story
- occasion

**Output:**
- 30-second premium mock biopic
- Narrated documentary style
- Multiple scenes
- Emotional/funny arc

---

## Template: Santa In Your Room

**Slug:** `SANTA_ROOM_V1`

**Upload:**
- room photo (required)
- child/pet photo (optional)

**Tell us:**
- child's name
- age
- what they want for Christmas

**Output:**
- Santa placing presents under their tree
- Looks at camera, says something personalized
- 10-15 seconds

---

## Template: Monster In Your Room

**Slug:** `MONSTER_ROOM_V1`

**Upload:**
- room photo (required)
- child/pet photo (optional)

**Tell us:**
- child's name
- favorite monster type

**Output:**
- Monster beside their bed / in their room
- Caught on "security camera" footage
- 10 seconds

---

## Template: Had To Do It To Em

**Slug:** `DO_IT_V1`

**Upload:**
- full body photo (required)

**Tell us:**
- name
- occasion
- what they "had to do"

**Output:**
- Cinematic walk into frame
- Classic pose
- Camera circles
- Text: "YOU KNOW [NAME] HAD TO [ACTION] ON 'EM"
- 10 seconds

---

## Template: Dog Interview

**Slug:** `DOG_INTERVIEW_V1`

**Upload:**
- dog photo (required)

**Tell us:**
- dog's name
- what the dog "thinks" about the recipient
- occasion

**Output:**
- Dog at podium / interview setup
- "Speaks" about the recipient
- 10-15 seconds

---

## Template: Custom Song

**Slug:** `CUSTOM_SONG_V1`

**Upload:**
- 1-3 photos

**Tell us:**
- recipient name
- occasion
- 3 things to include in lyrics
- tone (funny / wholesome / roast)

**Output:**
- 30-60 second original song
- Photos displayed with music
- Downloadable audio file

---

## Input Contract Standard

Every template defines:

```text
SLUG: [template_name]
VERSION: v1

REQUIRED UPLOADS:
- [photo type] (required/optional)

QUESTIONS:
- [question] (type, constraints)

OUTPUT FORMATS:
- [aspect ratio]
- [duration]
- [quality tier]

QA CRITERIA:
- [check]
```

**This is the product.** Not prompts. Not models. Not GPUs.

The customer sees: "Upload 3 photos, answer 4 questions, get a movie."
