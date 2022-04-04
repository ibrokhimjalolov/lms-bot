import logging

from bot.data.config import DEVELOPERS, ADMINS

from loader import dp


async def message2admins(text):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logging.exception(err)


async def message2developers(text):
    for dev in DEVELOPERS:
        try:
            await dp.bot.send_message(dev, text)
        except Exception as err:
            logging.exception(err)
