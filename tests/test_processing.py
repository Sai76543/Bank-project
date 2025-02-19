import pytest

from src.processing import filter_by_state, sort_by_date




@pytest.fixture()
def test_dict_list():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(test_dict_list):
    assert filter_by_state(test_dict_list, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.fixture()
def test_dict_list():
    return []


def test_filter_by_state_without_requested_state(test_dict_list):
    assert filter_by_state(test_dict_list, "AUTHORIZATION") == []

@pytest.fixture()
def test_dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(test_dict_list):
    assert sort_by_date(test_dict_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

@pytest.fixture()
def test_dict_list():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_reverse(test_dict_list):
    assert sort_by_date(test_dict_list, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

@pytest.fixture()
def test_dict_list_incorrect_date():
    return "Invalid isoformat string: '30.06.2018'"


def test_sort_by_date_incorrect_formating(test_dict_list_incorrect_date):
    with pytest.raises(TypeError) as exc_info:
        sort_by_date(test_dict_list_incorrect_date) == "Invalid isoformat string: '30.06.2018'"


@pytest.fixture()
def test_dict_list_incorrect_date_second_version():
    return (
            "Invalid isoformat string: 'четырнадцатое октября две" "тысячи восемнадцатого года'"
        )


def test_sort_by_date_incorrect_formating_texting(test_dict_list_incorrect_date_second_version):
    with pytest.raises(TypeError):
        sort_by_date(test_dict_list_incorrect_date_second_version) == (
            "Invalid isoformat string: 'четырнадцатое октября две" "тысячи восемнадцатого года'"
        )


import unittest
from src.processing import filter_by_description, categorize_operations, filter_by_state, sort_by_date
from collections import Counter
from datetime import datetime

class TestProcessing(unittest.TestCase):

    def test_filter_by_state(self):
        transactions = [
            {"state": "EXECUTED"},
            {"state": "CANCELED"},
            {"state": "EXECUTED"}
        ]
        result = filter_by_state(transactions, "EXECUTED")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["state"], "EXECUTED")

    def test_sort_by_date(self):
        transactions = [
            {"date": "2024-01-01T10:00:00.000"},
            {"date": "2024-01-03T10:00:00.000"},
            {"date": "2024-01-02T10:00:00.000"}
        ]
        result = sort_by_date(transactions)
        self.assertEqual(result[0]["date"], "2024-01-03T10:00:00.000")
        result = sort_by_date(transactions, sort_by_date_descending=False)
        self.assertEqual(result[0]["date"], "2024-01-01T10:00:00.000")


    def test_filter_by_description(self):
        transactions = [
            {"description": "Перевод организации ООО \"Рога и копыта\""},
            {"description": "Покупка в магазине \"Пятерочка\""},
            {"description": "Оплата услуг связи"},
            {"description": "Перевод другу"}
        ]

        result1 = filter_by_description(transactions, "перевод")
        self.assertEqual(len(result1), 2)
        self.assertEqual(result1[0]["description"], "Перевод организации ООО \"Рога и копыта\"")

        result2 = filter_by_description(transactions, "магазине")
        self.assertEqual(len(result2), 1)
        self.assertEqual(result2[0]["description"], "Покупка в магазине \"Пятерочка\"")

        result3 = filter_by_description(transactions, "нет совпадений")
        self.assertEqual(len(result3), 0)

    def test_categorize_operations(self):
        transactions = [
            {"description": "Перевод"},
            {"description": "Покупка"},
            {"description": "Оплата"},
            {"description": "Перевод"},
            {"description": "Покупка"}
        ]

        result = categorize_operations(transactions)
        self.assertIsInstance(result, Counter)
        self.assertEqual(result["Перевод"], 2)
        self.assertEqual(result["Покупка"], 2)
        self.assertEqual(result["Оплата"], 1)
