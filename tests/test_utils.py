import unittest
from unittest.mock import patch
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import load_operations_data, get_transaction_amount_rub


class TestUtils(unittest.TestCase):

    def test_load_operations_data_valid_file(self):
        with open("temp_test_file.json", "w", encoding="utf-8") as f:
            f.write('[{"id": 1, "amount": 100}]')
        data = load_operations_data("temp_test_file.json")
        self.assertTrue(isinstance(data, list))
        os.remove("temp_test_file.json")  # Удаляем файл

    def test_load_operations_data_file_not_found(self):
        data = load_operations_data("non_existent_file.json")
        self.assertEqual(data, [])

    @patch('src.external_api.convert_to_rub')
    def test_get_transaction_amount_rub_usd(self, mock_convert_to_rub):
        transaction = {"operationAmount": {"amount": "50.00", "currency": {"code": "USD"}}}
        mock_convert_to_rub.return_value = 3000.0
        amount = get_transaction_amount_rub(transaction)
        self.assertEqual(amount, 3000.0)

    def test_get_transaction_amount_rub_unsupported_currency(self):
        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "GBP"}}}
        with self.assertRaises(ValueError):
            get_transaction_amount_rub(transaction)