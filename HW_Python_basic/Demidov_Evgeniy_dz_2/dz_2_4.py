input_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for current_el in input_list:
    name_position = current_el.rfind(' ') + 1
    name = current_el[name_position:len(current_el)]
    name = name.capitalize()
    print(f'Привет, {name}!')