from typing import Union
import logging
import os

# Настройка логирования
logger = logging.getLogger(__name__)  # Имя логгера - имя модуля
logger.setLevel(logging.DEBUG)

# Создание папки logs
logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Создание обработчика для записи в файл
log_file = os.path.join(logs_dir, 'masks.log')  # Полный путь к файлу
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')  # 'w' перезаписывает файл

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Принимает параметр card_number:
    возвращает маску номера карты
    """
    logger.info(f"Вызвана функция get_mask_card_number с номером карты: {card_number}")
    if card_number == "":
        logger.warning("Передан пустой номер карты")
        return "Введите корректный номер"
    else:
        masked_number = card_number[:-10] + " " + "** ****" + card_number[-4:]
        logger.debug(f"Замаскированный номер карты: {masked_number}")
        return masked_number


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Принимает параметр account_number:
    возвращает маску номера счета
    """
    logger.info(f"Вызвана функция get_mask_account с номером счета: {account_number}")
    if account_number == "":
        logger.warning("Передан пустой номер счета")
        return "Введите корректный номер"
    else:
        masked_number = account_number[:4] + " " + "**" + account_number[-4:]
        logger.debug(f"Замаскированный номер счета: {masked_number}")
        return masked_number


if __name__ == '__main__':
    print(get_mask_account("11111111111111111111"))
    print("hello")
