def is_sum_digit_divisible_7(num):
    sum_digit = 0
    while num > 0:
        sum_digit += num % 10
        num //= 10
    return True if sum_digit % 7 == 0 else False


cub_lists = []

for num in range(1, 1001):
    if num % 2 == 0:
        cub_lists.append(num**3)

sum_num_divisible_7 = 0

sum_num_plus_17_and_divisible_7 = 0
_current_num_plus_17 = 0

for num in cub_lists:
    if is_sum_digit_divisible_7(num):
        sum_num_divisible_7 += num

    _current_num_plus_17 = num + 17
    if is_sum_digit_divisible_7(_current_num_plus_17):
       sum_num_plus_17_and_divisible_7 += _current_num_plus_17

print("The sum of number cube from 1 to 1000 which divisible by 7:", sum_num_divisible_7)
print("The sum of number cube from 1 to 1000 which add 17 and which divisible by 7:", sum_num_plus_17_and_divisible_7)

    

