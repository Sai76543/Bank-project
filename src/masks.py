from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    принимает параметр card_number:
    возвращает маску номера карты
    """
    if card_number != "" and len(card_number) == 16:
        masked_number = card_number[0:-10] + " " + "** ****" + card_number[-4:]
        return masked_number
    else:
        return ("Введите корректный номер")


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    принимает параметр account_number:
    возвращает маску номера счета
    """
    if account_number != "" and len(account_number) == 20:
        masked_number = account_number[:4] + " " + "**" + account_number[-4:]
        return masked_number
    else:
        return "Введите корректный номер"

print(get_mask_card_number("1111111111232123"))
print("hello")