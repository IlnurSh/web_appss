from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('8778399471:AAF_UIzAwtlCmZIiA4MNpYe35PizGNxri20')
dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу', web_app=WebAppInfo(url='https://yandex.ru/search/?text=сверхъестественное+сколько+смотрет&lr=50&clid=11528080')))
    await message.answer('Привет мой друг', reply_markup=markup)

    await dp.start_polling(bot)# запускает полинг


if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(cmd_start())
    except KeyboardInterrupt:
        print("Бот остановлен")