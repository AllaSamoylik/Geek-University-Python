for i in range(1,101):
    if i == 1 or (i % 10 == 1 and i != 11):
        print(f'{i} процент')
    elif 2 <= i <= 4 or (i % 10 == 2 and i != 12) or (i % 10 == 3 and i != 13) or (i % 10 == 4 and i != 14):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')