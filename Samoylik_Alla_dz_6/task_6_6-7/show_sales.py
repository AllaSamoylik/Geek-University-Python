import sys
from itertools import islice

if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read().strip())

if len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        sum_line = sum(1 for line in f)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if int(sys.argv[1]) <= sum_line:
            for line in islice(f, int(sys.argv[1]) - 1, None):
                print(line.replace('\n', ''))
        else:
            print('Номер записи, с которой осуществляется поиск, отсутствует в системе')


elif len(sys.argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        sum_line = sum(1 for line in f)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if int(sys.argv[1]) <= sum_line:
            if int(sys.argv[2]) <= sum_line:
                for line in islice(f, int(sys.argv[1]) - 1, int(sys.argv[2])):
                    print(line.replace('\n', ''))
            else:
                print('Номер записи, до которой осуществляется поиск, отсутствует в системе')
        else:
            print('Номер записи, с которой осуществляется поиск, отсутствует в системе')
