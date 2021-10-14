numbers = []

for i in range(1, 1001, 2):
    numbers.append(i ** 3)

begin = 0
last = 0
numbers_by_7 = []

for numb in range(len(numbers)):
    begin = numbers[numb]
    summ = 0
    while begin >= 10:
        last = begin % 10
        summ += last
        begin = begin // 10
    else:
        summ += begin

    if summ % 7 == 0:
        numbers_by_7.append(numbers[numb])

summ_total = 0

for i in range(len(numbers_by_7)):
    summ_total += numbers_by_7[i]
print(summ_total)

# Добавляем 17

numbers = []

for i in range(1, 1001, 2):
    numbers.append(i ** 3 + 17)

begin = 0
last = 0
numbers_by_7 = []

for numb in range(len(numbers)):
    begin = numbers[numb]
    summ = 0
    while begin >= 10:
        last = begin % 10
        summ += last
        begin = begin // 10
    else:
        summ += begin

    if summ % 7 == 0:
        numbers_by_7.append(numbers[numb])

summ_total = 0

for i in range(len(numbers_by_7)):
    summ_total += numbers_by_7[i]
print(summ_total)