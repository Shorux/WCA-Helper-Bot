from aiogram.types import Message

from dispatcher import bot


def is_group(message: Message | list[Message]):
    if isinstance(message, list):
        message = message[0]
    return message.chat.type == 'group' or message.chat.type == 'supergroup'


def is_private(message: Message):
    return message.chat.type == 'private'


async def is_admin(message: Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in ['administrator', 'creator']
