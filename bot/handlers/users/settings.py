from aiogram import types

from loader import dp
from bot.keyboards.default.main import SETTING_TEXT
from bot.filters import IsChatPrivate
from bot.keyboards.default.settings import CHANGE_LOGIN_TEXT, CHANGE_PASSWORD_TEXT, btn
from bot.states.settings import Settings
from bot.keyboards.default import main 

@dp.message_handler(IsChatPrivate(), text=SETTING_TEXT)
async def settings_handler(message: types.Message):
    await message.answer(
        "Choose one option.👇",
        reply_markup=btn
    )


@dp.message_handler(IsChatPrivate(), text=CHANGE_LOGIN_TEXT)
async def login_settings_handler(message: types.Message):
    await Settings.login.set()
    await message.answer(
        "Enter login:"
    )


@dp.message_handler(IsChatPrivate(), state=Settings.login)
async def set_login_settings_handler(message: types.Message, state):
    login = message.text
    message.user.login = login
    message.user.save(update_fields=['login'])
    await state.finish()
    await message.answer(
        "Done✅",
        reply_markup=main.btn
    )


@dp.message_handler(IsChatPrivate(), text=CHANGE_PASSWORD_TEXT)
async def password_settings_handler(message: types.Message):
    await Settings.pasaword.set()
    await message.answer(
        "Enter password:"
    )


@dp.message_handler(IsChatPrivate(), state=Settings.pasaword)
async def set_password_settings_handler(message: types.Message, state):
    password = message.text
    message.user.password = password
    message.user.save(update_fields=['password'])
    await state.finish()
    await message.answer(
        "Done✅",
        reply_markup=main.btn
    )
