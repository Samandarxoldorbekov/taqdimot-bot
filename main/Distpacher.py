import asyncio
import logging
import sys 
from os import getenv
#aiogram
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton ,Message
from aiogram.filters import CommandStart



dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="taqdimot yaratish"), KeyboardButton(text="Qo'shimcha hizmatlar")], 
        [KeyboardButton(text="Abturentlar uchun"), KeyboardButton(text="Profel")], 
        
    ],
    resize_keyboard=True  # Tugmalar ekran o‘lchamiga moslashadi
)
#stat buyrug'iga javob beruvchi qisim
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Asalomu alaykum kerakli bo'limni tanglang", reply_markup=menu)



# taqdimot yaratish
@dp.message(F.text == "taqdimot yaratish")
async def setting_handler(message: types.Message):
    await message.answer("taadimot yatarishni boshlayamiz")


#qoshimcha hizmatlar
@dp.message(F.text == "Qo'shimcha hizmatlar")
async def setting_handler(message: types.Message):
    await message.answer("kerakli bo'limni tanglang")


#abturintlar uchiun
@dp.message(F.text =="Abturentlar uchun")
async def setting_handler(message: types.Message):
    await message.answer("kerakli bo'linmi tanglang")
    


#profel
@dp.message(F.text == "Profel")
async def setting_handler(message: types.Message):
    await message.answer("siz o'z profelingizdasiz")










async def main() -> None:
    bot = Bot(token= "7481510974:AAG0pPCCCpBIU3zVy7EZoTNapuBDauUWEug",default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
