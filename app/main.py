import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart

from app.config import config
from app.database import database
from app.handlers.basic import get_start, personal_data
from app.handlers.exceptions import type_error
from app.handlers.forms import load_new_trip, get_first_place, get_last_place, get_transport_type, get_language, \
    cancel_handler
from app.middlewares.required import RequiredMiddleware
from app.utils.commands import set_commands
from app.utils.statesform import LoadTrip


async def start_bot(bot: Bot):
    await set_commands(bot=bot)
    await bot.send_message(config.my_telegram_id, text=f"<b>Bot started!</b>")
    await database.connect_database()
    await database.create_countries_table()
    await database.create_travels_table()


async def stop_bot(bot: Bot):
    await bot.send_message(config.my_telegram_id, text=f"<b>Bot stopped!</b>")
    await database.disconnect_database()


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=config.token, parse_mode='HTML')
    db = Dispatcher()
    db.message.middleware.register(RequiredMiddleware())
    db.startup.register(start_bot)
    db.shutdown.register(stop_bot)

    db.message.register(get_start, CommandStart())
    db.message.register(personal_data, Command(commands="my_data"))
    db.message.register(load_new_trip, Command(commands="load"))
    db.message.register(cancel_handler, Command(commands="cancel"))
    db.message.register(get_language, LoadTrip.LANGUAGE)
    db.message.register(get_first_place, LoadTrip.FIRST_PLACE)
    db.message.register(get_last_place, LoadTrip.LAST_PLACE)
    db.message.register(get_transport_type, LoadTrip.TRANSPORT_TYPE)
    db.errors.register(type_error)
    try:
        await db.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
    # F.text.casefold() == "cancel"