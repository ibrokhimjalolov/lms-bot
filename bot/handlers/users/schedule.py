from aiogram import types

from loader import dp
from services.lms.schedule import get_formated_text
from bot.keyboards.inline.course import course_callback
from models.models import TelegramUser
from bot.keyboards.default.main import DAILY_SCHEDULE, WEEKLY_SCHEDULE


@dp.message_handler(text=DAILY_SCHEDULE)
async def daily_schedule(message: types.Message):
    text = await get_formated_text(message)
    if not isinstance(text, list):
        text = [text]
    text = '\n'.join(text)
    await message.answer(
        text
    )


@dp.message_handler(text=WEEKLY_SCHEDULE)
async def weekly_schedule(message: types.Message):
    pass