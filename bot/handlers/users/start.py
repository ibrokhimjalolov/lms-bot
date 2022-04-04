from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from bot.states.auth import Auth
from bot.keyboards.default.main import btn


@dp.message_handler(CommandStart())
async def start_handler(message: types.Message):
    if not message.user.login:
        await Auth.login.set()
        await message.answer(f"Hi👋, {message.from_user.full_name}!")
        await message.answer("Enter login:")
        return
    if not message.user.password:
        await Auth.password.set()
        await message.answer(f"Hi👋, {message.from_user.full_name}!")
        await message.answer("Enter password:")
        return
   
    await message.answer(f"Hi👋, {message.from_user.full_name}!", reply_markup=btn)
