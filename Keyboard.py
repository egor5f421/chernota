from aiogram import types
from aiogram.types import FSInputFile


async def hello_btn(callback: types.CallbackQuery):
    # 🫘 🐟
    await callback.message.answer_photo(photo=FSInputFile('Stickers/hello.gif'),
                                        caption="Привет '{name}'".format(name=callback.message.chat.first_name))
