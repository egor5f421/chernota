from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import sqlite

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='Оформить премиум', callback_data='get_premium')]
    ])

    await message.answer('Привет я паучок, '
                         'меня зовут чернота.'   '\n\n'
                         'Чтобы получить больше функций нажми кнопку ↓', reply_markup=kb.as_markup())

    sqlite.add_user(message.chat.id, message.chat.username)
