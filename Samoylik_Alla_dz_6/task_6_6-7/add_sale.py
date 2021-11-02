import sys

if len(sys.argv) == 1:
    print('Пожалуйста, введите сумму продажи')

else:
    price = ','.join(sys.argv[1:])
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        sum_line = sum(1 for line in f)
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{price}\n')
    print(f'Сумма продажи - {price} записана в систему под номером {sum_line + 1}')
