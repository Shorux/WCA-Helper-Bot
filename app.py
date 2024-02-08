import os
import logging
import asyncio

import config
from dispatcher import bot, dp
from bot.handlers.handlers import router
from bot.database.models import init_database


def start_logging():
    if config.DEBUG:
        logging.basicConfig(level=logging.DEBUG)
        return

    if not os.path.isdir('logs'):
        os.mkdir('logs')
    logging.basicConfig(
        filename=f'./logs/bot_{config.BOT_TOKEN.split(":")[0]}.log',
        level=logging.WARNING,
        format='~%(asctime)s %(message)s'
    )


async def main():
    dp.include_router(router)

    await init_database()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    start_logging()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
