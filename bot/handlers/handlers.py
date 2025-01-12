from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from dispatcher import bot
from bot.extra.strings import _
from bot.keyboards.keyboards import lang_kb
from bot.database.models import async_session
from bot.database.requests import Users, Chats
from bot.filters.filters import is_private, is_admin
from bot.extra.helpers import send_statistic, del_msg, ln, handle_set_command
from apiwca.wca_requests import get_wca_profile, parsed_users, search_users


router = Router()


@router.message(CommandStart())
async def greetings_handler(message: Message):
    user_id = message.from_user.id

    async with async_session() as session:
        db = Users(session)
        user = await db.get(user_id)

    if user and user.wca_id:
        await send_statistic(message, wca_id=user.wca_id)
    else:
        await message.reply(_.please_set_wcaid[await ln(message)])


@router.message(Command(commands=['get', 'set']))
async def get_set_user_handler(message: Message):
    lang = await ln(message)
    split_msg = message.text.split()

    try:
        wca_id = split_msg[1].upper()
        profile = await get_wca_profile(wca_id)
    except:
        await del_msg(await message.reply(_.wrong_wcaid[lang]))
        return await del_msg(message)


    if message.text.startswith('/set'):
        msg = await handle_set_command(message, wca_id, profile, lang)

        await del_msg(await message.reply(msg), 600 if profile else 120)
    elif message.text.startswith('/get'):
        await send_statistic(message, profile, events=message.text.split()[2:], lang=lang)


@router.message(Command(commands=['search', 'qidirish']))
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


@router.message(Command(commands=['me', 'men']))
async def get_me_handler(message: Message):
    async with async_session() as session:
        db = Users(session)
        user = await db.get(message.from_user.id)

    if user and user.wca_id:
        msg = await send_statistic(message, wca_id=user.wca_id, events=message.text.split()[1:])
        time = 600
    else:
        msg = await message.reply(_.please_set_wcaid[await ln(message)])
        time = 120

    await del_msg([msg, message], time)


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
        db = Chats(session)
        await db.create(message.chat.id, lang)

    await bot.delete_message(message.chat.id, message.message_id)
    await del_msg(await message.answer(_.lang_registred[lang]), 10)
