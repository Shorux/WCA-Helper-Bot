import asyncio
from aiogram.types import Message

from config import _, events_list
from apiwca.wca_requests import parsed_wca_profile, get_wca_profile


async def send_statistic(message: Message, profile: dict = None,
                         wca_id: str = None, events: list = None):
    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        msg = await message.reply(_['wrong_wcaid'])
        await del_msg(msg)
        await del_msg(message)
        return False
    
    photo_url = profile.get('photo_url')
    data = parsed_wca_profile(profile, events)
    res_msg = _['statistic'].format(**data)
    time = 600

    if len(res_msg) < 1024:
        msg = await message.reply_photo(photo=photo_url, caption=res_msg)
    else:
        msg = await message.reply_photo(photo=photo_url)
        await del_msg(await message.answer(res_msg), time)

    await del_msg(msg, time)
    await del_msg(message, time)
    return True


async def del_msg(message: Message, time=120):
    await asyncio.sleep(time)
    try:
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            await message.delete()
    except:
        pass


def check_events(events: list):
    events = [event for event in events if event in events_list]
    return events
