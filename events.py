from aiogram import types


async def msg(message: types.Message):
    print(message.text)
    if message.text.lower() == "не знаю":
        await message.answer("Что ты не знаеш?")
        return
    elif message.text.isupper():
        await message.answer("Следи за капсом, а то покусаю!")  # "🫘 и 🐟")
        return

    await message.answer("Что ты хочешь сказать?")  # "🫘 🐟")


async def edited_msg(message: types.Message):
    await message.answer("Зачем изменил сообщение?")
