import requests

def get_weather_by_city(city_name, api_key=''):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&APPID={api_key}&mode=json'
    r = requests.get(url)
    content = r.json()
    print(content)

get_weather_by_city('Matara')