from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from bot.database.models import User
from bot.database.requests import create_user, get_user, update_wca_id

from config import _
from bot.wca_requests import parsed_wca_profile, get_wca_profile


router = Router()


async def send_statistic(message: Message, profile: dict = None, wca_id: str = None):
    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        await message.reply(_['wrong_wcaid'])
        return None
        
    photo_url = profile.get('photo_url')
    data = await parsed_wca_profile(profile)
    res_msg = _['statistic'].format(**data)

    if len(res_msg) < 1024:
        await message.reply_photo(photo=photo_url, caption=res_msg)
    else:
        await message.reply_photo(photo=photo_url)
        await message.answer(res_msg)

    return True


@router.message(CommandStart())
async def greetings(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if user and user.wca_id:
        profile = await get_wca_profile(user.wca_id)
        await send_statistic(message, profile)
    else:
        await message.reply(_['please_set_wcaid'])


@router.message(Command(commands=['get', 'set'], prefix='/'))
async def hello_handler(message: Message):
    try:
        wca_id = message.text.split()[1].upper()
    except:
        return await message.reply(_['wrong_wcaid'])
    
    if message.text.startswith('/get'):
        await send_statistic(message, wca_id=wca_id)
    elif message.text.startswith('/set'):
        profile = await get_wca_profile(wca_id)

        if not profile:
            return await message.reply(_['wrong_wcaid'])
        
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
        await message.reply(_['please_set_wcaid'])