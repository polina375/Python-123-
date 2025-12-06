class User():
    def __init__(self, user_id: int, name: str):
        self.__id: int = user_id
        self.__name: str = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, user_id: int):
        if type(user_id) is int and user_id > 0:
            self.__id = user_id
        else:
            raise ValueError('ID должен быть положительным целым числом')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) is str and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Имя должно быть строкой от 2 символов')