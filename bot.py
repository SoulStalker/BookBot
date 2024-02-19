import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


logger = logging.getLogger(__name__)


# Function for configuring and launching the bot
async def main() -> None:
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    # Console outputs information about the start of the bot's launch
    logger.info('Starting bot...')

    # Load the config into the config variable
    config: Config = load_config('.env')

    # Initialize the bot and dispatcher
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher()

    # Customize the bot's main menu
    await set_main_menu(bot)

    # Register the routers in the manager
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Skip the backlog of updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

