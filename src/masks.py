from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    принимает параметр card_number:
    возвращает маску номера карты
    """
    masked_number = card_number[0:-12] + " " + "** ****" + card_number[-4:]
    return masked_number


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    принимает параметр account_number:
    возвращает маску номера счета
    """
    masked_number = account_number[:4] + " " + "**" + account_number[-4:]
    return masked_number
