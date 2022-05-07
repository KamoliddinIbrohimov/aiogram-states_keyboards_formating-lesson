from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import PersonalData
from loader import dp

#
# @dp.message_handler(CommandHelp(), state=PersonalData.fullname)
# async def bot_help(message: types.Message):
#     await message.answer("Ism va familyanggizni kiriting!")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
