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