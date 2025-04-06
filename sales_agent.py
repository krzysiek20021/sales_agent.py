import openai
import requests

# Klucze API
openai.api_key = 'TWÓJ_OPENAI_API_KEY'
news_api_key = 'TWÓJ_NEWS_API_KEY'

def get_latest_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={news_api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles[:5]  # Pobierz 5 najnowszych artykułów

def generate_sales_strategy(news_articles, product_info):
    context = "Oto najnowsze wiadomości związane z rynkiem:\n"
    for article in news_articles:
        context += f"- {article['title']}: {article['description']}\n"

    prompt = f"{context}\nBiorąc pod uwagę powyższe informacje oraz dane o produkcie: {product_info}, zaproponuj strategię sprzedaży."
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

# Przykładowe użycie
product_info = "Innowacyjny system CRM dla małych firm."
news_articles = get_latest_news("CRM dla małych firm")
strategy = generate_sales_strategy(news_articles, product_info)
print(strategy)
