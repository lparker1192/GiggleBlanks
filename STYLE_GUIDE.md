# Mad Libs Story Style Guide

Audience: children age 6–7, usually playing with a parent. A grown-up may read the
story aloud, but it should also be readable by a strong first/second grader.

## File format

Each theme is one JSON file: an array of story objects.

```json
[
  {
    "id": "space-01",
    "theme": "Space",
    "title": "My First Day on the Moon",
    "text": "Today I flew to the moon in a {adjective} rocket. ..."
  }
]
```

- `id`: `<theme-slug>-NN`, two-digit number, unique.
- `title`: short, fun, no blanks in the title.
- `text`: the story. Blanks are written as `{type}` using ONLY the types below.
  Use `\n\n` between paragraphs (2–4 short paragraphs).

## Allowed blank types (exact spelling, lowercase)

Parts of speech (the learning focus — most blanks should be these):
- `{noun}` — a person, place, or thing
- `{plural noun}` — more than one thing (shoes, pickles)
- `{verb}` — an action word in its plain form (jump, wiggle)
- `{verb ending in ing}` — (jumping, wiggling)
- `{past tense verb}` — (jumped, wiggled)
- `{adjective}` — a describing word (fuzzy, enormous)
- `{adverb}` — describes how something is done, usually ends in -ly (quickly, loudly)

Light extras (use sparingly, at most 4 per story):
- `{number}`, `{color}`, `{animal}`, `{food}`, `{place}`, `{body part}`,
  `{silly word}`, `{sound}`, `{exclamation}`, `{name}`

## Hard rules

1. Every blank is its own word — NEVER design a story that expects a word to repeat.
   Do not write "the {noun}" and later refer back to "the same thing".
2. 12 to 16 blanks per story, like a classic Mad Libs page. At least 9 must be parts of
   speech (first list). Use at least 4 different part-of-speech types per story.
3. Length: 100–165 words of story text (not counting blanks), and no more than 12 words
   per blank on average. Nearly every sentence should have a blank; avoid long stretches
   of plain setup. Short and punchy beats long and explained.
4. Grammar must work with ANY reasonable answer:
   - Write `a` before a blank (the app fixes a/an automatically). Never write `an {..}`.
   - Do not start a sentence with a blank.
   - `{plural noun}` only where a plural fits ("three {plural noun}"). `{noun}` only where a singular fits.
   - `{verb}` only after words like "to", "can", "will", "would", "didn't", "let's", "please".
   - Do not attach suffixes to blanks (no `{noun}s`, no `{verb}ed`).
   - `{number}` should work as a word or digit; follow it with a `{plural noun}` or a plural word.
5. Age appropriate: no violence, weapons, injuries, scary peril, death, romance,
   kissing, crushes, potty/bathroom words, insults, mean jokes about people, junk-food
   shaming, body shaming, brands, real celebrities, or anything a parent would wince at.
   Mild silliness is great: burps are too far, sneezes and "a little bit smelly" are fine.
   Pirates have treasure maps, not swords. Monsters are friendly. Halloween is costumes and candy.
6. No reused titles across the library.

## What makes it funny (most important part)

- The narrator is completely sincere and matter-of-fact: a diary, a report, a list of
  rules, a letter, a recipe, a news report, a postcard, an announcement, instructions.
  Vary the format across a theme — do not write ten diary entries.
- Put blanks exactly where the reader expects one sensible word: the punchline spot.
  "Grandma's secret ingredient is always a pinch of {plural noun}."
- Surround blanks with specific, ordinary details so the silly word collides with reality:
  "Our teacher, Mr. Pots, wrote {plural noun} on the board in big letters."
- Rules, warnings, and "fun facts" are gold: "Never feed the giraffe after {number} o'clock."
- End with a satisfying closing line that has a blank in it.
- Clean, kid-sized vocabulary in the fixed text. Short sentences.
- No narrator commentary about the story being silly.

## Example (shape only, do not copy)

Title: Rules for the Classroom Hamster

"Our class hamster is named Pickles. Pickles is very {adjective} and likes to sleep
inside a {noun}. Every morning, someone must feed him three {plural noun} and a cup
of {food}.

Please do not {verb} near his cage. The last time someone did that, Pickles
{past tense verb} for a whole hour and would not stop. Mrs. Lee says he is very
{adjective} about his feelings.

On Fridays, Pickles gets to run around the room. Be careful! He moves {adverb} and
likes to hide in people's {plural noun}. If you see him, shout "{exclamation}!" and
someone will come help."
