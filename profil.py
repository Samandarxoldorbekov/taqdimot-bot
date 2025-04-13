from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def profel_as():
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Tarix", callback_data="tarix"),
             InlineKeyboardButton(text="balance", callback_data="balancs")],
            [InlineKeyboardButton(text="🔗 Referal", callback_data="referal")],
        ]
    )
    return menu
