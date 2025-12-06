import unittest
import io
from main import logger, get_currencies


class TestStreamWriteSimple(unittest.TestCase):

    def setUp(self):
        """Создаем StringIO и декорированную функцию"""
        self.nonstandardstream = io.StringIO()

        # создаем функцию и декорируем её
        @logger(handle=self.nonstandardstream)
        def decorated_get_currencies():
            return get_currencies(['USD'], url="https://invalid")

        self.decorated_func = decorated_get_currencies

    def test_error_logging(self):
        """Тестируем логирование ошибки"""
        # 1. Функция должна упасть с ConnectionError
        with self.assertRaises(ConnectionError):
            self.decorated_func()

        # 2. Получаем логи
        logs = self.nonstandardstream.getvalue()

        # 3. Проверяем наличие ERROR
        self.assertIn("ERROR", logs)

        # 4. Проверяем наличие ConnectionError
        self.assertIn("ConnectionError", logs)

        print(" Тест пройден: ERROR и ConnectionError найдены в логах")

    def tearDown(self):
        """Очистка"""
        # очистится
        pass



if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)