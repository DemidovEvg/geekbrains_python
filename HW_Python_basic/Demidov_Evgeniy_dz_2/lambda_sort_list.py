def price(str_price) -> str:
    # print(str_price)
    list_price = str_price.split(' ')
    rub_penny = int(list_price[0]) + int(list_price[2])/100
    return rub_penny


input_list = [57.8, 55, 1, 45.3, 10.04, 15,
    44.55, 100, 200, 200.60, 33, 15, 17, 19, 20]

output_list = []

for current_price in input_list:
    rub = int(current_price)
    penny = round((current_price - rub) * 100)
    output_list.append(f'{rub} руб {penny:0>2} коп')

print('*'*100)
print(output_list)
print(f'{"id списка перед сортировкой:": <45} {id(output_list)}',)
print('='*100)
output_list.sort(key = lambda a: price(a))
print(output_list)
print(f'{"id списка после сортировки по возрастанию:": <45} {id(output_list)}',)
print('='*100)
output_list.sort(key = lambda a: price(a), reverse=True)
print(output_list)
print(f'{"id списка после сортировки по убыванию:": <45} {id(output_list)}',)
print('='*100)
# А почему так не работает, выдает None? _max_five = (output_list[0:5]).sort(key = lambda a: price(a))
_max_five = output_list[0:5]
_max_five.sort(key = lambda a: price(a))
print(f'Максимальные пять цен, отсортированные по возрастанию: {_max_five}')

