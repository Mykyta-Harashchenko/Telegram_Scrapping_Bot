import asyncio
import requests
import aiohttp
from bs4 import BeautifulSoup


async def search_user_query(query:str)->list[dict]:
    print("Start search_user_query")
    res = []
    search_url = f'https://hotline.ua/ua/sr/?q={query.replace(" ", "+")}'
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(search_url, ssl=False) as response:
            print("Status:", response.status)

            html = await response.text()
            bs = BeautifulSoup(html, "lxml")
            catalog = bs.find("div", attrs={'class': "search-list__body"})
            items = catalog.find_all("div", class_="list-item flex")
            for el in items:
                title = el.find("a", class_="item-title text-md link link--black").text.strip()
                img = f'https://hotline.ua/{el.find("img", class_="rounded-border--sm")["src"]}'
                price = el.find("div", class_="text-md text-orange text-lh--1").text.strip()
                compare = f'https://hotline.ua/{el.find("a", class_="btn btn--orange")["href"]}'
                item = {"title": title, "img": img, "price": price, "compare": compare}
                res.append(item)
    return res


async def get_weather(city):
    city = city.replace(' ', '+')
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        weather_info = soup.find('span', class_='phrase')

        if weather_info:
            return weather_info.text
        else:
            return "Інформацію про погоду не знайдено."
    else:
        return f"Не вдалося отримати сторінку. Статус код: {response.status_code}"


async def search_course_currency():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)

    if response.status_code == 200:
        currency_data = response.json()
        result = []
        for item in currency_data:
            currency = item['ccy']
            buy_rate = item['buy']
            sell_rate = item['sale']
            result.append({'currency': currency, 'buy_rate': buy_rate, 'sell_rate': sell_rate})
        return result
    else:
        print(f"Помилка завантаження сторінки: {response.status_code}")
        return []

if __name__=="__main__":
    print(asyncio.run(get_weather('Kyiv')))
