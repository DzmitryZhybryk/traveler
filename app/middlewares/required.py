from aiogram import BaseMiddleware, types
from typing import Callable, Awaitable, Dict, Any

from app.config import config


class RequiredMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
                       event: types.Message,
                       data: dict[str, Any]) -> Any:
        if event.from_user.id == config.my_telegram_id:
            return await handler(event, data)

        await event.answer(config.greeting_strangers)
