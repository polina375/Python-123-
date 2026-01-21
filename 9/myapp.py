"""основная часть приложения """

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader,PackageLoader,  select_autoescape

from models.author import Author
from controllers.databasecontroller import DatabaseController, CurrencyRatesCRUD, UserCRUD
from controllers.currencycontroller import CurrencyController

main_author = Author("Полина", "P3123")

# БД и контроллеров
db_controller = DatabaseController()
currency_crud = CurrencyRatesCRUD(db_controller)
user_crud = UserCRUD(db_controller)
currency_controller = CurrencyController(currency_crud)


env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)


template = env.get_template("index.html")


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Обработчик запросов."""

    def do_GET(self):


        url = urlparse(self.path)
        path = url.path
        params = parse_qs(url.query)

        # Устанавливаем заголовки
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        # Переменная для ответа
        html_content = ""


        """ Главная страница"""
        if path == '/':
            currencies = currency_controller.list_currencies()
            users = user_crud._read()

            template = env.get_template('index.html')
            html_content = template.render(
                myapp="Currency Tracker",
                navigation=[
                    {'caption': 'Главная', 'href': '/'},
                    {'caption': 'Об авторе', 'href': '/author'},
                    {'caption': 'Пользователи', 'href': '/users'},
                    {'caption': 'Валюты', 'href': '/currencies'}
                ],
                author_name=main_author.name,
                author_group=main_author.group,
                currencies=currencies,
                users=users
            )

        #  Информация об авторе
        elif path == '/author':
            template = env.get_template('author.html')
            html_content = template.render(
                author_name=main_author.name,
                author_group=main_author.group
            )

        # Список пользователей
        elif path == '/users':
            users = user_crud._read()
            template = env.get_template('user.html')
            html_content = template.render(
                users=users
            )

            """Просмотр одного пользователя"""
        elif path == '/user':
            if 'id' in params and params['id'][0].isdigit():
                user_id = int(params['id'][0])
                users = user_crud._read(user_id)
                if users:
                    user = users[0]
                    user_currencies = user_crud.get_user_currencies(user_id)
                    template = env.get_template('user.html')
                    html_content = template.render(
                        user=user,
                        currencies=user_currencies
                    )
                else:
                    html_content = "Пользователь не найден"
            else:
                html_content = "Не указан ID пользователя"

            """ Список всех валют"""
        elif path == '/currencies':
            currencies = currency_controller.list_currencies()
            template = env.get_template('currencies.html')
            html_content = template.render(
                currencies=currencies
            )

            """Удаление валюты"""
        elif path == '/currency/delete':
            if 'id' in params and params['id'][0].isdigit():
                currency_id = int(params['id'][0])
                currency_controller.delete_currency(currency_id)
                """Перенаправляем на список валют"""
                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return

        #  Обновление курса валюты
        elif path == '/currency/update':
            for key, value in params.items():
                if key.upper() in ['USD', 'EUR', 'GBP', 'AUD', 'RUB']:
                    try:
                        new_value = float(value[0])
                        currency_controller.update_currency(key.upper(), new_value)
                    except ValueError:
                        pass
            html_content = "Курс обновлен. <a href='/'>На главную</a>"

        #  Вывод валют в консоль
        elif path == '/currency/show':
            currency_controller.show_currencies_in_console()
            html_content = "Данные выведены в консоль. <a href='/'>На главную</a>"

        #  Не найдено
        else:
            html_content = "Страница не найдена"

        #  Отправляем ответ
        self.wfile.write(html_content.encode('utf-8'))


if __name__ == "__main__":
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Сервер остановлен")
        db_controller.close()