from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from dispatcher import bot
from bot.extra.strings import _
from bot.keyboards.keyboards import lang_kb
from bot.database.requests import User, Chat
from bot.database.models import async_session
from bot.filters.filters import is_private, is_admin
from bot.extra.helpers import send_statistic, del_msg, check_events, ln
from apiwca.wca_requests import get_wca_profile, parsed_users, search_users


router = Router()


@router.message(CommandStart())
async def greetings_handler(message: Message):
    user_id = message.from_user.id

    async with async_session() as session:
        db = User(session)
        user = await db.get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        await message.reply(_.please_set_wcaid[await ln(message)])


@router.message(Command(commands=['get', 'set']))
async def get_set_user_handler(message: Message):
    splited_msg = message.text.split()

    try:
        wca_id = splited_msg[1].upper()
    except:
        await del_msg(await message.reply(_.wrong_wcaid[await ln(message)]))
        return await del_msg(message)

    profile = await get_wca_profile(wca_id)

    if message.text.startswith('/set'):
        if profile:
            async with async_session() as session:
                db = User(session)
                await db.create(message.from_user.id, wca_id)

            time = 600
            msg = await message.reply(_.register_wcaid[await ln(message)])
        else:
            time = 120
            msg = await message.reply(_.wrong_wcaid[await ln(message)])

        await del_msg(msg, time)
        await del_msg(message, time)
    elif message.text.startswith('/get'):
        events = check_events(splited_msg[2:]) 

        await send_statistic(message, profile, events=events)


@router.message(Command('search'))
async def search_users_handler(message: Message):
    query = ' '.join(message.text.split()[1:])
    users = await search_users(query)
    lang = await ln(message)

    if users:
        time = 600
        resp = parsed_users(lang, users)
    else:
        time = 120
        resp = _.not_found[lang]
    
    await del_msg(await message.reply(resp), time)
    await del_msg(message, time)


@router.message(Command('me'))
async def get_me_handler(message: Message):
    events = check_events(message.text.split()[1:])
    user_id = message.from_user.id

    async with async_session() as session:
        db = User(session)
        user = await db.get(user_id)

    if user and user.wca_id:
        msg = await send_statistic(message, wca_id=user.wca_id, events=events)
        time = 600
    else:
        msg = await message.reply(_.please_set_wcaid[await ln(message)])
        time = 120

    await del_msg(message, time)
    await del_msg(msg, time)


@router.message(Command('lang'))
async def set_language(message: Message):
    if is_private(message) or await is_admin(message):
        await message.reply(_.choose_lang[await ln(message)], reply_markup=lang_kb)
    
    await del_msg(message, 1)


@router.callback_query(F.data.startswith('lang_'))
async def lang_callback(callback: CallbackQuery):
    
    lang = callback.data[-2:]
    message = callback.message

    async with async_session() as session:
        db = Chat(session)
        await db.create(message.chat.id, lang)

    await bot.delete_message(message.chat.id, message.message_id)
    await del_msg(await message.answer(_.lang_registred[lang]), 10)
