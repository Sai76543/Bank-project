from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    принимает параметр card_number:
    возвращает маску номера карты
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

print(get_mask_card_number("7000792289606361")) # входной аргумент


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    принимает параметр account_number:
    возвращает маску номера счета
    """
    return f"**{account_number[-4:]}"

print(get_mask_account("73654108430135874305")) # входной аргумент