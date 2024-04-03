import asyncio
import logging

import aiogram

import Keyboard
import config
import events
from commands import *

sqlite.create_table()

logging.basicConfig(level=logging.INFO, format='%(name)s - %(message)s       level: %(levelname)s')

bot = aiogram.Bot(token=config.TOKEN)
dp = aiogram.Dispatcher()

# Commands
dp.include_router(router)

# Keyboard
dp.include_router(Keyboard.router)

# Events
dp.include_router(events.router)


async def main():
    #    dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
