from models import User, Currency, UserCurrency

#  создание объектов
user = User(1, "Тест")
print(f"User id: {user.id}")
print(f"User name: {user.name}")

currency = Currency(1, '840', 'USD', 'Доллар', 90.0, 1)
print(f"Currency id: {currency.id}")
print(f"Currency name: {currency.name}")

uc = UserCurrency(1, 1, 1)
print(f"UserCurrency id: {uc.id}")
print(f"UserCurrency user_id: {uc.user_id}")

#  список
users_list = [User(1, 'Алексей'), User(2, 'Мария')]
for u in users_list:
    print(f"User {u.id}: {u.name}")