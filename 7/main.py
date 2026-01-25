import functools
import sys
import requests
from requests.exceptions import RequestException
import logging

def logger(func=None, *, handle=sys.stdout):
    """
        Декоратор для логирования вызовов функций.

        Может использоваться как с параметрами, так и без них:
            @logger
            @logger(handle=...)

        При каждом вызове функции логируются:
        - имя функции,
        - позиционные и именованные аргументы,
        - возвращаемое значение,
        - возникшие исключения.

        Parameters:
            func (callable, optional): Декорируемая функция.
                Если None, декоратор был вызван с параметрами.
            handle (file-like object or logging.Logger): Объект,
                в который производится логирование.
                По умолчанию sys.stdout.

        Returns:
            callable: Обёртка вокруг декорируемой функции.
        """
    if func is None:
        # @logger(handle=...) - нужно вернуть декоратор
        return lambda f: logger(f, handle=handle)

    # @logger декорируем сразу
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
                Обёртка над функцией, выполняющая логирование её вызова.

                Parameters:
                    *args: Позиционные аргументы функции.
                    **kwargs: Именованные аргументы функции.

                Returns:
                    Any: Результат выполнения декорируемой функции.

                Raises:
                    Exception: Повторно выбрасывает исключения,
                        возникшие внутри декорируемой функции.
                """
        if isinstance(handle, logging.Logger):
            handle.info(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                handle.info(f"{func.__name__} вернула {result}")
                return result
            except Exception as e:
                handle.error(f"{func.__name__} вызвала {type(e).__name__}: {e}")
                raise
        handle.write(f"INFO: Вызов {func.__name__} с args={args}, kwargs={kwargs}\n")
        if hasattr(handle, 'flush'):
            handle.flush()

        try:
            result = func(*args, **kwargs)
            handle.write(f"INFO: {func.__name__} вернула {result}\n")
            if hasattr(handle, 'flush'):
                handle.flush()
            return result
        except Exception as e:
            handle.write(f"ERROR: {func.__name__} вызвала {type(e).__name__}: {e}\n")
            if hasattr(handle, 'flush'):
                handle.flush()
            raise

    return wrapper

@logger
def get_currencies(
        currency_codes: list[str],
        url: str = "https://www.cbr-xml-daily.ru/daily_json.js"
) -> dict[str, float]:
    """
    Получает курсы валют с API Центробанка России.

        currency_codes: Список кодов валют (USD, EUR)
        url: URL API ЦБ РФ

        dict: {"USD": 93.25, "EUR": 101.7}

        ConnectionError: API недоступен
        ValueError: Некорректный JSON
        KeyError: Нет ключа "Valute" или валюта не найдена
        TypeError: Курс валюты не число
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except RequestException as e:
        raise ConnectionError(f"API недоступен: {e}")

    # JSON , кидает ValueError при проблемах
    try:
        data = response.json()
    except ValueError as e:
        raise ValueError(f"Некорректный JSON: {e}")

    #  Проверка наличия ключа Valute кидает KeyError
    if "Valute" not in data:
        raise KeyError("Отсутствует ключ 'Valute' в ответе API")

    # Сбор курсов валют
    result = {}
    for code in currency_codes:
        # Проверка существования валюты кидает KeyError
        if code not in data["Valute"]:
            raise KeyError(f"Валюта '{code}' отсутствует в данных")

        # Получаем значение курса
        value = data["Valute"][code]["Value"]

        # Проверка, кидает TypeError если не число
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Курс валюты '{code}' имеет тип {type(value).__name__}, "
                f"ожидалось число"
            )

        result[code] = float(value)  # Приводим к float для единообразия

    return result


print(get_currencies(["USD", "EUR"]))


try:
    print(get_currencies(["XYZ"]))
except Exception as e:
    print(f"Исключение проброшено наружу: {e}")

    """Тест логирования в StringIO """

    import io

    # Создаем виртуальный "файл" в памяти
    stream = io.StringIO()


