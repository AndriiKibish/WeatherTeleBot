from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from bot_token import BOT_TOKEN
from funcs import get_weather_city, pars_weather_data

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


async def process_start_command(message: Message):
    await message.answer(
        'Hi! Send me the name of the city and I will show you what is the weather there now')


async def process_city_answer(message: Message):
    await message.answer(pars_weather_data(get_weather_city(f'{message.text}')))


dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_city_answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
