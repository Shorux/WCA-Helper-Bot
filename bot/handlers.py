from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from bot.database.models import User
from bot.database.requests import create_user, get_user, update_wca_id

from config import _s
from bot.wca_requests import parsed_wca_profile, get_wca_profile


router = Router()


@router.message(CommandStart())
async def greetings(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        res_msg = _s['statistic'].format(**(await parsed_wca_profile(user.wca_id)))
    else:
        res_msg = _s['please_set_wcaid']

    await message.reply(res_msg)


@router.message(Command('set', prefix='/!'))
async def hello_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    wca_id = message.text.split([1])

    if user:
        await update_wca_id(user_id, wca_id)
    else:
        user = User(user_id=user_id, wca_id=wca_id)
        await create_user(user_id, )
