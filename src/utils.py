import json
import os
import logging

# Настройка логирования
logger = logging.getLogger(__name__)  # Имя логгера - имя модуля
logger.setLevel(logging.DEBUG)

# Создание папки logs
logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Создание обработчика для записи в файл
log_file = os.path.join(logs_dir, 'utils.log')  # Полный путь к файлу
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')  # 'w' перезаписывает файл

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_operations_data(filepath):
    """
    Загружает данные о финансовых транзакциях из JSON-файла и возвращает список словарей.
    """
    logger.info(f"Вызвана функция load_operations_data с файлом: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.debug(f"Данные успешно загружены из файла: {filepath}")

            if not isinstance(data, list):
                logger.warning(f"Файл {filepath} содержит данные не в формате списка.")
                return []

            return data

    except FileNotFoundError:
        logger.error(f"Файл {filepath} не найден: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {filepath} содержит некорректный JSON: {filepath}")
        return []
    except Exception as e:
        logger.exception(f"Произошла ошибка при чтении файла {filepath}: {e}")
        return []


def get_transaction_amount_rub(transaction):
    """
    Извлекает сумму транзакции в рублях из словаря с данными о транзакции.
    """
    logger.info(f"Вызвана функция get_transaction_amount_rub с транзакцией: {transaction}")
    try:
        from src.external_api import convert_to_rub  # ИСПРАВЛЕННЫЙ ИМПОРТ!
        amount = float(transaction["operationAmount"]["amount"])
        currency_code = transaction["operationAmount"]["currency"]["code"]
        logger.debug(f"Сумма: {amount}, Валюта: {currency_code}")

        if currency_code == "RUB":
            logger.debug(f"Сумма уже в рублях: {amount}")
            return amount
        elif currency_code in ("USD", "EUR"):
            logger.info(f"Конвертация {amount} {currency_code} в рубли")
            amount = convert_to_rub(amount, currency_code)
            logger.debug(f"Сумма после конвертации: {amount} RUB")
            return amount
        else:
            logger.warning(f"Неподдерживаемая валюта: {currency_code}")
            raise ValueError(f"Неподдерживаемая валюта: {currency_code}")

    except ValueError as e: # конкретизировал исключение
        logger.error(f"Ошибка ValueError при обработке транзакции: {e}")
        raise e # Перевыбрасываем исключение после логирования
    except Exception as e:
        logger.exception(f"Произошла ошибка при обработке транзакции: {e}")
        raise  # Перевыбрасываем исключение после логирования