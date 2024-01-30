from aiogram import Bot, Dispatcher

from config import TOKEN


bot = Bot(token=TOKEN, parse_mode='MARKDOWN_V2')
dp = Dispatcher()
