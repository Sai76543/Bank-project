import pytest


from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date


@pytest.mark.parametrize("card_num, expected", [("1111111111232123", "111111 ** ****2123"),
                                                ("2100709056785342", "210070 ** ****5342"),
                                                ("", "Введите корректный номер")
                                                ])
def test_get_mask_card_number_input(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("account_num, expected", [("87965436543212345674", "8796 **5674"),
                                                   ("45673546876549876543", "4567 **6543"),
                                                   ("", "Введите корректный номер")
                                                   ])
def test_get_mask_account_input(account_num, expected):
    assert get_mask_account(account_num) == expected