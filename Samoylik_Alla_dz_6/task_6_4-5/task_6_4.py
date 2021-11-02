import os
import sys
import pickle

if len(sys.argv) != 4:
    print('Пожалуйста, укажите относительные пути к двум исходным и выходному файлам')
    # Можно взять тут :) --> users.csv hobby.csv users_hobby_2.pickle
else:
    with open(os.path.abspath(sys.argv[1]), 'r', encoding='utf-8') as f_users:
        with open(os.path.abspath(sys.argv[2]), 'r', encoding='utf-8') as f_hobby:
            with open(os.path.abspath(sys.argv[3]), 'wb') as f_sum:
                while True:
                    line_first = f_users.readline()
                    line_second = f_hobby.readline()
                    if not (line_first or line_second):
                        break
                    # Делаем кортежи, обоснование: список нельзя в ключ, словарь бесполезен - больше двух элементов,
                    # множество выбросит одинаковые элементы, если будут
                    if line_first != '':
                        line_first_1 = tuple(item for item in line_first.strip().split(','))
                    else:
                        print('1')
                        break
                    line_second_2 = None if line_second == '' else tuple(
                        item for item in line_second.strip().split(','))
                    users_hobby = {line_first_1: line_second_2}
                    pickle.dump(users_hobby, f_sum)

    with open(os.path.abspath(sys.argv[3]), "rb") as f_sum:
        while True:
            try:
                users_hobby = pickle.load(f_sum)
                print(users_hobby)
            except EOFError:
                break
