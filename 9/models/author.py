


class Author:
    """Класс для представления автора приложения."""

    def __init__(self, name: str, group: str):
        """
            name: Имя автора
            group: Группа автора
        """
        self.__name = name
        self.__group = group

    @property
    def name(self) -> str:
        """Возвращает имя автора"""
        return self.__name

    @property
    def group(self) -> str:
        """Возвращает группу автора"""
        return self.__group