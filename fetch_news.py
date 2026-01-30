import feedparser
import json
import os

USED_FILE = "data/used_news.json"

def load_used():
    if os.path.exists(USED_FILE):
        with open(USED_FILE, "r") as f:
            return json.load(f)
    return []

def save_used(data):
    with open(USED_FILE, "w") as f:
        json.dump(data, f)

def get_news():
    feed = feedparser.parse(
        "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    )
    used = load_used()

    for entry in feed.entries:
        title = entry.title
        if title not in used:
            used.append(title)
            save_used(used)
            return title

    return None
