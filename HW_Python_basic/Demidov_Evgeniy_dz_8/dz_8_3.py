# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...


# @type_logger
# def calc_cube(x):
#    return x ** 3


# >>> a = calc_cube(5)
# 5: <class 'int'>


# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from pathlib import Path
from functools import wraps

def type_logger(func):
    func_name = func.__name__

    #маскировка декоратора type_logger
    @wraps(func)
    def wrapper(*args, **kwargs):
        file = Path(__file__).parent/'logger.txt'
        result = func(*args, **kwargs)

        with file.open('a') as fp:
            args_str = ', '.join(map(str, args))
            kwargs_str = ', '.join(map(lambda d: f'{d}={kwargs[d]}', kwargs))
            fp.write(f'func({args_str}, *, {kwargs_str}) => result = {result}\n')

        args_str_for_print = ', '.join(map(lambda a: f'{a}: {type(a)}', args))    
        print(f'{func_name}({args_str_for_print})')
        return result
    return wrapper

@type_logger
def calc(x,y, sec_name='Anonymous', for_what='test'):
    print(f'{sec_name} {for_what}')
    return x**y


print(f'Function\'s name {calc.__name__}')
print(f"result = {calc(10, 2, sec_name='Demidov', for_what='for solve quadratic equation')}")