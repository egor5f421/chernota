import sqlite

import aiogram
from aiogram import types, Router

router = Router()


@router.callback_query(aiogram.F.data == "get_premium")
async def get_premium(callback: types.CallbackQuery):
    await callback.message.answer('Держи')
    sqlite.set_premium(callback.message.chat.id, True)
    await callback.answer('')
