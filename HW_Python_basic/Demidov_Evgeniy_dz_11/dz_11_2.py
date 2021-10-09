# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

import argparse

parser = argparse.ArgumentParser(description='Sript for divide two number')
parser.add_argument('num1', type=int, help='num1')
parser.add_argument('num2', type=int, help='num1')
user_input = parser.parse_args()


class DemidovZeroDivisionError(Exception):
    def __init__(self, msg=''):
        self.txt = 'Demidov see what you want divide by zero ' + msg

try:
    if user_input.num2 == 0:
        raise DemidovZeroDivisionError()
except DemidovZeroDivisionError as e:
    print(e.txt)
else:
    print(user_input.num1 / user_input.num2)
