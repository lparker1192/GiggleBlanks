"""Check Mad Libs story files against the style guide.

Usage:
  python3 validate.py stories/space.json [more files ...]
  python3 validate.py stories/*.json
Prints problems per story and a summary. Read-only: never changes any file.
"""
import json
import re
import sys

POS = {"noun", "plural noun", "verb", "verb ending in ing", "past tense verb",
       "adjective", "adverb"}
EXTRAS = {"number", "color", "animal", "food", "place", "body part",
          "silly word", "sound", "exclamation", "name"}
ALLOWED = POS | EXTRAS
BLANK = re.compile(r"\{([^{}]*)\}")
BANNED = ["kiss", "crush", "girlfriend", "boyfriend", "poop", "pee", "fart", "burp",
          "butt", "toilet", "sword", "gun", "knife", "kill", "dead", "die ", "died",
          "blood", "stupid", "dumb", "hate", "shut up", "idiot", "fat ", "ugly"]


def check_story(s, seen_ids, seen_titles):
    probs = []
    for key in ("id", "theme", "title", "text"):
        if not isinstance(s.get(key), str) or not s.get(key).strip():
            probs.append(f"missing or empty '{key}'")
    if probs:
        return probs
    sid, title, text = s["id"], s["title"], s["text"]
    if sid in seen_ids:
        probs.append("duplicate id")
    seen_ids.add(sid)
    tkey = title.strip().lower()
    if tkey in seen_titles:
        probs.append(f"duplicate title (also in {seen_titles[tkey]})")
    seen_titles.setdefault(tkey, sid)
    if "{" in title or "}" in title:
        probs.append("blank in title")

    blanks = BLANK.findall(text)
    bad = [b for b in blanks if b not in ALLOWED]
    if bad:
        probs.append(f"unknown blank types: {bad}")
    if text.count("{") != text.count("}") or text.count("{") != len(blanks):
        probs.append("unbalanced braces")
    n = len(blanks)
    if not 12 <= n <= 16:
        probs.append(f"{n} blanks (need 12-16)")
    pos = [b for b in blanks if b in POS]
    if len(pos) < 9:
        probs.append(f"only {len(pos)} part-of-speech blanks (need 9+)")
    if len(set(pos)) < 4:
        probs.append(f"only {len(set(pos))} part-of-speech types (need 4+)")
    extras = [b for b in blanks if b in EXTRAS]
    if len(extras) > 4:
        probs.append(f"{len(extras)} extra-type blanks (max 4)")

    words = len(BLANK.sub("", text).split())
    if not 100 <= words <= 165:
        probs.append(f"{words} words of fixed text (need 100-165)")
    if words / max(n, 1) > 12:
        probs.append(f"{words / max(n, 1):.1f} words per blank (max 12)")

    if re.search(r"\ban \{", text, re.I):
        probs.append("'an' before a blank (write 'a')")
    if re.search(r"\}(s|es|ed|ing|'s)\b", text):
        probs.append("suffix attached to a blank")
    # blank at the start of a sentence or paragraph
    if re.search(r'(^|[.!?]["”]?\s+|\n\s*)["“]?\{', text):
        probs.append("sentence starts with a blank")
    low = " " + text.lower() + " "
    hits = [w.strip() for w in BANNED if w in low]
    if hits:
        probs.append(f"check wording: {hits}")
    return probs


def main(paths):
    seen_ids, seen_titles = set(), {}
    total, bad_count = 0, 0
    for path in paths:
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception as e:
            print(f"{path}: cannot read JSON: {e}")
            bad_count += 1
            continue
        if not isinstance(data, list):
            print(f"{path}: top level must be a list")
            bad_count += 1
            continue
        for s in data:
            total += 1
            probs = check_story(s if isinstance(s, dict) else {}, seen_ids, seen_titles)
            if probs:
                bad_count += 1
                print(f"{path} :: {s.get('id', '?') if isinstance(s, dict) else '?'}")
                for p in probs:
                    print(f"   - {p}")
    print(f"\n{total} stories checked, {bad_count} with problems.")
    return 1 if bad_count else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
