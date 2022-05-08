from aiogram import types
from aiogram.types import CallbackQuery
import logging
#from aiogram.types import ReplyKeyboardRemove

from loader import dp
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu

@dp.message_handler(text="🛍Maxsulotlar")
async def sed_products(message: types.Message):
    await message.reply("Maxsulotni tanlang", reply_markup=categoryMenu)



@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)