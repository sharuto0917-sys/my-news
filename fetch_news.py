import feedparser
import json

feeds = {
    "日本": "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja",
    "国際": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=ja&gl=JP&ceid=JP:ja",
    "AI・IT": "https://news.google.com/rss/search?q=AI+OR+IT&hl=ja&gl=JP&ceid=JP:ja",
    "教育": "https://news.google.com/rss/search?q=教育&hl=ja&gl=JP&ceid=JP:ja",
    "音楽": "https://news.google.com/rss/search?q=音楽&hl=ja&gl=JP&ceid=JP:ja"
}

news = {}

for category, url in feeds.items():
    feed = feedparser.parse(url)

    news[category] = []

    for entry in feed.entries[:5]:
        news[category].append({
            "title": entry.title,
            "url": entry.link
        })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("ニュースを取得しました！")

git add news.json
git diff --cached ...
git push