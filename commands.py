from aiogram import types


async def cmd_start(message: types.Message):
    await message.answer("Привет я паучок, меня зовут чернота. Как тебя зовут?")
