from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .auth import AuthMiddleware

print(__name__)
if __name__ == "bot.middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(AuthMiddleware())
