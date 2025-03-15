import requests
import json
from config import NEWS_API_KEY, NEWS_API_URL

def fetch_news(topic):
    """Fetch news articles related to the given topic."""
    params = {
        "q": topic,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }
    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [{"title": a["title"], "content": a.get("content", ""), "url": a["url"]} for a in articles]
    else:
        print(f"Error fetching news: {response.status_code}, {response.text}")
        return []
