from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from bot.database.models import User
from bot.database.requests import create_user, get_user, update_wca_id

from config import _
from bot.wca_requests import parsed_wca_profile, get_wca_profile


router = Router()


@router.message(CommandStart())
async def greetings(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        data = await parsed_wca_profile(user.wca_id)
        res_msg = _['statistic'].format(**data)
    else:
        res_msg = _['please_set_wcaid']

    await message.reply(res_msg)


@router.message(Command('set', prefix='/!'))
async def hello_handler(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    wca_id = message.text.split()[1]
    if not (await get_wca_profile(wca_id)):
        return await message.reply(_['wrong_wcaid'])
    
    if user:
        await update_wca_id(user_id, wca_id)
    else:
        user = User(user_id=user_id, wca_id=wca_id)
        await create_user(user)
    
    await message.reply(_['register_wcaid'])


@router.message(Command('me', prefix='/!'))
async def get_me(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        data = await parsed_wca_profile(user.wca_id)
        res_msg = _['statistic'].format(**data)
    else:
        res_msg = _['please_set_wcaid']

    await message.reply(res_msg)
