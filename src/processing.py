from typing import Any, Dict, Iterable


def filter_by_currency(list_dict_check: Iterable[Dict], value_key: str = "USD") -> Iterable[Dict]:
    """Функция которая, принимает на вход список словарей, представляющих транзакции и возвращает итератор с соответствующей валютой 'USD'."""
    for check_dict in list_dict_check:
        if (check_dict["operationAmount"]["currency"]["code"]) == value_key:
            yield check_dict
        elif (check_dict["operationAmount"]["currency"]["code"]) == "RUB":
            continue
        elif (check_dict["operationAmount"]["currency"]["code"]) != value_key:
            raise TypeError("Не соответствует заданной валюте")


def transaction_descriptions(list_dict: Iterable[Dict], key: str = "description") -> Iterable[Dict]:
    """Функция который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for check_key in list_dict:
        if key in check_key:
            yield check_key[key]
        elif not check_key.get(key):
            raise TypeError("Отсутствует строка")


def card_number_generator(start: int, stop: int) -> Any:
    """Функция-генератор которая принимает начальное и конечное значения для генерации диапазона номеров."""
    if start >= stop:
        raise IndexError("Неправильный ввод данных")
    for card_list in range(start, stop):
        if 1 <= start <= 9999999999999999 or 1 <= stop <= 9999999999999999:
            card_number = "".join(f"{card_list:016}" for _ in range(16))
            formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
            yield formatted_card_number