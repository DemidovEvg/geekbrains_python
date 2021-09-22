#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ///ключи — ФИО//, //значения — данные о хобби//. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович

# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи


# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
import os
import sys

# Задание номер 3
def create_dict_fio_hobby(*, users_file_name = 'users.csv', hobby_file_name = 'hobby.csv'):
    user_hobby_dict = dict()
    with open(users_file_name, 'r', encoding='utf-8') as users_f:
        with open(hobby_file_name, 'r', encoding='utf-8') as hobby_f:
            for line in users_f:
                user = line.rstrip()
                hobby = hobby_f.readline().rstrip()
                if user != '' and hobby != '':
                    user_hobby_dict[user] = hobby
                elif user != '' and hobby == '':
                    user_hobby_dict[user] = None
                elif user == '' and hobby != '':
                    return 1

# Задание номер 4
def create_file_fio_hobby(*, users_file_name = 'users.csv', hobby_file_name = 'hobby.csv', result_file_name = 'result_ex_3_and_4.txt'):
    user_hobby_dict = dict()

    if os.path.isfile(result_file_name):
        os.remove(result_file_name)
    is_need_write_one_in_file = False
    with open(users_file_name, 'r', encoding='utf-8') as users_f:
        with open(hobby_file_name, 'r', encoding='utf-8') as hobby_f:
            with open(result_file_name, 'a', encoding='utf-8') as result_f:
                for line in users_f:
                    user = line.rstrip()
                    hobby = hobby_f.readline().rstrip()
                    if user != '' and hobby != '':
                        result_f.write(f'{user}: {hobby}\n')
                    elif user != '' and hobby == '':
                        result_f.write(f'{user}: None\n')
                    elif user == '' and hobby != '':
                       is_need_write_one_in_file = True

    if is_need_write_one_in_file:
         with open(result_file_name, 'w', encoding='utf-8') as result_f:
             result_f.write('1')
                
    return user_hobby_dict

def get_input_y_or_n(promt):
    user_input = ''
    while (user_input.upper() != 'Y' and 
            user_input.upper() != 'N' and 
            user_input.upper() != 'EXIT'):
        user_input = input(promt)
    return user_input.upper()  

# Задание номер 5
if len(sys.argv) >= 4:
    create_file_fio_hobby(users_file_name = sys.argv[1], hobby_file_name = sys.argv[2], result_file_name = sys.argv[3])
elif len(sys.argv) <= 3:
    arg_dict = dict()
    print('Need arguments: <file name with users name> <file name with users hobby> <file name with result>')
    user_input = get_input_y_or_n('Use standard name for rest files? Y or N or EXIT: ')
    if user_input == 'Y':
        arg_names = ['path', 'users_file_name', 'hobby_file_name', 'result_file_name']
        if len(sys.argv) == 1:
            create_file_fio_hobby()
        elif len(sys.argv) == 2:
            create_file_fio_hobby(users_file_name = sys.argv[1])
        elif len(sys.argv) == 3:
            create_file_fio_hobby(users_file_name = sys.argv[1], hobby_file_name = sys.argv[2])
        print('Done')
    else:
        print('Restart sripts with right arguments: <file name with users name> <file name with users hobby> <file name with result>')
        print('Еhe program was interrupted ')


