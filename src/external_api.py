import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"


def convert_to_rub(amount, from_currency):
    """
    Конвертирует сумму из указанной валюты в рубли, используя Exchange Rates Data API.
    Использует endpoint convert для прямой конвертации.
    Возвращает float.
    """

    if not API_KEY:
        raise ValueError("API key для Exchange Rates Data API не найден в .env файле.")

    url = f"{BASE_URL}convert?to=RUB&from={from_currency}&amount={amount}"

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "result" in data:
            converted_amount = float(data["result"])
            return converted_amount
        else:
            raise ValueError("Не удалось получить сконвертированную сумму из API ответа.")

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка при запросе к API: {e}")
    except Exception as e:
        raise ValueError(f"Произошла непредвиденная ошибка: {e}")