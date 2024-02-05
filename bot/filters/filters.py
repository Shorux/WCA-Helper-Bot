from aiogram.types import Message
from aiogram.filters import Filter

from dispatcher import bot


def is_group(message: Message):
    return message.chat.type == 'group' or message.chat.type == 'supergroup'


def is_private(message: Message):
    print(message.chat.type)
    return message.chat.type == 'private'


async def is_admin(message: Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    print(member)
    return member.status == 'administrator'