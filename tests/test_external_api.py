import unittest
from unittest.mock import patch
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.external_api import convert_to_rub
from dotenv import load_dotenv

load_dotenv()


class TestExternalAPI(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_success(self, mock_get):
        mock_response = unittest.mock.MagicMock()
        mock_response.json.return_value = {"result": 7500.0}
        mock_get.return_value = mock_response

        amount = 100.0
        from_currency = "USD"
        result = convert_to_rub(amount, from_currency)
        self.assertEqual(result, 7500.0)
        self.assertIsInstance(result, float)

    @patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": ""})
    def test_convert_to_rub_no_api_key(self):
        amount = 100.0
        from_currency = "USD"
        with self.assertRaises(ValueError):
            convert_to_rub(amount, from_currency)

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_api_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        amount = 100.0
        from_currency = "USD"
        with self.assertRaises(ValueError):
            convert_to_rub(amount, from_currency)

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_bad_response(self, mock_get):
        mock_response = unittest.mock.MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTPError")
        mock_get.return_value = mock_response
        amount = 100.0
        from_currency = "USD"
        with self.assertRaises(ValueError):
            convert_to_rub(amount, from_currency)