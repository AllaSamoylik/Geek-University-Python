class OnlyNumbersError(Exception):
    def __init__(self, msg):
        self.msg = msg


only_numbers_list = []

while True:
    is_numb = input('Введите число: ')
    if is_numb == 'stop':
        break
    try:
        try:
            numb = float(is_numb)
        except ValueError as e:
            raise OnlyNumbersError('Это не число')
    except OnlyNumbersError as err:
        print(err)
    else:
        only_numbers_list.append(numb)

print(only_numbers_list)
