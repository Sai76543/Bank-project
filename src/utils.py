import json
import os

def load_operations_data(filepath):
    """
    Загружает данные о финансовых транзакциях из JSON-файла и возвращает список словарей.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if not isinstance(data, list):
                print(f"Ошибка: Файл {filepath} содержит данные не в формате списка.")
                return []

            return data

    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {filepath} содержит некорректный JSON.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {filepath}: {e}")
        return []


def get_transaction_amount_rub(transaction):
    """
    Извлекает сумму транзакции в рублях из словаря с данными о транзакции.
    """
    from src.external_api import convert_to_rub  # ИСПРАВЛЕННЫЙ ИМПОРТ!
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount
    elif currency_code in ("USD", "EUR"):
        return convert_to_rub(amount, currency_code)
    else:
        raise ValueError(f"Неподдерживаемая валюта: {currency_code}")