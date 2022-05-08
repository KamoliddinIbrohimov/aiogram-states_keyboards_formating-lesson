from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books" )
        ],
        [
            InlineKeyboardButton(text="⛓Sahifaga o'tish", url="https://github.com/KamoliddinIbrohimov"),
        ],
        [
            InlineKeyboardButton(text="🔎Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="📤Ulashish", switch_inline_query="Botimizga marhamat"),
        ],
    ])

#Kurslar uchun Keyboard
coursesMenu = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(text="🐍Python dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)