init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Обработка списка
i = 0
while i < len(init_list):
    if init_list[i].isdigit():
        init_list[i] = init_list[i].zfill(2)
        init_list.insert((i + 1), '"')
        init_list.insert(i, '"')
        i += 2
    elif init_list[i].find('+') != -1:
        if init_list[i][1:].isdigit():
            init_list[i] = '+' + init_list[i][1:].zfill(2)
            init_list.insert((i + 1), '"')
            init_list.insert(i, '"')
            i += 2
    else:
        i += 1
print(init_list)

# В красивую строку
i = 0
while i < len(init_list):
    if init_list[i] == '"':
        init_list[i:(i+3)] = [''.join(init_list[i:(i+3)])]
    else:
        i += 1
print(' '. join(init_list))
