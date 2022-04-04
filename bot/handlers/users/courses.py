from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp
from services.lms.my_courses import get_formated_text, parse
from bot.keyboards.default.main import ATTENDANCES_TEXT, MY_COURSES_TEXT, MY_COURSES_ICON
from bot.filters import IsChatPrivate
from bot.keyboards.inline.course import course_callback


@dp.message_handler(IsChatPrivate(), text=ATTENDANCES_TEXT)
async def attendances_handler(message: types.Message):
    await message.answer(
        await get_formated_text(message)
    )


@dp.message_handler(IsChatPrivate(), text=MY_COURSES_TEXT)
async def my_courses_handler(message: types.Message):
	buttons = InlineKeyboardMarkup(row_width=2)
	data = await parse(message)
	for course in data.get('courses', []):
		text = MY_COURSES_ICON+course['subject']
		callback_data=course_callback.new(id=str(course['id']))
		buttons.add(InlineKeyboardButton(
			text=text,
			callback_data=callback_data
		))
	await message.answer(
			f"Semester: <b>{data['semester']['name']}</b>",
			reply_markup=buttons
    )
