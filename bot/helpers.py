import asyncio
from aiogram.types import Message

from config import _, events_list
from apiwca.wca_requests import parsed_wca_profile, get_wca_profile


def check_events(events: list):
    events = [event for event in events if event in events_list]
    return events


async def send_statistic(message: Message, profile: dict = None,
                         wca_id: str = None, events: list = None):
    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        msg = await message.reply(_['wrong_wcaid'])
        await del_msg(msg)
        return await del_msg(message)
        
    photo_url = profile.get('photo_url')
    data = parsed_wca_profile(profile, events)
    res_msg = _['statistic'].format(**data)

    if len(res_msg) < 1024:
        await message.reply_photo(photo=photo_url, caption=res_msg)
    else:
        await message.reply_photo(photo=photo_url)
        await message.answer(res_msg)

    return True

async def del_msg(message: Message, time=120):
    await asyncio.sleep(time)
    try:
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            await message.delete()
    except:
        pass
