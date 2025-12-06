from .author import Author

class App():
    def __init__(self, name: str, version: str, author: Author):
        self.__name: str = name
        self.__version: str = version
        self.__author: Author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) is str and len(name) > 0:
            self.__name = name
        else:
            raise ValueError('Название должно быть непустой строкой')

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        if type(version) is str and len(version) > 0:
            self.__version = version
        else:
            raise ValueError('Версия должна быть непустой строкой')

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: Author):
        if type(author) is Author:
            self.__author = author
        else:
            raise TypeError('Автор должен быть объектом Author')