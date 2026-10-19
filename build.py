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
    # Standalone version for regular web hosting (GitHub Pages): full HTML document,
    # with the page's <title> moved into <head> so previews and bookmarks see it.
    title_tag = "<title>Giggle Blanks</title>"
    body = page.replace(title_tag + "\n", "", 1)
    standalone = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<link rel=\"icon\" type=\"image/svg+xml\" href=\"icon.svg\">\n"
        "<link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"favicon-32.png\">\n"
        "<link rel=\"apple-touch-icon\" href=\"apple-touch-icon.png\">\n"
        "<link rel=\"manifest\" href=\"manifest.json\">\n"
        "<meta name=\"theme-color\" content=\"#ffcb3d\">\n"
        "<meta name=\"apple-mobile-web-app-title\" content=\"Giggle Blanks\">\n"
        + title_tag + "\n"
        "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    )
    index = os.path.join(HERE, "index.html")
    with open(index, "w") as f:
        f.write(standalone)
    themes = len({s["theme"] for s in stories})
    print(f"Built {out} and {index}: {len(stories)} stories, {themes} themes, {len(page)//1024} KB")


if __name__ == "__main__":
    main()
