from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback,books_callback
#1-Usul
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
#2-Usul
#Kurslar uchun Keyboard
coursesMenu = InlineKeyboardMarkup(row_width=2)
python = InlineKeyboardButton(text="🐍Python dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌎Django darslari", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

tg_bot = InlineKeyboardButton(text="🤖Telegram bot", callback_data="course:telegram")
coursesMenu.insert(tg_bot)

algorithm = InlineKeyboardButton(text="📈Malumotlar Tuzilmasi va Algaritmlash", callback_data="course:algorithm")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙Orqaga", callback_data="back")
coursesMenu.insert(back_button)

#3-Usul

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammmal Dasturlash. JavaScript": "js_book",
}


booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=books_callback.new(item_name=value)))
booksMenu.insert(back_button)

telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/"),
            InlineKeyboardButton(text="🔙Orqaga", callback_data="back")
        ],
    ])

algaritm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/"),
            InlineKeyboardButton(text="🔙Orqaga", callback_data="back")
        ],
    ])

