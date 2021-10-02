# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...


# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3


# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


# Примечание: сможете ли вы замаскировать работу декоратора?

import functools

def val_checker(func_check):
    def _val_checker(func):
        @functools.wraps(func)
        def wrapper(x):
            result = None
            if func_check(x):
                result = func(x)
            else:
                raise ValueError(f'wrong val {x}')
            return result
        return wrapper
    return _val_checker


@val_checker(lambda x: x>0)
def calc_cube(x):
    return x**3

print(calc_cube(-11))
print(calc_cube.__name__)

