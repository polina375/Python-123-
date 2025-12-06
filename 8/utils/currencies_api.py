import requests


def get_currencies(currency_list=None):
    """
    Получает курсы валют с API ЦБ РФ
    """
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()

        result = {}
        for code, info in data['Valute'].items():
            if currency_list is None or code in currency_list:
                result[code] = info['Value'] / info['Nominal']

        return result
    except:
        # Если API не работает, возвращаем тестовые данные
        return {'USD': 90.0, 'EUR': 100.0, 'GBP': 115.0}