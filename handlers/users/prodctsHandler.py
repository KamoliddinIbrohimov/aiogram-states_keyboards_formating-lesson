from aiogram import types
from aiogram.types import CallbackQuery
import logging
#from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.callback_data import course_callback, books_callback
from loader import dp
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard, algaritm_keyboard


@dp.message_handler(text="🛍Maxsulotlar")
async def sed_products(message: types.Message):
    await message.answer("Maxsulotni tanlang", reply_markup=categoryMenu)
    await message.delete()



@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)
    await call.message.delete()

@dp.callback_query_handler(text="books")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.answer(cache_time=60)
    await call.message.delete()


#CallbacackData yordamida filtirlaymiz
@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data : dict):
    #logging yordammida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Siz Mukammal telegram bot Kursini tanladinggiz!",
                              reply_markup=telegram_keyboard)
    await call.answer(cache_time=60)
    await call.message.delete()

@dp.callback_query_handler(course_callback.filter(item_name="algorithm"))
async def buying_course(call: CallbackQuery, callback_data : dict):
    #logging yordammida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Siz Malumotlar Tuzilmasi va Algaritmlash kursini tanladinggiz!",
                              reply_markup=algaritm_keyboard)
    await call.answer(cache_time=60)
    await call.message.delete()


@dp.callback_query_handler(books_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmanggiz qabul qilindi", cache_time=60, show_alert=True)

@dp.callback_query_handler(text="back")
async def back_button(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()
