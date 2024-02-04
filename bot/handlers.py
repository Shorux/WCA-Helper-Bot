from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import _
from .database.requests import DB
from .helpers import send_statistic, del_msg, check_events
from apiwca.wca_requests import get_wca_profile, parsed_users, search_users


router = Router()


@router.message(CommandStart())
async def greetings_handler(message: Message):
    db = await DB()
    user_id = message.from_user.id
    user = await db.get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        await message.reply(_['please_set_wcaid'])


@router.message(Command(commands=['get', 'set']))
async def get_set_user_handler(message: Message):
    splited_msg = message.text.split()

    try:
        wca_id = splited_msg[1].upper()
    except:
        await del_msg(await message.reply(_['wrong_wcaid']))
        return await del_msg(message)

    profile = await get_wca_profile(wca_id)

    if message.text.startswith('/set'):
        if profile:
            db = await DB()
            await db.create(message.from_user.id, wca_id)

            time = 600
            msg = await message.reply(_['register_wcaid'])
        else:
            time = 120
            msg = await message.reply(_['wrong_wcaid'])

        await del_msg(msg, time)
        await del_msg(message, time)
    elif message.text.startswith('/get'):
        events = check_events(splited_msg[2:]) 

        await send_statistic(message, profile, events=events)


@router.message(Command('search'))
async def search_users_handler(message: Message):
    query = ' '.join(message.text.split()[1:])

    if query:
        users = await search_users(query)
        resp = parsed_users(users)

        time = 600
        msg = await message.reply(resp)
    else:
        time = 120
        msg = await message.reply(_['not_found'])
    
    await del_msg(message, time)
    await del_msg(msg, time)


@router.message(Command('me'))
async def get_me_handler(message: Message):
    events = check_events(message.text.split()[1:])
    user_id = message.from_user.id

    db = await DB()
    user = await db.get(user_id)

    if user and user.wca_id:
        msg = await send_statistic(message, wca_id=user.wca_id, events=events)
        time = 600
    else:
        msg = await message.reply(_['please_set_wcaid'])
        time = 120

    await del_msg(message, time)
    await del_msg(msg, time)
