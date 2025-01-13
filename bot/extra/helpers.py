import asyncio
from aiogram.types import Message, InputMediaPhoto

from .strings import _, events_list
from bot.database.requests import Chats, Users
from bot.database.models import async_session
from bot.filters.filters import is_group
from apiwca.wca_requests import parsed_wca_profile, get_wca_profile


async def send_statistic(message: Message, profile: dict = None,
                         wca_id: str = None, events: list = None, lang: str = None) -> None:
    lang = lang if lang else await ln(message)

    if wca_id:
        profile = await get_wca_profile(wca_id)

    if not profile:
        msg = await message.reply(_.wrong_wcaid[lang])
        return await del_msg([msg, message])

    if events:
        events = check_events(events)

    time = 600
    trash = []
    photo_url = profile.get('photo_url')
    media_msg = [
        InputMediaPhoto(media=photo_url)
    ]
    res_msg = parsed_wca_profile(lang, profile, events)

    if len(res_msg) > 1020:
        trash.append(await message.reply_media_group(media=media_msg))
        trash.append(await message.answer(res_msg))
    else:
        trash.append(await message.reply_photo(photo=photo_url, caption=res_msg))

    await del_msg(trash, time)


async def handle_set_command(message: Message, wca_id: str, profile: dict, lang: str) -> str:
    if profile:
        async with async_session() as session:
            db = Users(session)
            await db.create(message.from_user.id, wca_id)

        return _.register_wcaid[lang]
    return _.wrong_wcaid[lang]


async def del_msg(message: Message | list[Message] | None, time=120) -> None:
    try:
        if is_group(message):
            await asyncio.sleep(time)

            if isinstance(message, list):
                await asyncio.wait([msg.delete() for msg in message])
            else:
                await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")


async def ln(message: Message) -> str:
    chat_id = message.chat.id

    async with async_session() as session:
        db = Chats(session)
        lang = await db.get_lang(chat_id)

    return lang


def check_events(events: list) -> list:
    return [event for event in events if event in events_list]
