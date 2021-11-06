import os


def make_dirs(dirpath, *dirnames):
    for dir in dirnames:
        dir_path = os.path.join(dirpath, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    dir_tree = os.listdir(dirpath)
    print(dirpath)
    for dir in dir_tree:
        print(f'-- {dir}')


make_dirs('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
