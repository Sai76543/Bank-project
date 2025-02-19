import re
from typing import List, Dict
from collections import Counter
from datetime import datetime

def filter_by_state(dict_list: list, state_value: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state. Возвращает новый список словарей, содержащий
    только те, у которых ключ state соответствует указанному значению (по умолчанию 'EXECUTED')"""
    returned_list = []
    for dict_ in dict_list:
        if dict_["state"] == state_value:
            returned_list.append(dict_)
    return returned_list


def sort_by_date(dict_list: list, sort_by_date_descending: bool = True) -> list:
    """Принимает список словарей. Возвращает новый список, отсортированный по дате от новых к старым. Если надо
    изменить порядок сортировки, то при вызове функции вторым параметром передай False"""
    sorted_list = sorted(
        dict_list, key=lambda strindate: datetime.fromisoformat(strindate["date"]), reverse=sort_by_date_descending
    )
    return sorted_list


def filter_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует список транзакций по наличию строки поиска в описании.

    Args:
        transactions: Список словарей с данными о банковских операциях.
        search_string: Строка поиска.

    Returns:
        Список словарей, у которых в описании есть данная строка.
    """
    search_string = search_string.lower()
    result = [
        transaction for transaction in transactions
        if transaction.get("description") and re.search(search_string, transaction["description"].lower())
    ]
    return result


def categorize_operations(transactions: List[Dict], category_field="description") -> Counter:
    """
    Категоризует операции по категориям, указанным в поле `category_field`, используя Counter.

    Args:
        transactions: Список словарей с данными о банковских операциях.
        category_field: Ключ, содержащий категорию операции (по умолчанию "description").

    Returns:
        Counter, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    categories = Counter(transaction.get(category_field) for transaction in transactions if transaction.get(category_field))
    return categories