
from settings import *

class CurrencyService:
    def __init__(self) -> None:
        self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        self.scheduler = AsyncIOScheduler()

    async def fetch_currency_rates(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(CB_URL) as response:
                return await response.text()

    def parse_xml(self, xml_data) -> None:
        root = ET.fromstring(xml_data)
        root = ET.fromstring(xml_data)
        date = root.get('Date')
        self.redis.set('last_update', date)
        for valute in root.findall('Valute'):
            code = valute.find('CharCode').text
            nominal = float(valute.find('Nominal').text)
            value = float(valute.find('Value').text.replace(',', '.'))
            rate = value / nominal
            self.redis.set(code, rate)
    
    async def update_currency_rates(self) -> None:
        try:
            xml_data = await self.fetch_currency_rates()
            self.parse_xml(xml_data)
            print("Currency rates updated")
        except Exception as e:
            print("Error updating currency rates")
            logging.error(f"Error updating currency rates: {e}\n{traceback.format_exc()}")

    def get_rate(self, currency_code: int) -> float|None:
        rate = self.redis.get(currency_code)
        return float(rate) if rate else None

    def start_scheduler(self):
        self.scheduler.add_job(self.update_currency_rates, 'cron', hour=0, minute=0)  # Обновление каждый день в полночь
        self.scheduler.start()