from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


async def get_start_kb() -> KeyboardButton:
    return KeyboardButton(text="Пошук товарів Hotline")  # Повертаємо кнопку

async def get_currency_rate_kb() -> KeyboardButton:
    return KeyboardButton(text="Курс Валют")  # Повертаємо кнопку



async def get_compare_button(button_url: str):
    buttons = [[InlineKeyboardButton(text="Порівняти ціни", web_app=WebAppInfo(url=button_url))]]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


async def get_api_link_button(url='https://privatbank.ua/rates-archive'):
    button = InlineKeyboardButton(text="Перейти до приватбанку", url=url)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard

async def get_weather_button() -> KeyboardButton:
    return KeyboardButton(text="Погода")


async def get_weather_link_button(city: str) -> InlineKeyboardMarkup:
    url = f'https://www.weather-forecast.com/locations/{city.replace(" ", "-")}/forecasts/latest'
    button = InlineKeyboardButton(text="Перейти до сайту", url=url)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard

async def about_bot_button() -> KeyboardButton:
    return KeyboardButton(text="Про бота")
