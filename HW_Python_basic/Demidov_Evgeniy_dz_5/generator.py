# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...



# def odd_nums(n):
#     for res_num in range(1, n+1, 2):
#         yield res_num

n = 15
odd_to_15 = (res_num for res_num in range(1, n+1, 2))


print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
