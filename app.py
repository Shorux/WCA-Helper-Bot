import sys
import logging
import asyncio

from dispatcher import bot, dp
from bot.database.models import async_main
from bot.handlers import router


async def main():
    dp.include_router(router)

    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
