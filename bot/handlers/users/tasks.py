from aiogram import types

from loader import dp
from services.lms.tasks import get_formated_text
from bot.keyboards.inline.course import course_callback
from models.models import TelegramUser


@dp.callback_query_handler(course_callback.filter())
async def task_handler(call: types.CallbackQuery, callback_data: dict):
    message = call.message
    setattr(message, 'text', callback_data.get('id'))
    id = call.from_user.id
    full_name = call.from_user.full_name
    try:
        user = TelegramUser.objects.get(id=id)
        if user.full_name != full_name:
            user.full_name = full_name
            user.save(update_fields=['full_name'])
        is_new_user = False
    except Exception:
        user = TelegramUser.objects.create(
            id=id,
            full_name=full_name
        )
        is_new_user = True
    setattr(message, 'user', user)
    setattr(message.user, 'is_new_user', is_new_user)
    text = await get_formated_text(message)
    if not isinstance(text, list):
        text = [text]
    for m in text:
        await message.answer(m)
    await call.answer(cache_time=60)
