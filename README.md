# Giggle Blanks

A fill-in-the-blank story game for kids around age 6–7. Kids answer one word prompt at a
time (noun, adjective, past tense verb, and so on), each with a plain-language meaning and
example words. Then the finished story is revealed for reading aloud.

- 270 original, hand-curated stories across 27 themes
- Real part-of-speech prompts as a gentle grammar lesson
- Every blank is a separate word (no repeated answers)
- "a" / "an" adjusts automatically to the word the child picks
- "Pick for me" helper, read-aloud button, and remembers which stories were played
- Works in light and dark mode, phone or desktop; one self-contained HTML file

## Files

| Path | What it is |
| --- | --- |
| `giggle-blanks.html` | The built app. Open it in any browser. |
| `stories/*.json` | The story library, one file per theme. |
| `app.template.html` | App page with a placeholder where the stories go. |
| `build.py` | Combines the template and all stories into `giggle-blanks.html`. |
| `validate.py` | Checks stories against the style guide (blank types, counts, grammar traps, wording). |
| `STYLE_GUIDE.md` | Rules for writing new stories. |

## Adding or editing stories

1. Edit or add a file in `stories/` following `STYLE_GUIDE.md`.
2. Check it:

   ```
   python3 validate.py stories/*.json
   ```

3. Rebuild the app:

   ```
   python3 build.py
   ```

Requires only Python 3 (no packages).
