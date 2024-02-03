import os
import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher

from bot.database.models import async_main
from bot.handlers import router


async def main():
    bot = Bot(token=os.getenv('TOKEN'), parse_mode='MARKDOWN')
    dp = Dispatcher()

    dp.include_router(router)

    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
