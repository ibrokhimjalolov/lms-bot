from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("send <code>/start</code>",)
    await message.answer("\n".join(text))


@dp.message_handler()
async def bot_help(message: types.Message):
    text = ("send <code>/start</code>",)
    await message.answer("\n".join(text))


@dp.message_handler(state='*')
async def bot_help(message: types.Message, state):
    await state.finish()
    text = ("send <code>/start</code>",)
    await message.answer("\n".join(text))
