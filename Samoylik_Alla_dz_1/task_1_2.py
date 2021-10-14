numbers = []

for i in range(1, 1001, 2):
    numbers.append(i ** 3)

first = 0
last = 0
numbers_by_7 = []

for numb in range(len(numbers)):
    first = numbers[numb]
    sum_of_digits = 0
    while first >= 10:
        last = first % 10
        sum_of_digits += last
        first = first // 10
    else:
        sum_of_digits += first

    if sum_of_digits % 7 == 0:
        numbers_by_7.append(numbers[numb])

sum_total = 0

for i in range(len(numbers_by_7)):
    sum_total += numbers_by_7[i]
print(sum_total)

# Добавляем 17

numbers = []

for i in range(1, 1001, 2):
    numbers.append(i ** 3 + 17)

first = 0
last = 0
numbers_by_7 = []

for numb in range(len(numbers)):
    first = numbers[numb]
    sum_of_digits = 0
    while first >= 10:
        last = first % 10
        sum_of_digits += last
        first = first // 10
    else:
        sum_of_digits += first

    if sum_of_digits % 7 == 0:
        numbers_by_7.append(numbers[numb])

sum_total = 0

for i in range(len(numbers_by_7)):
    sum_total += numbers_by_7[i]
print(sum_total)
