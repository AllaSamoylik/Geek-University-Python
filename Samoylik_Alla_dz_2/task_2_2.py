init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

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

init_list[1:4] = [''.join(init_list[1:4])]
init_list[3:6] = [''.join(init_list[3:6])]
init_list[8:11] = [''.join(init_list[8:11])]

print(' '. join(init_list))
