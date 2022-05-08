from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python'),
            KeyboardButton(text='Telegram bot'),
        ],
    ],
    resize_keyboard=True
)

product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍Maxsulotlar"),
            KeyboardButton(text="ℹQo'llanma"),
        ],
    ],
    resize_keyboard=True
)