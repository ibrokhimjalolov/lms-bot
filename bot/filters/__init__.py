from loader import dp

from .admin import IsAdmin
from .chat_type import (
    IsChatPrivate,
    IsChatGroup,
    IsChatChannel
)



if __name__ == "bot.filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsChatPrivate)
    dp.filters_factory.bind(IsChatGroup)
    dp.filters_factory.bind(IsChatChannel)
