import asyncio
import os  # 👈 ВАЖНО: добавить этот импорт!
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import time
import json

# 👇 Берем токен из переменных окружения Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Проверка (для отладки, потом можно убрать)
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в переменных окружения!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    cache_buster = int(time.time() * 1000)
    url = f'https://ilnursh.github.io/web_appss/?v={cache_buster}'
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text='Открыть магазин',
                web_app=WebAppInfo(url=url)
            )]
        ],
        resize_keyboard=True
    )
    
    await message.answer('Привет! Нажми кнопку, чтобы открыть магазин', reply_markup=keyboard)

@dp.message()
async def handle_web_app(message: types.Message):
    if message.web_app_data:
        data = json.loads(message.web_app_data.data)
        name = data.get('name', 'Не указано')
        email = data.get('email', 'Не указано')
        phone = data.get('phone', 'Не указано')
        
        await message.answer(f"✅ Заказ получен!\n\n👤 Имя: {name}\n📧 Email: {email}\n📱 Телефон: {phone}")
    else:
        await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")