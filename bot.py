import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import time

bot = Bot(token='8778399471:AAF_UIzAwtlCmZIiA4MNpYe35PizGNxri20')
dp = Dispatcher()
url = f'https://ilnursh.github.io/web_appss/?v={int(time.time())}'

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text='Открыть магазин',
                web_app=WebAppInfo(url=url)
            )]
        ],
        resize_keyboard=True
    )
    
    await message.answer('Привет! Нажми кнопку, чтобы открыть магазин',reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")