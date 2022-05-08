from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import pythonKeyboard

from loader import dp


@dp.message_handler(Command("menu"))
async def show_meny(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)
    await message.delete()

@dp.message_handler(Text('Telegram bot'))
async def send_link(message: Message):
    await message.answer("https://mohirdev.uz/courses/telegram/lesson/tugmalar-keyboards/")
    await message.delete()

@dp.message_handler(Text("Python"))
async def show_python(message: Message):
    await message.answer("▶Python kurslariga hush kelibsiz", reply_markup=pythonKeyboard)
    await message.delete()


@dp.message_handler(Text("1-dars"))
async def send_link(message: Message):
    await message.answer("https://mohirdev.uz/courses/python/lesson/00-darslarni-qanday-o%ca%bbzlashtiramiz/", reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler(Text("2-dars"))
async def send_link(message: Message):
    await message.answer("https://mohirdev.uz/courses/python/lesson/02-hello-world/", reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler(Text("3-dars"))
async def send_link(message: Message):
    await message.answer("https://mohirdev.uz/courses/python/lesson/03-print-sinteks-va-arifmetik-amallar/", reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler(Text("🔝Boshiga"))
async def start(message:Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)
    await message.delete()
