"""
Контроллер для бизнес-логики работы с валютами.
"""

from typing import List, Dict
from controllers.databasecontroller import CurrencyRatesCRUD


class CurrencyController:
    """Управляет операциями с валютами"""

    def __init__(self, db_controller: CurrencyRatesCRUD):
        """ Контроллер валют"""
        self.db = db_controller

    def list_currencies(self) -> List[Dict]:
        """Возвращает список всех валют"""
        return self.db._read()

    def update_currency(self, char_code: str, value: float) -> bool:
        """Обновляет курс валюты"""
        return self.db._update({char_code: value})

    def delete_currency(self, currency_id: int) -> bool:
        """Удаляет валюту"""
        return self.db._delete(currency_id)

    def show_currencies_in_console(self):
        """Выводит валюты в консоль"""
        currencies = self.list_currencies()
        print("\n" + "=" * 70)
        print("ВАЛЮТЫ:")
        print("=" * 70)
        print(f"{'ID':<3} {'Код':<5} {'Название':<25} {'Курс':<10} {'Номинал':<8}")
        print("-" * 70)
        for curr in currencies:
            print(f"{curr['id']:<3} {curr['char_code']:<5} {curr['name']:<25} "
                  f"{curr['value']:<10} {curr['nominal']:<8}")
        print("=" * 70 + "\n")