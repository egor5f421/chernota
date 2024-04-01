import logging

import asyncio

import aiogram
from aiogram.filters import Command

import Keyboard
import config
import events
from commands import *

logging.basicConfig(level=logging.INFO, format='%(name)s - %(message)s       level: %(levelname)s')

bot = aiogram.Bot(token=config.TOKEN)
dp = aiogram.Dispatcher()

# Commands
dp.message.register( cmd_start                 , Command("start")                   )

# Keyboard                                     ,                                    )
dp.callback_query.register( Keyboard.hello_btn , aiogram.F.data == "hello"          )

# Events                                       ,                                    )
dp.message.register( events.msg                ,                                    )
dp.edited_message.register( events.edited_msg  ,                                    )


async def main():
    #    dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())