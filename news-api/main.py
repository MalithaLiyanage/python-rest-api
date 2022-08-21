import requests

def get_news(topic, from_date, to_date, language='en', api_key=''):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

def get_news_by_country(country='lk', api_key=''):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2022-7-27', to_date='2022-8-27'))
print(get_news_by_country(country='us'))