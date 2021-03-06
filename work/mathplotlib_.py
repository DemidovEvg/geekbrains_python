import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math

def time_counter(*, rep = 1):
    def time_counter_inner1(func):
        def time_counter_inner2(*args, **kwargs):
            start = time.perf_counter()
            for i in range(rep):
                result = func(*args, **kwargs)
            print(f'{func.__name__} '
                  f'time: '
                  f'{time.perf_counter() - start} with repetition {rep}') 
            return result
        return time_counter_inner2
    return  time_counter_inner1

@time_counter(rep=1)
def foo(dd):
    return sorted(dd)




x = np.linspace(1, 10**5, 50)
y = [math.log(i,2) for i in x]

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
pass
