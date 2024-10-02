import asyncio
import logging
import sys

import mongoengine
from aiogram import Bot, Dispatcher, html, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup
from googletrans import Translator

from keyboards import (get_start_kb,
                       get_compare_button,
                       get_currency_rate_kb,
                       get_api_link_button,
                       get_weather_button,
                       get_weather_link_button,
                       about_bot_button)
from parsers import search_user_query, search_course_currency, get_weather
from config.config import config
from DB.crud import save_user, get_all_users
from states import FormHotline, FormWeather
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

TOKEN = config.get("BOT_TOKEN")

translator = Translator()
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def get_combined_kb() -> ReplyKeyboardMarkup:
    # Отримуємо список кнопок з двох функцій
    start_button = await get_start_kb()
    currency_button = await get_currency_rate_kb()
    weather_button = await get_weather_button()
    about_button = await about_bot_button()

    # Створюємо клавіатуру з двома кнопками в одному ряді
    kb = ReplyKeyboardMarkup(
        keyboard=[[start_button, currency_button, weather_button, about_button]],  # Додаємо кнопки в один ряд
        resize_keyboard=True
    )

    return kb


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    try:
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await get_combined_kb())
        data = {'chat_id': message.from_user.id, 'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name, 'language': message.from_user.language_code}
        await save_user(data)
    except mongoengine.errors.NotUniqueError:
        print('Такий користувач вже існує')



@dp.message(F.text == 'Пошук товарів Hotline')
async def search_handler(message: Message, state: FSMContext) -> None:
    await message.answer('Введіть назву товара:')
    await state.set_state(FormHotline.title)

@dp.message(FormHotline.title)
async def process_title(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.clear()
    products = await search_user_query(message.text)
    for product in products:
        caption = f'{product.get("title")}\n{product.get("price")}'
        await bot.send_photo(chat_id=message.from_user.id, photo=product.get('img'), caption=caption,
                             reply_markup=await get_compare_button(product.get("compare")))


@dp.message(F.text == 'Про бота')
async def bot_info_handler(message: Message, state: FSMContext) -> None:
    url_to_chat = 'https://t.me/rdhtchllppr'
    await message.answer(f'Цей бот був створений, щоб продемонструвати мої навички у скрапінгу. '
                         f'Тут була використана технологія aiogram, база даних типу JSON під назвою MongoDB, та бібліотека Google Translator для перекладу даних з парсингу. '
                         f'Я буду дуже вдячний отримати ваші відгуки на рахунок свого бота в приватних повідомленнях {url_to_chat}')
@dp.message(F.text == 'Погода')
async def weather_handler(message: Message, state: FSMContext) -> None:
    await message.answer('Введіть назву міста англійською:')
    await state.set_state(FormWeather.title)


@dp.message(FormWeather.title)
async def weather_process_title(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.clear()
    products = await get_weather(message.text)
    translated_products = translator.translate(products, src='en', dest='uk').text
    await message.answer(translated_products, reply_markup=await get_weather_link_button(message.text))



@dp.message(F.text == 'Курс Валют')
async def currency_course(message: Message, state: FSMContext) -> None:
    course_info = await search_course_currency()
    if course_info:
        formatted_info = "\n".join([f"{item['currency']}: Купівля - {item['buy_rate']}, Продаж - {item['sell_rate']}" for item in course_info])
        await message.answer(f"Курс валют:\n{formatted_info}", reply_markup=await get_api_link_button())
    else:
        await message.answer("Не вдалося отримати курс валют.")

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    async with bot:
        users = await get_all_users()

        # Виберіть конкретний chat_id, наприклад, перший з користувачів
        if users:
            chat_id = users[0]['chat_id']  # або вкажіть конкретний chat_id
            try:
                logging.info(f"Відправка повідомлення користувачу {chat_id}")
                await bot.send_message(chat_id=chat_id, text="Привіт, це тестове повідомлення!")  # Додайте текст повідомлення
            except TelegramForbiddenError:
                logging.warning(f"Бот заблокований користувачем {chat_id}.")
            except Exception as e:
                logging.error(f"Інша помилка: {e}")

        await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
