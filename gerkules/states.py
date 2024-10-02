from aiogram.fsm.state import StatesGroup, State


class FormHotline(StatesGroup):
    title = State()

class FormWeather(StatesGroup):
    title = State()
