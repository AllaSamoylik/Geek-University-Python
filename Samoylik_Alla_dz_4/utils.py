from decimal import Decimal
from datetime import date
import requests
from bs4 import BeautifulSoup

month_dict = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sept': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


def currency_rates(currency):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    # Извлекаем дату
    date_split = response.headers['Date'].split()
    year = int(date_split[3])
    month = int(month_dict[date_split[2]])
    day = int(date_split[1])
    current_date = date(year, month, day)
    # Разбираем дом дерево на строки
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('valute')
    list_items = [str(i) for i in items]
    # Находим нужный курс
    for item in list_items:
        currency_found = item.find(currency.upper())
        if currency_found != -1:
            value = item.find('value')
            rate = item[value + 6:value + 13]
            rate_in_decimal = Decimal(rate.replace(',', '.'))
            print(f'Курс {currency.upper()} на {current_date} - {rate_in_decimal}')
        elif currency_found is None:
            return None


if __name__ == '__main__':
    currency_rates('USD')
    currency_rates('eur')
