from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq isminggizni kiriting")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text.title()

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzilinggizni kiriting")
    await PersonalData.next()
    #await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_fullname(message: types.Message, state:FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqaminggizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_fullname(message: types.Message, state:FSMContext):
    try:
        phone = int(message.text)

        await state.update_data(
            {"phone": phone}
        )
    except:
        await message.answer("iltimos malumotni to'g'ri kiriting")

    await state.update_data(
        {"phone": phone}
    )

    #Malumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidagi malumotlar qabul qilindi:\n"
    msg += f"Isminggiz - {name}\n"
    msg += f"Emailinggiz - {email}\n"
    msg += f"Telefon: {phone}"
    await message.answer(msg)
    await state.finish()
    #await state.reset_state(with_data=False)
