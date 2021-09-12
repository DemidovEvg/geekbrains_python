input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

_num_el = 0
new_list = []
for current_el in input_list:
    try:
        int(current_el)
        if current_el[0] == '+' or current_el[0] == '-':
            sign = current_el[0]
            current_el = current_el[1:len(current_el)]
        else:
            sign = ''
        new_list.extend(['"', f'{sign}{current_el:0>2}', '"'])
    except ValueError:
        new_list.append(current_el)
print(new_list)

#Так как между скобками и числами нет пробелов, то просто объединить не получится,
#необходимо проанализировать список и создать список с пробелами в нужных местах
#а уже потом объединить новый список в необходимую строку
new_list_for_string = []
_num_el = 0
if len(input_list) > 1:
    new_list_for_string.append(input_list[_num_el])
    while _num_el + 1 < len(input_list):
        current_el = input_list[_num_el]
        next_el = input_list[_num_el + 1]
        try:
            int(current_el)
            if next_el == '"':
                new_list_for_string.extend([next_el])
            else:
                new_list_for_string.extend([' ', next_el])
        except ValueError:
            try:
                int(next_el)
                if current_el == '"':
                    new_list_for_string.extend([next_el])
                else:
                    new_list_for_string.extend([' ', next_el])

            except ValueError:
                new_list_for_string.extend([' ', next_el])
        _num_el += 1
output_string = ''.join(new_list_for_string).capitalize()

print(output_string)
