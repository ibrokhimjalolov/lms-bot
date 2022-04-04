from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import BoundFilter



class IsChatPrivate(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE



class IsChatGroup(BoundFilter):

    def check(self, message: Message) -> bool:
        return message.chat.type in [
            ChatType.GROUP,
            ChatType.SUPER_GROUP,
        ]



class IsChatChannel(BoundFilter):

    def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.CHANNEL

