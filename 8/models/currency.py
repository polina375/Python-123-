class Currency:
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
        if isinstance(currency_id, int) and currency_id > 0:
            self.__id = currency_id
        else:
            raise ValueError('ID должен быть положительным целым числом')

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, code: str):
        if isinstance(code, str) and len(code) == 3 and code.isdigit():
            self.__num_code = code
        else:
            raise ValueError('Цифровой код должен быть строкой из 3 цифр')

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, code: str):
        if isinstance(code, str) and len(code) == 3:
            self.__char_code = code.upper()
        else:
            raise ValueError('Символьный код должен быть строкой из 3 символов')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Название должно быть строкой от 2 символов')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self.__value = float(value)
        else:
            raise ValueError('Курс должен быть положительным числом')

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: int):
        if isinstance(nominal, int) and nominal > 0:
            self.__nominal = nominal
        else:
            raise ValueError('Номинал должен быть положительным целым числом')