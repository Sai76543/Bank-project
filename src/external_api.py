import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"

def convert_to_rub(amount, from_currency):
    """
    Конвертирует сумму из указанной валюты в рубли, используя Exchange Rates Data API.
    """

    if not API_KEY:
        raise ValueError("API key не найден в .env файле.")

    url = f"{BASE_URL}latest?symbols=RUB&base={from_currency}"

    headers = {
    "apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "rates" in data and "RUB" in data["rates"]:
            rub_rate = data["rates"]["RUB"]
            return amount * rub_rate
        else:
            raise ValueError("Не удалось получить курс рубля из API ответа.")

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка при запросе к API: {e}")
    except Exception as e:
        raise ValueError(f"Произошла непредвиденная ошибка: {e}")