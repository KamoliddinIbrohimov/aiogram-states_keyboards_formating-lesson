from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

pythonKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-dars"),
            KeyboardButton(text="2-dars"),
            KeyboardButton(text="3-dars"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
            KeyboardButton(text="🔝Boshiga"),
        ],
    ],
    resize_keyboard=True
)