class ZeroError(Exception):
    def __init__(self, msg):
        self.msg = msg


dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))

try:
    if divisor == 0:
        raise ZeroError('Деление на 0 невозможно!')
except ZeroError as err:
    print(err)
else:
    print(f'{dividend} / {divisor} = {round(dividend / divisor, 2)}')
