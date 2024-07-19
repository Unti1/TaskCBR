from bot.handlers import *
from settings import *
from bot.middlewares.sevice_middleware import CurrencyServiceMiddleware
from tools.currency_service import CurrencyService


async def main():
    bot = Bot(token = config['tg']['api'])
    
    currency_service = CurrencyService()
    currency_service.start_scheduler()
    await currency_service.update_currency_rates()

    dp = Dispatcher()
    dp.include_routers(
                       commands_.router, 
                       )
    dp.message.middleware(CurrencyServiceMiddleware(currency_service))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())