from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from bot.states.auth import Auth


@dp.message_handler(state=Auth.set_login)
async def set_login_handler(message: types.Message, state: FSMContext):
    await Auth.login.set()
    await message.answer("Enter login:")


@dp.message_handler(state=Auth.login, content_types=types.ContentTypes.TEXT)
async def login_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await Auth.password.set()
    await message.answer("Enter password:")


@dp.message_handler(state=Auth.login)
async def login_handler(message: types.Message, state: FSMContext):
    await message.answer("Enter login:")


@dp.message_handler(state=Auth.set_password)
async def set_password_handler(message: types.Message, state: FSMContext):
    await Auth.password.set()
    await message.answer("Enter password🙈:")


@dp.message_handler(state=Auth.password, content_types=types.ContentTypes.TEXT)
async def password_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        message.user.login = data.get('login', '')
        message.user.password = data.get('password', '')
        message.user.save(update_fields=['login', 'password'])
    await state.finish()
    await message.answer("Done✅")


@dp.message_handler(state=Auth.password)
async def password_handler(message: types.Message, state: FSMContext):
    await message.answer("Enter password🙈:")
