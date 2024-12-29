from src.masks import get_mask_card_number, get_mask_account
from typing import Union


def mask_account_card(card_number: Union[str]) -> Union[str]:
    """ Функция, которая маскирует номер счета или карты"""
    if "Счет" in card_number or "Счёт" in card_number:
        return get_mask_account(card_number)

    elif "Visa" in card_number or "Maestro" in card_number or "MasterCard" in card_number:
        return get_mask_card_number(card_number)


def get_date(user_date: Union[str]) -> Union[str]:
    """Функция получения даты в определенном формате и возвращает в формате ДД.ММ.ГГГГ"""
    # Добавляем импорт библиотеки datetime
    import datetime
    # Преобразуем строку в объект datetime
    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматируем дату в строку "ДД.ММ.ГГГГ"
    new_date = date_format.strftime("%d.%m.%Y")
    # Возвращаем отформатированную дату
    return new_date


print(mask_account_card("Visa Platinum 1234567891234567"))
print(mask_account_card("Счет 35383033474447895560"))
print(get_date("2024-03-11T02:26:18.671407"))
