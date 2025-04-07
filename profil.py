from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def profel_as():
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="taqdimot yaratish", callback_data="taqdimot_yaratish"),
             InlineKeyboardButton(text="Profil", callback_data="profil")],
            [InlineKeyboardButton(text="🔗 Referal", callback_data="referal")],
        ]
    )
    return menu
