import unittest
import io
from main import logger, get_currencies


class TestStreamWrite(unittest.TestCase):


    def setUp(self):

        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def wrapped():
            return get_currencies(['USD'], url="https://invalid")

        self.wrapped = wrapped

    def test_logging_error(self):
        """Тест логирования ошибки"""
        # Функция с ConnectionError
        with self.assertRaises(ConnectionError):
            self.wrapped()

        #  Получаем логи
        logs = self.stream.getvalue()

        # Проверяем
        self.assertIn("ERROR", logs)
        self.assertIn("ConnectionError", logs)

        print(" Тест из задания выполнен успешно!")
        print(f"Логи: {logs}")


if __name__ == '__main__':
    unittest.main(verbosity=2)