import json
import logging
import pandas as pd
import os
from typing import List, Dict

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file = os.path.join(logs_dir, 'data_loader.log')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_operations_data(filepath: str) -> List[Dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-, CSV- или XLSX-файла
    и возвращает список словарей.
    """
    logger.info(f"Вызвана функция load_operations_data с файлом: {filepath}")
    try:
        file_extension = filepath.split('.')[-1].lower()

        if file_extension == 'json':
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    logger.warning(f"Файл {filepath} содержит данные не в формате списка.")
                    return []
                logger.debug(f"Данные успешно загружены из JSON-файла: {filepath}")
                return data

        elif file_extension == 'csv':
            df = pd.read_csv(filepath)
            data = df.to_dict(orient='records')
            logger.debug(f"Данные успешно загружены из CSV-файла: {filepath}")
            return data

        elif file_extension == 'xlsx':
            df = pd.read_excel(filepath)
            data = df.to_dict(orient='records')
            logger.debug(f"Данные успешно загружены из XLSX-файла: {filepath}")
            return data

        else:
            logger.error(f"Неподдерживаемый формат файла: {filepath}")
            raise ValueError(f"Неподдерживаемый формат файла: {filepath}")

    except FileNotFoundError:
        logger.error(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {filepath} содержит некорректный JSON.")
        return []
    except Exception as e:
        logger.exception(f"Произошла ошибка при чтении файла {filepath}: {e}")
        return []