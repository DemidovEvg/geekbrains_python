# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os
from pathlib import Path
from collections import defaultdict

def generate_key(size):
    if size == 0:
        return 0
    count = 10
    while True:
        if size <= count:
            return count
        else:
            count *= 10


folder_obj = Path.cwd()
dict_from_file = defaultdict(int)
print(folder_obj)

for cur_file in folder_obj.glob('**/*.*'):
    size = cur_file.stat().st_size
    key = generate_key(size)
    dict_from_file[key] += 1

for key, val in sorted(dict_from_file.items(), key = lambda d: d[0]):
    print(f'{key}: {val}')

