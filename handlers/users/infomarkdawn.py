from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("infomarkdawn"))
async def bot_help(message: types.Message):
    text = f"Assalomu alekum {message.from_user.full_name}\!\n"
    text += f"*Bu qalin matn*\n"
    text += f"_Bu egri matn_\n"
    text += f"__Bu ostki chiziq matn__\n"
    text += f"~Bu o'chirilgan matn~\n"
    text += f"[Bu sahifaga link](#)\n"
    text += f"Bu `print('Hello World')` kod"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)
