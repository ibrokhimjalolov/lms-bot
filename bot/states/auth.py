from aiogram.dispatcher.filters.state import State, StatesGroup


class Auth(StatesGroup):
    set_login = State()
    login = State()
    set_password = State()
    password = State()
