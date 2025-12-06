import unittest
from unittest.mock import patch, MagicMock
from main import get_currencies


class TestGetCurrenciesAssignment(unittest.TestCase):


    def test_real_currencies(self):
        """
         Проверить корректный возврат реальных курсов
        """
        try:
            # получаем реальные данные
            result = get_currencies(["USD", "EUR"])

            # проверки
            self.assertIsInstance(result, dict)
            self.assertIn("USD", result)
            self.assertIn("EUR", result)
            self.assertIsInstance(result["USD"], float)
            self.assertIsInstance(result["EUR"], float)

        except ConnectionError:
            self.skipTest("Нет доступа к API - пропускаем тест с реальными данными")

    def test_nonexistent_currency_behavior(self):
        """
        При несуществующей валюте
        """
        try:
            # Должен выбросить KeyError
            with self.assertRaises(KeyError):
                get_currencies(["XYZ"])
        except ConnectionError:
            self.skipTest("Нет доступа к API")

    @patch('main.requests.get')
    def test_connection_error_exception(self, mock_get):
        """
        Выброс ConnectionError
        """
        # Создаем ошибку сети
        mock_get.side_effect = Exception("Network error")

        # Проверяем
        with self.assertRaises(ConnectionError):
            get_currencies(["USD"], url="https://test.com")

    @patch('main.requests.get')
    def test_value_error_exception(self, mock_get):
        """
        Проверить ValueError
        """
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            get_currencies(["USD"])

    @patch('main.requests.get')
    def test_key_error_exception(self, mock_get):
        """
         Проверить KeyError
        """
        mock_response = MagicMock()
        # Ответ без ключа Valute
        mock_response.json.return_value = {"Date": "2024-01-01"}
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError):
            get_currencies(["USD"])


if __name__ == '__main__':
    unittest.main(verbosity=2)