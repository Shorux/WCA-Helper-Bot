import asyncio
from aiogram.types import Message

from .strings import _, events_list
from bot.database.requests import Chats
from bot.database.models import async_session
from bot.filters.filters import is_group
from apiwca.wca_requests import parsed_wca_profile, get_wca_profile


async def send_statistic(message: Message, profile: dict = None,
                         wca_id: str = None, events: list = None) -> None:
    lang = await ln(message)

    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        msg = await message.reply(_.wrong_wcaid[lang])
        await del_msg(msg)
        return await del_msg(message)

    if events:
        events = check_events(events)

    time = 600
    photo_url = profile.get('photo_url')
    res_msg = parsed_wca_profile(lang, profile, events)

    if len(res_msg) > 1020:
        await del_msg(await message.reply_photo(photo=photo_url), time)
        asyncio.sleep(0.1)
        await del_msg(await message.answer(res_msg), time)
    else:
        await del_msg(await message.reply_photo(photo=photo_url, caption=res_msg), time)
    await del_msg(message, time)


async def del_msg(message: Message, time=120) -> None:
    try:
        if is_group(message):
            await asyncio.sleep(time)
            await message.delete()
    except:
        pass


async def ln(message: Message) -> str:
    chat_id = message.chat.id

    async with async_session() as session:
        db = Chats(session)
        lang = await db.get_lang(chat_id)

    return lang


def check_events(events: list) -> list:
    return [event for event in events if event in events_list]
