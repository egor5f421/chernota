from aiogram import types, Router

router = Router()


@router.message()
async def msg(message: types.Message):
    try:
        print(message.text)
    except UnicodeEncodeError:
        print(message.content_type)
    if message.text.lower() == "не знаю":
        await message.answer("А ну говори, что не знаеш?")
        return
    elif message.text.isupper():
        await message.answer("Следи за капсом, а то покусаю, и тоже капсом писать буду!".upper())  # 🫘 🐟
        return

    await message.answer("Что ты хочешь сказать?")


@router.edited_message()
async def edited_msg(message: types.Message):
    await message.answer("Зачем изменил сообщение?")
