from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

CHANGE_LOGIN_TEXT = "Change login"
CHANGE_PASSWORD_TEXT = "Change login"


btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CHANGE_LOGIN_TEXT),
            KeyboardButton(text=CHANGE_PASSWORD_TEXT),
        ],
    ],
    resize_keyboard=True
)
