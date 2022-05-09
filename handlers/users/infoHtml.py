from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("infohtml"))
async def bot_help(message: types.Message):
    text = f"Assalomu alekum {message.from_user.full_name}!\n"
    text += f"<b>Bu qalin matn</b>\n"
    text += f"<i>Bu egri matn</i>\n"
    text += f"<u>Bu ostki chiziq matn</u>\n"
    text += f"<s>Bu o'chirilgan matn</s>\n"
    text += f"<a href='#'>Bu sahifaga link</a>\n"
    text += f"Bu <code>print('Hello World')</code> kod"

    await message.answer(text)
