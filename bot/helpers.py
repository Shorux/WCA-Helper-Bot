import asyncio
from aiogram.types import Message

from config import _, events_list
from .filters.filters import is_group
from .database.requests import chat_db
from apiwca.wca_requests import parsed_wca_profile, get_wca_profile


async def send_statistic(message: Message, profile: dict = None,
                         wca_id: str = None, events: list = None):
    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        msg = await message.reply(_.wrong_wcaid[await ln(message)])
        await del_msg(msg)
        await del_msg(message)
        return None
    print()
    lang = await ln(message)
    photo_url = profile.get('photo_url')
    data = parsed_wca_profile(lang, profile, events)
    res_msg = _.statistic[lang].format(**data)
    time = 600

    if len(res_msg) < 1024:
        msg = await message.reply_photo(photo=photo_url, caption=res_msg)
    else:
        msg = await message.reply_photo(photo=photo_url)
        await del_msg(await message.answer(res_msg), time)

    await del_msg(msg, time)
    await del_msg(message, time)


async def del_msg(message: Message, time=120):
    try:
        if is_group(message):
            await asyncio.sleep(time)
            await message.delete()
    except:
        pass


async def ln(message: Message) -> str:
    chat_id = message.chat.id
    db = await chat_db()
    lang = await db.get_lang(chat_id)

    return lang


def check_events(events: list):
    events = [event for event in events if event in events_list]
    return events
