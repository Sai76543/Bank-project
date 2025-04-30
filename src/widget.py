from src.masks import get_mask_card_number, get_mask_account
from typing import Union


def mask_account_card(card_number: Union[str]) -> Union[str]:
    """ Функция, которая маскирует номер счета или карты"""
    if "Счет" in card_number or "Счёт" in card_number:
        return get_mask_account(card_number)

    elif "Visa" in card_number or "Maestro" in card_number or "MasterCard" in card_number:
        return get_mask_card_number(card_number)


def get_date(core_date: str) -> str:
    """Принимает дату и время в формате ISO 8601, возвращает дату в формате ДД.ММ.ГГГГ"""
    core_date_list = core_date.split("-")
    if (
        core_date_list[0].isdigit()
        and core_date_list[1].isdigit()
        and core_date_list[2][:2].isdigit
        and len(core_date_list) == 3
    ):
        returned_date = core_date_list[2][:2] + "." + core_date_list[1] + "." + core_date_list[0]
        return returned_date
    raise ValueError("некорректный формат даты")




print(mask_account_card("Union Pay 6010203040506070"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2000-03-11"))
