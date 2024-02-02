from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import _
from apiwca.wca_requests import get_wca_profile

from bot.database.requests import DB
from bot.database.models import User as UserMd
from bot.helpers import send_statistic, del_msg, check_events


router = Router()


@router.message(CommandStart())
async def greetings(message: Message):
    user_id = message.from_user.id
    user = await (await DB()).get(user_id)

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
        events = None
        try:
            events = check_events(message.text.split()[2:])
        except:
            pass
        
        await send_statistic(message, wca_id=wca_id, events=events)
    elif message.text.startswith('/set'):
        profile = await get_wca_profile(wca_id)

        if not profile:
            msg = await message.reply(_['wrong_wcaid'])
            await del_msg(msg)
            return await del_msg(message)
        
        user_id = message.from_user.id
        user = await (await DB()).get(user_id)
        
        if user:
            await (await DB()).update_wca_id(user_id, wca_id)
        else:
            user = UserMd(user_id=user_id, wca_id=wca_id)
            await (await DB()).create(user)
        
        await message.reply(_['register_wcaid'])


@router.message(Command('me', prefix='/'))
async def get_me(message: Message):
    events = None
    try:
        events = check_events(message.text.split()[1:])
    except:
        pass
    print('handler', events)

    user_id = message.from_user.id
    user = await (await DB()).get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id, events=events)
    else:
        msg = await message.reply(_['please_set_wcaid'])

        await del_msg(msg)
        await del_msg(message)