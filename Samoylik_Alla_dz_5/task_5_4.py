import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Пробуем через List Comprehensions:
start = perf_counter()
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result)

print(f'Занимает в памяти - {sys.getsizeof(result)} байт')
print(f'Затрачивает {perf_counter() - start} секунд')
print('-' * 50)

# Пробуем через генератор:
start = perf_counter()
result_gen = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
result_gen_list = list(result_gen)[:len(src)]
print(result_gen_list)

print(f'Занимает в памяти - {sys.getsizeof(result_gen)} байт')
print(f'Затрачивает {perf_counter() - start} секунд')
print('-' * 50)
