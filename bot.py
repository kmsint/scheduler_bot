import asyncio
import logging

from aiogram import Bot, Dispatcher


from config_data.config import Config, load_config
from handlers.other_handlers import register_echo_handler
from handlers.user_handlers import register_user_handlers
# from keyboards.main_menu import set_main_menu
from utils.scheduler import scheduler

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_echo_handler(dp)


async def send_message_to_admin(dp: Dispatcher):
    await dp.bot.send_message(chat_id=173901673, text='Сообщение')




async def some_func():
    print('some_text')
    await asyncio.sleep(1)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    scheduler.add_job(send_message_to_admin, 'interval', seconds=5, args=(dp,))

    # Настраиваем главное меню бота
    # await set_main_menu(dp)

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Запускаем polling
    try:
        scheduler.start()
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:

        # Запускаем функцию main
        # task = [scheduler(), main()]
        # asyncio.run(asyncio.wait(task))
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(main_2())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
