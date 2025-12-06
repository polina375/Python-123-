from jinja2 import Environment, PackageLoader, select_autoescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from models import Author , App, User, Currency, UserCurrency
from utils.currencies_api import get_currencies


env = Environment(
    loader=PackageLoader("my app"),
    autoescape=select_autoescape()
)

# Создаем автора
main_author = Author('Полина', 'P3123')
app = App('Currency Tracker', '1.0', main_author)

# Навигация
navigation = [
    {'caption': 'Главная', 'href': '/'},
    {'caption': 'Валюты', 'href': '/currencies'},
    {'caption': 'Пользователи', 'href': '/users'},
    {'caption': 'Об авторе', 'href': '/author'},
]

# Создаем пользователей
users = [
    User(1, 'Алексей Петров'),
    User(2, 'Мария Ворфоломеева'),
    User(3, 'Дмитрий Иванов')
]
# Создаем валюты
currencies = [
    Currency(1, '840', 'USD', 'Доллар США', 90.5, 1),
    Currency(2, '978', 'EUR', 'Евро', 98.2, 1),
    Currency(3, '826', 'GBP', 'Фунт стерлингов', 115.3, 1)
]
# Создаем подписки
user_currencies = [
    UserCurrency(1, 1, 1),  # Алексей → USD
    UserCurrency(2, 1, 2),  # Алексей → EUR
    UserCurrency(3, 2, 2),  # Мария → EUR
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]  # Убираем параметры

        if path == '/':
            # Главная страница
            template = env.get_template("index.html")
            html = template.render(
                myapp="Currency Tracker",
                author_name=main_author.name,
                group=main_author.group,
                navigation=navigation,
                a_variable=f"Версия {app.version}"
            )


        elif path == '/currencies':
            # Получаем реальные курсы
            rates = get_currencies(['USD', 'EUR', 'GBP'])
            # Обновляем курсы
            for currency in currencies:
                if currency.char_code in rates:
                    currency.value = rates[currency.char_code]
            template = env.get_template("currencies.html")
            html = template.render(
                myapp=app.name,
                author_name=main_author.name,
                group=main_author.group,
                navigation=navigation,
                currencies=currencies

            )


        elif path == '/users':
            template = env.get_template("users.html")
            html = template.render(
                myapp="Currency Tracker",
                author_name=main_author.name,
                group=main_author.group,
                navigation=navigation,
                users=users
            )
        elif path == '/user':
            query = self.path.split('?')[1] if '?' in self.path else ''
            params = parse_qs(query)
            user_id = params.get('id', [''])[0]

            # Находим пользователя
            user = None
            if user_id:
                for u in users:
                    if str(u.id) == user_id:
                        user = u
                        break

            subscribed_currencies = []
            if user:
                for uc in user_currencies:
                    if uc.user_id == user.id:
                        for c in currencies:
                            if c.id == uc.currency_id:
                                subscribed_currencies.append(c)
                                break

            template = env.get_template("user.html")
            html = template.render(
                myapp="Currency Tracker",
                author_name=main_author.name,
                group=main_author.group,
                navigation=navigation,
                user=user,
                subscribed_currencies = subscribed_currencies
            )

        else:

            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes("Страница не найдена", "utf-8"))
            return


        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))



httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print('Сервер запущен на http://localhost:8080')
httpd.serve_forever()