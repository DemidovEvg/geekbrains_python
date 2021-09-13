import utils
import sys


if __name__ == '__main__':
    program, *argv = sys.argv
    if not len(argv):
        print('Add currency code')
        
    else:
        current = argv[0]
        result, datetime_object = utils.current_rates(current, float)
        if result != None:
            print(f'Курс {current} равен {result:.4f}р /Дата ответа - {datetime_object}')
        else:
            print(f'None')
        