import requests
import json
from config import money

class ConverterBot:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise ConvertationException(f'нельзя конвертировать одинаковые валюты))')
        try:
            base_ticket = money[base]
        except KeyError:
            raise ConvertationException(f'Не удалось обработать валюту "{base}"')

        try:
            quote_ticket = money[quote]
        except KeyError:
            raise ConvertationException(f'Не удалось обработать валюту "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertationException(f'Не удалось обработать количество "{amount}"')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticket}&tsyms={quote_ticket}')
        total = float(json.loads(r.content)[quote_ticket])
        total = round(amount * total, 2)
        return total

# собственный класс  исключений
class ConvertationException(Exception):
    pass