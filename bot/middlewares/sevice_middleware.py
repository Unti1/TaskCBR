

from typing import Any, Awaitable, Callable, Coroutine, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from tools.currency_service import CurrencyService


class CurrencyServiceMiddleware(BaseMiddleware):
    def __init__(self, service: CurrencyService) -> None:
        self.service: CurrencyService = service

    async def __call__(self, 
                 handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                 event: TelegramObject, 
                 data: Dict[str, Any]) -> Coroutine[Any, Any, Any]:
        data['currency_service'] = self.service
        return await handler(event, data)