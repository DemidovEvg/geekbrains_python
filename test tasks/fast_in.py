import time
import numpy as np

def time_counter(*, rep = 1):
    def time_counter_inner1(func):
        def time_counter_inner2(*args, **kwargs):
            start = time.perf_counter()
            for i in range(rep):
                result = func(*args, **kwargs)
            print(f'{func.__name__} time: '
                  f'{time.perf_counter() - start} with repetition {rep}') 
            return result
        return time_counter_inner2
    return  time_counter_inner1


@time_counter(rep = 10)
def first_solution(numbers):
    result_list = []
    for i, number in enumerate(numbers):
        number_is_in_tail = number in numbers[i+1:]
        result_list.append((i, number, number_is_in_tail)) 
    return result_list


@time_counter(rep = 10)  
def second_solution(numbers):
    result_list = []
    first_appear = {}
    numbers_reverse = list(reversed(numbers))
    size = len(numbers)
    for i, number in enumerate(numbers):
        if number not in first_appear:
            try:
                first_appear[number] = size - numbers_reverse.index(number) - 1
            except:
                first_appear[number] = None

        if first_appear[number] != None and i < first_appear[number]:
            number_is_in_tail = True
        else:
            number_is_in_tail = False
        result_list.append((i, number, number_is_in_tail))
    return result_list


numbers = list(np.random.randint(low = 1, high = 10, size = 10000))

print(first_solution(numbers)[100])
print(second_solution(numbers)[100])

