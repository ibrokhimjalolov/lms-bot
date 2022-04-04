from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ATTENDANCES_TEXT = "Attendances❌"
MY_COURSES_ICON = "💼"
MY_COURSES_TEXT = MY_COURSES_ICON + "Courses"
DAILY_SCHEDULE = "📅Daily schedule"
WEEKLY_SCHEDULE = "🗓Weekly schedule"
SETTING_TEXT = "⚙️Setting"


btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ATTENDANCES_TEXT),
            KeyboardButton(text=MY_COURSES_TEXT),
        ],
        [
            KeyboardButton(text=DAILY_SCHEDULE),
            KeyboardButton(text=WEEKLY_SCHEDULE),
        ],
        [
            KeyboardButton(text=SETTING_TEXT),
        ]
    ],
    resize_keyboard=True
)
