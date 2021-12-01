import time
import psutil


def fib(num: int):
    result = {}
    def inner(num):
        if num == 0:
            raise ValueError
        elif num == 1:
            result[num] = 1
        elif num == 2:
            result[num] = 1
            return fib(num - 1)
        else:
            last_el = result[num - 1] if num in result else fib(num - 1)[num - 1]
            last_el_previous = result[num - 2] if num in result else fib(num-2)[num-2]
            result[num] = last_el + last_el_previous
    inner(num)
    return result

# 1 1 2 3 5
start = time.perf_counter()
print(fib(10))
print(f'Time execution : {time.perf_counter() - start}')

# Python program to print Fibonacci series
def fib2(delta:'int', output:'list'=[])-> 'list':
    if delta == 0:
        return output
    else:
        if len(output)< 2:
            output.append(1)
            fib2(delta-1, output)
        else:
            last = output[-1]
            second_last = output[-2]
            output.append(last + second_last)
            fib2(delta-1, output)
        return output

start = time.perf_counter()
print(fib2(10))
print(f'Time execution2 : {time.perf_counter() - start}')

def fib3(num):
    output = []
    if type(num) != int:
        raise TypeError
    elif num <=0:
        raise ValueError  
    elif num == 1:
        output.append(1)
        return output
    elif num == 2:
        output.append(1)
        return output
    else:
        output.extend([1, 1])
        for i in range(3, num + 1):
            output.append(output[-1] + output[-2])
        return output

start = time.perf_counter()
print(fib3(10))
print(f'Time execution3 : {time.perf_counter() - start}')


def fib4(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

start = time.perf_counter()
print(fib4(10))
print(f'Time execution4 : {time.perf_counter() - start}') 

start = time.perf_counter()

def fib_memo(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed)
    return computed[n]

print(fib_memo(10))
print(f'Time execution fib_memo : {time.perf_counter() - start}') 


start = time.perf_counter()
def fib_local(n):
    computed = {0: 0, 1: 1}
    def fib_inner(n):
        if n not in computed:
            computed[n] = fib_inner(n-1) + fib_inner(n-2)
        return computed[n]
    f = fib_inner(n)
    print(computed)
    return f

print(fib_local(10))
print(f'Time execution fib_local : {time.perf_counter() - start}') 