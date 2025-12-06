class User:
    """Класс для представления пользователя"""

    def __init__(self, name: str, id: int = None):
        """
        Инициализирует объект User

            name: Имя пользователя
            id: Уникальный идентификатор
        """
        self.id = id
        self.name = name

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {
            "id": self.id,
            "name": self.name
        }