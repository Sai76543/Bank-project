import unittest
from unittest.mock import patch
import os
import sys
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import get_transaction_amount_rub
from src.data_loader import load_operations_data # Import load_operations_data

class TestUtils(unittest.TestCase):

    TEST_CSV_FILENAME = "test_transactions.csv"
    TEST_XLSX_FILENAME = "test_transactions.xlsx"

    def setUp(self):
        # Создаем тестовые файлы CSV и XLSX с известным содержимым
        self.create_test_csv(self.TEST_CSV_FILENAME)
        self.create_test_xlsx(self.TEST_XLSX_FILENAME)

    def tearDown(self):
        # Удаляем тестовые файлы после каждого теста
        if os.path.exists(self.TEST_CSV_FILENAME):
            os.remove(self.TEST_CSV_FILENAME)
        if os.path.exists(self.TEST_XLSX_FILENAME):
            os.remove(self.TEST_XLSX_FILENAME)

    def create_test_csv(self, filename):
        data = {'id': [1, 2, 3],
                'amount': [100.0, 200.0, 150.0],  # Укажите тип float для числовых значений
                'operationAmount': ['{"amount": "100", "currency": {"code": "RUB"}}',
                                    '{"amount": "200", "currency": {"code": "USD"}}',
                                    '{"amount": "150", "currency": {"code": "EUR"}}']}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    def create_test_xlsx(self, filename):
        data = {'id': [1, 2, 3],
                'amount': [100.0, 200.0, 150.0],  # Укажите тип float для числовых значений
                'operationAmount': ['{"amount": "100", "currency": {"code": "RUB"}}',
                                    '{"amount": "200", "currency": {"code": "USD"}}',
                                    '{"amount": "150", "currency": {"code": "EUR"}}']}
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    def test_load_operations_data_csv(self):
        data = load_operations_data(self.TEST_CSV_FILENAME)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)

        # Проверяем содержимое первой транзакции
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['amount'], 100.0)
        self.assertEqual(data[0]['operationAmount'], '{"amount": "100", "currency": {"code": "RUB"}}')

        # Проверяем содержимое второй транзакции
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[1]['amount'], 200.0)
        self.assertEqual(data[1]['operationAmount'], '{"amount": "200", "currency": {"code": "USD"}}')

    def test_load_operations_data_xlsx(self):
        data = load_operations_data(self.TEST_XLSX_FILENAME)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)

        # Проверяем содержимое первой транзакции
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['amount'], 100.0)
        self.assertEqual(data[0]['operationAmount'], '{"amount": "100", "currency": {"code": "RUB"}}')

        # Проверяем содержимое второй транзакции
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[1]['amount'], 200.0)
        self.assertEqual(data[1]['operationAmount'], '{"amount": "200", "currency": {"code": "USD"}}')

    def test_load_operations_data_unsupported_format(self):
        with self.assertRaises(ValueError):
            load_operations_data("test.txt")

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