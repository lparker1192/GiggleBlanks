"""Combine stories/*.json into the app page.

Usage: python3 build.py
Reads app.template.html and every stories/*.json, writes giggle-blanks.html.
(giggle-blanks.html is a generated build file; the story files are never changed.)
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["space", "robots", "superheroes", "pirates", "under-the-sea", "beach-day",
         "dinosaurs", "jungle-adventure", "at-the-zoo", "school-days", "field-trip",
         "sports-day", "birthday-party", "snow-day", "halloween-fun", "camping-trip",
         "on-the-farm", "wild-weather", "castles-and-kingdoms", "friendly-dragons",
         "friendly-monsters", "in-the-kitchen", "pets", "grocery-store", "road-trip",
         "bedtime", "construction-site"]


def main():
    files = glob.glob(os.path.join(HERE, "stories", "*.json"))
    rank = {name: i for i, name in enumerate(ORDER)}
    files.sort(key=lambda p: rank.get(os.path.basename(p)[:-5], 999))
    stories = []
    for path in files:
        with open(path) as f:
            for s in json.load(f):
                stories.append({k: s[k] for k in ("id", "theme", "title", "text")})
    with open(os.path.join(HERE, "app.template.html")) as f:
        page = f.read()
    marker = "/*STORIES*/[]"
    assert marker in page, "story marker missing from template"
    data = json.dumps(stories, ensure_ascii=False).replace("</", "<\\/")
    page = page.replace(marker, data)
    out = os.path.join(HERE, "giggle-blanks.html")
    with open(out, "w") as f:
        f.write(page)
    themes = len({s["theme"] for s in stories})
    print(f"Built {out}: {len(stories)} stories, {themes} themes, {len(page)//1024} KB")


if __name__ == "__main__":
    main()
