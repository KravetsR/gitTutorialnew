import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # якщо користувача немає, добавляємо його
        db.add_subscriber(message.from_user.id)
    else:
        #якщо він вже є, обновляємо статус
        db.update_subscription(message.from_user.id, True)
    
    await message.answer('Ви успішно підписалися')

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # якщо користувача немає, добавляємо його з неактивною підпискою (запам'ятовуємо)
        db.add_subscriber(message.from_user.id, False)
        await message.answer('Ви не підписані')
    else:
        #якщо він вже є, обновляємо йому статус
        db.update_subscription(message.from_user.id, False)
        await message.answer('Ви успішно відписалися від розсилки')    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)