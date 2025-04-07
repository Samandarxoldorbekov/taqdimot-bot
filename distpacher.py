import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, types ,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from taqdimot import taqdimot_gen
from profil import profel_as


dp = Dispatcher()
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="taqdimot yaratish"), KeyboardButton(text="Profil")],
        
    ],
    resize_keyboard=True  # Tugmalar ekran o‘lchamiga moslashadi
)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Asalomu alaykum kerkli bo'limni tanlang 👇", reply_markup=menu)

@dp.message(F.text == "taqdimot yaratish")
async def settings_handler(message: types.Message):
    await message.answer("taqdimot yaratishni boshlaymiz",reply_markup=taqdimot_gen())

@dp.message(F.text == "Profil")
async def settings_handler(message: types.Message):
    await message.answer("siz o'z profilingizdasiz",reply_markup=profel_as())



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token="7576626442:AAGgECnqZQ-l2hIO58fPqIyOUXA8DhWgIRc", default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())