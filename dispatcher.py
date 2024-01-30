import os

from aiogram import Bot, Dispatcher


bot = Bot(token=os.getenv('TOKEN'), parse_mode='MARKDOWN_V2')
dp = Dispatcher()
