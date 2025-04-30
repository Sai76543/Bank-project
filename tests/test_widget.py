import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 700079 ** ****6361"),
        ("MasterCard 1234567890123456", "MasterCard 123456 ** ****3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("date,expected", [
    ("2023-10-15", "15.10.2023"),
    ("2000-01-01", "01.01.2000")
])
def test_get_date(date, expected):
    assert get_date(date) == expected





