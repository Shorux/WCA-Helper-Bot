from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import _
from bot.database.models import User
from bot.wca_requests import get_wca_profile
from bot.helpers import send_statistic, del_msg
from bot.database.requests import create_user, get_user, update_wca_id


router = Router()


@router.message(CommandStart())
async def greetings(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        msg = await message.reply(_['please_set_wcaid'])
        await del_msg(msg)
        return await del_msg(message)


@router.message(Command(commands=['get', 'set'], prefix='/'))
async def hello_handler(message: Message):
    try:
        wca_id = message.text.split()[1].upper()
    except:
        msg = await message.reply(_['wrong_wcaid'])
        await del_msg(msg)
        return await del_msg(message)

    if message.text.startswith('/get'):
        await send_statistic(message, wca_id=wca_id)
    elif message.text.startswith('/set'):
        profile = await get_wca_profile(wca_id)

        if not profile:
            msg = await message.reply(_['wrong_wcaid'])
            await del_msg(msg)
            return await del_msg(message)
        
        user_id = message.from_user.id
        user = await get_user(user_id)
        
        if user:
            await update_wca_id(user_id, wca_id)
        else:
            user = User(user_id=user_id, wca_id=wca_id)
            await create_user(user)
        
        await message.reply(_['register_wcaid'])


@router.message(Command('me', prefix='/'))
async def get_me(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        msg = await message.reply(_['please_set_wcaid'])

        await del_msg(msg)
        await del_msg(message)