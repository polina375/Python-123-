class UserCurrency():
    def __init__(self, uc_id: int, user_id: int, currency_id: int):
        self.__id: int = uc_id
        self.__user_id: int = user_id
        self.__currency_id: int = currency_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, uc_id: int):
        if type(uc_id) is int and uc_id > 0:
            self.__id = uc_id
        else:
            raise ValueError('ID должен быть положительным целым числом')

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int):
        if type(user_id) is int and user_id > 0:
            self.__user_id = user_id
        else:
            raise ValueError('ID пользователя должен быть положительным целым числом')

    @property
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, currency_id: int):
        if type(currency_id) is int and currency_id > 0:
            self.__currency_id = currency_id
        else:
            raise ValueError('ID валюты должен быть положительным целым числом')