"""
Реализует CRUD-операции.
"""

import sqlite3
from typing import List, Dict, Optional


class DatabaseController:
    """Управляет соединением с БД"""

    def __init__(self, db_path: str = ":memory:"):
        """ Контроллер БД."""
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        """Создает таблицы в базе данных"""
        cursor = self.connection.cursor()

        # Таблица пользователей
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        # Таблица валют
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                num_code TEXT NOT NULL,
                char_code TEXT NOT NULL,
                name TEXT NOT NULL,
                value REAL,
                nominal INTEGER
            )
        """)

        # Таблица подписок
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_currency (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                currency_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES user(id),
                FOREIGN KEY(currency_id) REFERENCES currency(id)
            )
        """)

        self.connection.commit()
        self.add_test_data()

    def add_test_data(self):
        """Добавляет тестовые данные"""
        cursor = self.connection.cursor()

        # Проверяем, есть ли валюты
        cursor.execute("SELECT COUNT(*) FROM currency")
        if cursor.fetchone()[0] == 0:
            # Добавляем валюты
            data = [
                {"num_code": "840", "char_code": "USD", "name": "Доллар США", "value": 90.0, "nominal": 1},
                {"num_code": "978", "char_code": "EUR", "name": "Евро", "value": 91.0, "nominal": 1},
                {"num_code": "826", "char_code": "GBP", "name": "Фунт стерлингов", "value": 100.0, "nominal": 1},
                {"num_code": "036", "char_code": "AUD", "name": "Австралийский доллар", "value": 52.85, "nominal": 1}
            ]

            sql = """
                INSERT INTO currency(num_code, char_code, name, value, nominal)
                VALUES(?, ?, ?, ?, ?)
            """
            cursor.executemany(sql,data )

            # Добавляем пользователей
            users = ["Иван", "Мария", "Алексей"]
            for name in users:
                cursor.execute("INSERT INTO user(name) VALUES(?)", (name,))

            # Добавляем подписки
            cursor.execute("INSERT INTO user_currency(user_id, currency_id) VALUES(1, 1)")
            cursor.execute("INSERT INTO user_currency(user_id, currency_id) VALUES(1, 2)")
            cursor.execute("INSERT INTO user_currency(user_id, currency_id) VALUES(2, 3)")

            self.connection.commit()

    def close(self):
        """Закрывает соединение с БД"""
        if self.connection:
            self.connection.close()


class CurrencyRatesCRUD:
    """CRUD-операции для валют"""

    def __init__(self, db_controller: DatabaseController):

        self.db = db_controller

    def _create(self, currency_data: Dict) -> int:
        """Создает новую валюту"""

        sql = """
            INSERT INTO currency(num_code, char_code, name, value, nominal)
            VALUES(:num_code, :char_code, :name, :value, :nominal)
        """
        cursor = self.db.connection.cursor()
        cursor.execute(sql, currency_data)
        self.db.connection.commit()
        return cursor.lastrowid

    def _read(self, currency_id: Optional[int] = None) -> List[Dict]:
        """Читает валюты из БД"""
        cursor = self.db.connection.cursor()

        if currency_id:
            sql = "SELECT * FROM currency WHERE id = ?"
            cursor.execute(sql, (currency_id,))
        else:
            sql = "SELECT * FROM currency"
            cursor.execute(sql)

        return [dict(row) for row in cursor.fetchall()]

    def _update(self, currency_dict: Dict[str, float]) -> bool:
        """Обновляет курс валюты"""
        char_code = list(currency_dict.keys())[0]
        value = list(currency_dict.values())[0]

        sql = "UPDATE currency SET value = ? WHERE char_code = ?"
        cursor = self.db.connection.cursor()
        cursor.execute(sql, (value, char_code))
        self.db.connection.commit()
        return cursor.rowcount > 0

    def _delete(self, currency_id: int) -> bool:
        """Удаляет валюту"""

        sql1 = "DELETE FROM user_currency WHERE currency_id = ?"
        cursor = self.db.connection.cursor()
        cursor.execute(sql1, (currency_id,))


        sql2 = "DELETE FROM currency WHERE id = ?"
        cursor.execute(sql2, (currency_id,))
        self.db.connection.commit()
        return cursor.rowcount > 0


class UserCRUD:
    """CRUD-операции для пользователей"""

    def __init__(self, db_controller: DatabaseController):
        """CRUD для пользователей"""
        self.db = db_controller

    def _read(self, user_id: Optional[int] = None) -> List[Dict]:
        """Читает пользователей из БД"""
        cursor = self.db.connection.cursor()

        if user_id:
            sql = "SELECT * FROM user WHERE id = ?"
            cursor.execute(sql, (user_id,))
        else:
            sql = "SELECT * FROM user"
            cursor.execute(sql)

        return [dict(row) for row in cursor.fetchall()]

    def get_user_currencies(self, user_id: int) -> List[Dict]:
        """Получает валюты пользователя"""
        sql = """
            SELECT c.* FROM currency c
            JOIN user_currency uc ON c.id = uc.currency_id
            WHERE uc.user_id = ?
        """
        cursor = self.db.connection.cursor()
        cursor.execute(sql, (user_id,))
        return [dict(row) for row in cursor.fetchall()]