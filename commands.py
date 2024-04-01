from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Сказать", callback_data="hello"))

    await message.answer("Привет я паучок, меня зовут чернота. Как тебя зовут?",
                         reply_markup=keyboard.as_markup()
                         )
