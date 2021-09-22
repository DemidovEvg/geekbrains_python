# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1


# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import argparse
from pathlib import Path


def push(path_file, data):
    with path_file.open("a", encoding='utf-8') as f:
        f.write(str(data) + '\n')


def correct(path_file, data, num_row):
    cur_line_num = 1
    is_find_row = False
    path_file_tmp = Path(str(path_file).replace('.csv', '') + '_tmp.csv')
    with path_file.open("r", encoding='utf-8') as f_out: 
        with path_file_tmp.open("a", encoding='utf-8') as f_in: 
            line = f_out.readline()
            while line:
                if cur_line_num == num_row:
                    f_in.write(str(data) + '\n')
                    is_find_row = True
                else:
                    f_in.write(line)
                cur_line_num += 1
                line = f_out.readline()

    if  not is_find_row:
        path_file_tmp.unlink()
        raise ValueError('File has less row than input row')
    path_file.unlink()
    path_file_tmp.rename(path_file)
    
def pull(path_file, start, end):
    if start == None:
        start = 1
    elif end!= None and end < start:
        raise ValueError('Incorrect start [or | and] end')
    line_num = 1
    with path_file.open("r", encoding='utf-8') as f:  
        for line in f:
            if line_num >= start:
                print(line.strip())
            line_num += 1
            if end != None and end < line_num:
                break


parser = argparse.ArgumentParser(description='Sript for push and pull data for bakery sales')
subparser = parser.add_subparsers(help='sub-command [args | -h]', required=True)
parser_push = subparser.add_parser('push', help='[args | -h]', 
                                    description='Sub-command for push data to file')
parser_push.set_defaults(func=push)
parser_push.add_argument('-c', '--correct', metavar='num_row', type=int, help='Enter num row for correct data')
parser_push.add_argument('data', type=str, help='it is the sales in rub for save in file')
parser_pull = subparser.add_parser('pull', help='[args | -h]',
                                    description='Sub-command for pull data in rub from file')
parser_pull.set_defaults(func=pull)
parser_pull.add_argument('start', type=int, nargs='?',
                            help='optional parameter - start row for the pull')
parser_pull.add_argument('end', type=int, nargs='?',
                            help='optional parameter - end row for the pull')

user_input = parser.parse_args()

path_file = Path('bakery.csv')

if user_input.func == push:
    try:
        data = float(user_input.data.replace(',', '.'))
        if user_input.correct != None:
            correct(path_file, user_input.data, user_input.correct)
        else:
            push(path_file, user_input.data)
    except ValueError as e:
        print(e)
        print('Incorrect data')
elif user_input.func == pull:
    pull(path_file, user_input.start, user_input.end)

