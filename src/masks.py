from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    принимает параметр card_number:
    возвращает маску номера карты
    """
    if card_number == "":
        return "Введите корректный номер"
    else:
        masked_number = card_number[0:-10] + " " + "** ****" + card_number[-4:]
        return masked_number


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    принимает параметр account_number:
    возвращает маску номера счета
    """
    if account_number == "":
        return "Введите корректный номер"
    else:
        masked_number = account_number[:4] + " " + "**" + account_number[-4:]
        return masked_number


print(get_mask_account("11111111111111111111"))
print("hello")