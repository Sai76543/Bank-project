import logging
from src.data_loader import load_operations_data
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file = os.path.join(logs_dir, 'utils.log')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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

    except ValueError as e:  # конкретизировал исключение
        logger.error(f"Ошибка ValueError при обработке транзакции: {e}")
        raise e  # Перевыбрасываем исключение после логирования
    except Exception as e:
        logger.exception(f"Произошла ошибка при обработке транзакции: {e}")
        raise  # Перевыбрасываем исключение после логирования