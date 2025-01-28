import pytest
from tests.cfgtest import test_transactions
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(test_transactions):
    generator = filter_by_currency(test_transactions)
    assert next(generator) == test_transactions[0]
    assert next(generator) == test_transactions[1]
    assert next(generator) == test_transactions[3]

def test_filter_by_currency_other_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "RUB")
    assert next(generator) == test_transactions[2]
    assert next(generator) == test_transactions[4]

def test_filter_by_currency_absent_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator) == StopIteration

def test_filter_by_currency_absent_list():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator) == StopIteration


def test_transaction_descriptions(test_transactions):
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"

def test_transaction_descriptions():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator) == StopIteration

def test_card_number_generator_min():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_max():
    generator = card_number_generator(9999999999999997, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"

