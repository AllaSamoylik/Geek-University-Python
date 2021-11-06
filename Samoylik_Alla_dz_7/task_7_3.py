import os
import shutil

os.chdir('my_project')

all_src = []
dirname = 'templates'
dst = os.path.join(os.getcwd(), dirname)

for root, dirs, files in os.walk(os.getcwd()):
    for dir in dirs:
        if dir == dirname:
            all_src.append(os.path.join(root, dir))

for src in all_src:
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        elif os.path.isfile(s):
            shutil.copy2(s, d)

os.chdir('..')
