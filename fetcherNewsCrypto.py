import requests

def fetch_crypto_news(crypto):
    url = f'https://newsapi.org/v2/everything?q={crypto}&apiKey=YOUR_NEWSAPI_KEY'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles

if __name__ == "__main__":
    crypto_name = input("Enter the cryptocurrency (e.g., bitcoin): ")
    news_articles = fetch_crypto_news(crypto_name)

    print(f"Latest news articles about {crypto_name.capitalize()}:")
    for article in news_articles:
        print(f"- {article['title']} (Source: {article['source']['name']})")
