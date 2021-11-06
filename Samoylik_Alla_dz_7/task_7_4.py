import os


def statistics(dir_name):
    file_stat = {}
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            f_stat = os.stat(os.path.join(root, file))
            f_size = f_stat.st_size
            up_bound = 10 ** len(str(f_size))
            if up_bound in file_stat:
                file_stat[up_bound] += 1
            else:
                file_stat[up_bound] = 1

    sorted_file_stat = dict(sorted(file_stat.items()))
    print(sorted_file_stat)


statistics(input(f'Введите имя папки для получения статистики: '))
