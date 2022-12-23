from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from lexicon.lexicon import LEXICON


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])


# Функция для регистрации хэндлеров пользователя в диспетчере
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
