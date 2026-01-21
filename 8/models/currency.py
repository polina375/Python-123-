class Currency:
    """
       Класс представляет валюту в системе.

       Использует как модель (Model) в архитектуре MVC.
       Инкапсулирует данные о валюте и выполняет их валидацию
       через свойства (property).

       Arg:
           id (int): Уникальный идентификатор валюты.
           num_code (str): Числовой код валюты (3 цифры).
           char_code (str): Символьный код валюты (3 символа)
           name (str): Полное название валюты.
           value (float): Курс валюты.
           nominal (int): Номинал валюты.
       """
    def __init__(self, currency_id: int, num_code: str, char_code: str,
                 name: str, value: float, nominal: int):
        self.__id = currency_id
        self.__num_code = num_code
        self.__char_code = char_code
        self.__name = name
        self.__value = value
        self.__nominal = nominal

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, currency_id: int):
        #  Устанавливает идентификатор валюты.
        if isinstance(currency_id, int) and currency_id > 0:
            self.__id = currency_id
        else:
            raise ValueError('ID должен быть положительным целым числом')

    @property
    def num_code(self):
        #  Возвращает числовой код валюты
        return self.__num_code

    @num_code.setter
    def num_code(self, code: str):
        #  Устанавливает числовой код валюты
        if isinstance(code, str) and len(code) == 3 and code.isdigit():
            self.__num_code = code
        else:
            raise ValueError('Цифровой код должен быть строкой из 3 цифр')

    @property
    def char_code(self):
        #  Возвращает символьный код валюты
        return self.__char_code

    @char_code.setter
    def char_code(self, code: str):
        # Устанавливает символьный код валюты
        if isinstance(code, str) and len(code) == 3:
            self.__char_code = code.upper()
        else:
            raise ValueError('Символьный код должен быть строкой из 3 символов')

    @property
    def name(self):
        #  Возвращает название валюты
        return self.__name

    @name.setter
    def name(self, name: str):
        # Устанавливает название валюты
        if isinstance(name, str) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Название должно быть строкой от 2 символов')

    @property
    def value(self):
        #  Возвращает курс валюты
        return self.__value

    @value.setter
    def value(self, value: float):
        #     Устанавливает курс валюты.
        if isinstance(value, (int, float)) and value > 0:
            self.__value = float(value)
        else:
            raise ValueError('Курс должен быть положительным числом')

    @property
    def nominal(self):
        # Возвращает номинал валюты
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: int):
        #   Устанавливает номинал валюты
        if isinstance(nominal, int) and nominal > 0:
            self.__nominal = nominal
        else:
            raise ValueError('Номинал должен быть положительным целым числом')