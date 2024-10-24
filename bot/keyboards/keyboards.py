from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='RU', callback_data='lang_ru'),
            InlineKeyboardButton(text='EN', callback_data='lang_en'),
            
        ],
        [
            InlineKeyboardButton(text='UZ', callback_data='lang_uz'),
            InlineKeyboardButton(text='KZ', callback_data='lang_kz'),
        ]
])
