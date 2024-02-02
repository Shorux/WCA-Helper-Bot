from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import _
from apiwca.wca_requests import get_wca_profile, parsed_users, search_users

from .database.requests import DB
from .database.models import User as UserMd
from .helpers import send_statistic, del_msg, check_events


router = Router()


@router.message(CommandStart())
async def greetings_handler(message: Message):
    db = await DB()
    user_id = message.from_user.id
    user = await db.get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        msg = await message.reply(_['please_set_wcaid'])
        await del_msg(msg)
        return await del_msg(message)


@router.message(Command(commands=['get', 'set']))
async def get_set_user_handler(message: Message):
    db = await DB()

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
        user = await db.get(user_id)
        
        if user:
            await db.update_wca_id(user_id, wca_id)
        else:
            user = UserMd(user_id=user_id, wca_id=wca_id)
            await db.create(user)
        
        await message.reply(_['register_wcaid'])


@router.message(Command('search'))
async def search_users_handler(message: Message):
    try:
        query = ' '.join(message.text.split()[1:])

        if query:
            users = await search_users(query)
            resp = parsed_users(users)
            await message.reply(resp)
        else:
            await del_msg(await message.reply(_['not_found']))
    except:
        pass


@router.message(Command('me'))
async def get_me_handler(message: Message):
    db = await DB()

    events = None
    try:
        events = check_events(message.text.split()[1:])
    except:
        pass
    print('handler', events)

    user_id = message.from_user.id
    user = await db.get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id, events=events)
    else:
        msg = await message.reply(_['please_set_wcaid'])

        await del_msg(msg)
        await del_msg(message)
