


class Currency:


    def __init__(self, num_code: str, char_code: str, name: str, value: float, nominal: int, id: int = None):
        """
        Инициализирует объект Currency.

        num_code: Цифровой код валюты char_code: Символьный код валюты name: Название валюты value: Курс валюты nominal: Номинал валюты id: Уникальный идентификатор
        """
        self.__id = id
        self.__num_code = num_code
        self.__name = name
        self.__nominal = nominal

        # Используем сеттеры для валидации
        self.char_code = char_code
        self.value = value

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор валюты"""
        return self.__id

    @id.setter
    def id(self, val: int) -> None:
        """Устанавливает уникальный идентификатор валюты"""
        self.__id = val

    @property
    def num_code(self) -> str:
        """Возвращает цифровой код валюты"""
        return self.__num_code

    @property
    def char_code(self) -> str:
        """Возвращает символьный код валюты"""
        return self.__char_code

    @char_code.setter
    def char_code(self, val: str) -> None:
        """Устанавливает символьный код валюты

       val: Символьный код (должен состоять из 3 символов)

         ValueError: Если код не состоит из 3 символов
        """
        if len(val) != 3:
            raise ValueError("Код валюты должен состоять из 3 символов")
        self.__char_code = val.upper()

    @property
    def name(self) -> str:
        """Возвращает название валюты."""
        return self.__name

    @property
    def value(self) -> float:
        """Возвращает курс валюты"""
        return self.__value

    @value.setter
    def value(self, val: float) -> None:
        """Устанавливает курс валюты с валидацией   Курс валюты (должен быть >= 0)
             ValueError: Если курс отрицательный
        """
        if val < 0:
            raise ValueError("Курс валюты не может быть отрицательным")
        self.__value = val

    @property
    def nominal(self) -> int:
        """Возвращает номинал валюты"""
        return self.__nominal

    def to_dict(self) -> dict:
        """Преобразует объект в словарь
 dict: Словарь с данными валюты
        """
        return {
            "id": self.__id,
            "num_code": self.__num_code,
            "char_code": self.__char_code,
            "name": self.__name,
            "value": self.__value,
            "nominal": self.__nominal
        }

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        return (f"Currency(id={self.__id}, num_code='{self.__num_code}', "
                f"char_code='{self.__char_code}', name='{self.__name}', "
                f"value={self.__value}, nominal={self.__nominal})")