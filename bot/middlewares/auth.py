from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware

from models.models import TelegramUser
from bot.states.auth import Auth


class AuthMiddleware(BaseMiddleware):
    """
    Auth middleware
    """

    def __init__(self):
        super(AuthMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        id = message.from_user.id
        full_name = message.from_user.full_name
        try:
            user = TelegramUser.objects.get(id=id)
            if user.full_name != full_name:
                user.full_name = full_name
                user.save(update_fields=['full_name'])
            is_new_user = False
        except Exception as e:
            print(e)
            user = TelegramUser.objects.create(
                id=id,
                full_name=full_name
            )
            is_new_user = True
        setattr(message, 'user', user)
        setattr(message.user, 'is_new_user', is_new_user)
