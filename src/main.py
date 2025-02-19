import logging
import os
from src.data_loader import load_operations_data
from src.processing import filter_by_description, categorize_operations
import datetime

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logs_dir = "logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file = os.path.join(logs_dir, 'main.log')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    """
    Основная логика программы для работы с банковскими транзакциями.
    """
    logger.info("Запуск программы")
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор: ")

        if choice in ("1", "2", "3"):
            if choice == "1":
                filepath = input("Введите путь к JSON-файлу: ")
                logger.info(f"Выбран JSON-файл: {filepath}")
            elif choice == "2":
                filepath = input("Введите путь к CSV-файлу: ")
                logger.info(f"Выбран CSV-файл: {filepath}")
            else:
                filepath = input("Введите путь к XLSX-файлу: ")
                logger.info(f"Выбран XLSX-файл: {filepath}")

            try:
                transactions = load_operations_data(filepath)
                if not transactions:
                    print("Не удалось загрузить транзакции. Проверьте файл и его формат.")
                    logger.warning("Не удалось загрузить транзакции")
                    continue  # Вернуться к началу цикла
                else:
                    logger.info(f"Успешно загружено {len(transactions)} транзакций.")
                    print(f"Для обработки выбран {filepath.split('.')[-1].upper()}-файл.") # Более корректное сообщение

                break  # Выйти из цикла, если файл успешно загружен

            except Exception as e:
                print(f"Произошла ошибка при загрузке файла: {e}")
                logger.exception("Ошибка при загрузке файла")

        else:
            print("Некорректный выбор. Пожалуйста, выберите пункт меню 1, 2 или 3.")
            logger.warning(f"Некорректный выбор пункта меню: {choice}")

    # Фильтрация по статусу
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(available_statuses)}")
        status = input("Ваш выбор: ").upper()

        if status in available_statuses:
            filtered_transactions = [t for t in transactions if t.get("state") == status]
            logger.info(f"Операции отфильтрованы по статусу: {status}")
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")
            logger.warning(f"Некорректный статус операции: {status}")

    # Сортировка по дате
    sort_by_date = input("\nОтсортировать операции по дате? Да/Нет: ").lower()
    if sort_by_date == "да":
        order = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").lower()
        if order in ("возрастанию", "убыванию"):
            reverse = order == "убыванию"
            try:
                filtered_transactions.sort(key=lambda t: datetime.datetime.strptime(t["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
                logger.info(f"Операции отсортированы по дате в порядке: {order}")
            except (ValueError, KeyError) as e:
                print(f"Ошибка при сортировке по дате: {e}.  Возможно, неверный формат даты.")
                logger.error(f"Ошибка при сортировке по дате: {e}")
        else:
            print("Некорректный порядок сортировки.")
            logger.warning(f"Некорректный порядок сортировки: {order}")

    # Фильтр рублевых транзакций
    ruble_only = input("\nВыводить только рублевые транзакции? Да/Нет: ").lower()
    if ruble_only == "да":
        filtered_transactions = [t for t in filtered_transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]
        logger.info("Отображены только рублевые транзакции.")

    # Фильтр по слову в описании
    filter_description = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_description == "да":
        search_word = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_by_description(filtered_transactions, search_word)
        logger.info(f"Список транзакций отфильтрован по слову: {search_word}")

    # Вывод итогового списка транзакций
    print("\nРаспечатываю итоговый список транзакций...")

    if filtered_transactions:
        for transaction in filtered_transactions:
            print(transaction) #  Или форматируйте вывод как вам нужно
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    logger.info("Завершение программы")


if __name__ == "__main__":
    main()