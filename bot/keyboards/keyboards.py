from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='RU', callback_data='ru'),
            InlineKeyboardButton(text='EN', callback_data='en'),
            InlineKeyboardButton(text='UZ', callback_data='uz')
        ]
])