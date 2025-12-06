import unittest
from unittest.mock import MagicMock
from controllers.currencycontroller import CurrencyController


class TestCurrencyController(unittest.TestCase):


    def test_list_currencies(self):

        mock_db = MagicMock()
        mock_db._read.return_value = [
            {"id": 1, "char_code": "USD", "value": 90.0},
            {"id": 2, "char_code": "EUR", "value": 91.0}
        ]

        controller = CurrencyController(mock_db)
        result = controller.list_currencies()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['char_code'], "USD")
        mock_db._read.assert_called_once()

    def test_update_currency(self):

        mock_db = MagicMock()
        mock_db._update.return_value = True

        controller = CurrencyController(mock_db)
        result = controller.update_currency("USD", 95.0)

        self.assertTrue(result)
        mock_db._update.assert_called_once_with({"USD": 95.0})

    def test_delete_currency(self):

        mock_db = MagicMock()
        mock_db._delete.return_value = True

        controller = CurrencyController(mock_db)
        result = controller.delete_currency(1)

        self.assertTrue(result)
        mock_db._delete.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()