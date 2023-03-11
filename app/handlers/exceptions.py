from aiogram import types


class TownNotFoundException(Exception):
    pass


async def type_error(exc: types.error_event.ErrorEvent):
    await exc.update.message.answer(f"{exc.exception}")
