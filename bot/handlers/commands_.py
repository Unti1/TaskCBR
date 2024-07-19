from settings import *
from tools.currency_service import CurrencyService

router = Router()

@router.message(Command("start"))
async def start_msg(message: Message):
    await message.reply("Привет! Я бот для отображения курсов валют. Используйте /exchange для конвертации и /rates для просмотра курсов.")

@router.message(Command("exchange"))
async def exchange(message: Message, currency_service: CurrencyService, command: Command):
    example = 'Пример: /exchange USD RUB 10'
    
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы, при вводе. " + example
        )
        return
    
    try:
        from_currency, to_currency, amount = command.args.split()
        print(from_currency, to_currency, amount)
        from_rate = currency_service.get_rate(from_currency)
        to_rate = currency_service.get_rate(to_currency) if to_currency != "RUB" else 1 
        print(from_rate, to_rate)
        
        if from_rate is None or to_rate is None:
            await message.reply("Извините, не могу найти курс для указанных валют.")
            return

        result = float(amount) * (from_rate/to_rate)
        await message.reply(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError:
        await message.reply("Неверно." + example)
    
@router.message(Command("rates"))
async def rates(message: types.Message, currency_service: CurrencyService, command: Command):
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY']  # Пример списка валют
    rates = []
    for currency in currencies:
        rate = currency_service.get_rate(currency)
        if rate:
            rates.append(f"{currency}: {rate:.2f}")
    await message.reply("\n".join(rates))
