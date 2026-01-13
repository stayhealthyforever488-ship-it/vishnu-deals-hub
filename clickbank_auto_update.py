import feedparser, json, datetime

AFFILIATE_ID = "vishnuar"
RSS_FEEDS = {
    "Health & Fitness": "https://feeds.clickbank.net/rss.xml?cat=Health%20%26%20Fitness",
    "E-Business": "https://feeds.clickbank.net/rss.xml?cat=E-Business%20%26%20E-Marketing",
    "Self Help": "https://feeds.clickbank.net/rss.xml?cat=Self-Help"
}

def fetch_products():
    all_products = []
    for category, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:300]:  # limit for faster loading
            product = {
                "title": entry.title,
                "description": entry.summary[:150] + "...",
                "category": category,
                "link": f"https://{AFFILIATE_ID}.hop.clickbank.net/?cbpage={entry.link}",
                "updated": datetime.datetime.utcnow().isoformat()
            }
            all_products.append(product)
    return all_products

def save_to_file(products):
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    products = fetch_products()
    save_to_file(products)
    print(f"✅ Saved {len(products)} products to products.json")
