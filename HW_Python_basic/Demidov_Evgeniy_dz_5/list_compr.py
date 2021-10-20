# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

from time import perf_counter
import random


src = []
for i in range(10*7):
    src.append(random.randint(0,500))

start1 = perf_counter()
result_1_way = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(f'time calculations is {(perf_counter() - start1)*1000} мс')
#print(result_1_way)

start2 = perf_counter()
result_2_way = [elem for elem_prev, elem in zip(src, src[1:]) if elem > elem_prev]
print(f'time calculations is {(perf_counter() - start2)*1000} мс')
#print(result_1_way)

