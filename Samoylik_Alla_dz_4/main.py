import sys
from utils import currency_rates

command = None

try:
    command = sys.argv[1]
except IndexError:
    print('Пожалуйста, введите команду')

if command == 'rate':
    try:
        currency = sys.argv[2]
    except IndexError:
        print('Введите название валюты')
    else:
        currency_rates(currency)
