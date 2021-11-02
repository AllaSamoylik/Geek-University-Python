import sys

if len(sys.argv) < 3:
    if len(sys.argv) == 2:
        print('Пожалуйста, введите сумму продажи для редактирования')
    else:
        print('Пожалуйста, введите номер записи и сумму продажи для редактирования')

else:
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        sale_numb = int(sys.argv[1])
        price = ','.join(sys.argv[2:])
        sum_line = sum(1 for line in file)
        with open('bakery.csv', 'r+', encoding='utf-8') as f:
            if sale_numb <= sum_line:
                for i in range(1, sale_numb):
                    line = f.readline()
                    f.tell()
                f.seek(f.tell())
                f.write(f'{price}\n')
                print(f'Сумма продажи - {price} под номером {sale_numb} отредактирована в системе ')
            else:
                print('Номер записи, которая подлежит редактированию, отсутствует в системе')
