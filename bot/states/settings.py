from aiogram.dispatcher.filters.state import State, StatesGroup


class Settings(StatesGroup):
    login = State()
    pasaword = State()
