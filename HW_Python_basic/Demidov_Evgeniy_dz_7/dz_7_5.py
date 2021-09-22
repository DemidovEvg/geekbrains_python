# 5.	*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
from pathlib import Path
from collections import defaultdict
def get_ext(file):
    name = file.name
    ext = name.rsplit('.')
    return ext[-1]


def generate_key(size):
    if size == 0:
        return 0
    count = 10
    while True:
        if size <= count:
            return count
        else:
            count *= 10


path_to_folder = os.getcwd()
folder_obj = Path(path_to_folder)
dict_from_file = dict()

print(path_to_folder)
for cur_file in folder_obj.glob('**/*.*'):
    if cur_file.is_file():
        size = cur_file.stat().st_size   
        key = generate_key(size)
        ext = get_ext(cur_file)
        if key in dict_from_file:
            count_file = dict_from_file[key][0] + 1
            ext_list = dict_from_file[key][1]
            if ext not in ext_list:
                ext_list.append(ext)
        else:
            count_file = 0
            ext_list = [ext]

        dict_from_file[key] = (count_file, ext_list)

for key, val in sorted(dict_from_file.items(), key = lambda d: d[0]):
    print(f'{key}: {val}')
