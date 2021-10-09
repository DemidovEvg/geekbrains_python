# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class OfficeEquipment:
    def __init__(self, price, weight, length, height, width, color, 
                                                num_list_in_minut):
        self.attr = {}
        self.attr['price'] = price
        self.attr['weight'] = weight
        self.attr['length'] = length
        self.attr['height'] = height
        self.attr['width'] = width
        self.attr['color'] = color
        self.attr['num_list_in_minut'] = num_list_in_minut  
    
    def get_type_for_equipment(self):
        return 'Other office equipment'

    def __str__(self):
        return str(self.attr)

class Printer(OfficeEquipment):
    def __init__(self,* , price, weight, length, height, width, color, 
                 num_list_in_minut, toner_mark, tray_capacity):
        super().__init__(price, weight, length, height, width, color, 
                         num_list_in_minut)
        self.attr['toner_mark'] = toner_mark
        self.attr['tray_capacity'] = tray_capacity

    def get_type_for_equipment(self):
        return 'Принтер'

class Scanner(OfficeEquipment):
    def __init__(self, *, price, weight, length, height, width, color, 
                num_list_in_minut, scan_to: list, two_sided_scann = False):
        super().__init__(price, weight, length, height, width, color, 
                        num_list_in_minut)
        self.attr['scan_to'] = scan_to
        self.attr['two_sided_scann'] = two_sided_scann

    def get_type_for_equipment(self):
        return 'Сканер'

class Copier(OfficeEquipment):
    def __init__(self, *, price, weight, length, height, width, color, 
                num_list_in_minut, copies_per_minute, 
                up_to_letter_size = False):
        super().__init__(price, weight, length, height, width, color,
                         num_list_in_minut)
        self.attr['copies_per_minute'] = copies_per_minute
        self.attr['up_to_letter_size'] = up_to_letter_size

    def get_type_for_equipment(self):
        return 'Копир'
    

class OfficeEquipmentWarehouse:
    def __init__(self):
        self.office_equipment = {}
        self.count = 0

    def get_id(self):
        _count = self.count
        self.count += 1
        return _count

    def put_in_the_warehouse(self, *office_equipments: OfficeEquipment):
        for eq in office_equipments:
            self.office_equipment[self.get_id()] = eq
    
    def revision(self):
        for eq_key, eq_val in self.office_equipment.items():
            print(f'id({eq_key}):---'
                    f'{self.office_equipment[eq_key].get_type_for_equipment()}'
                    f'---{eq_val}')
    
    def get(self, type_eq=str, number=1):
        if not isinstance(number, int):
            raise TypeError("number isn't int")
        elif number < 1:
            raise ValueError("number less than 1")
        result_dict = {}
        pretty_type_eq = type_eq.capitalize()
        for eq_key in dict(self.office_equipment):
            if self.office_equipment[eq_key]\
                        .get_type_for_equipment() == pretty_type_eq:
                result_dict[f'id({eq_key})---{pretty_type_eq}'
                                        ] = self.office_equipment.pop(eq_key)
                number -= 1
                if number == 0:
                    return result_dict


list_equipment = []
list_equipment.append(Printer(price=55, weight=10, length=1, height=1, width=1,
                     color='red',num_list_in_minut=50, toner_mark='upt10', 
                    tray_capacity=400))
list_equipment.append(Printer(price=35, weight=5, length=2, height=2, width=2,
                     color='blue',num_list_in_minut=35, toner_mark='upt33', 
                    tray_capacity=100))
list_equipment.append(Scanner(price=35, weight=5, length=2, height=2, width=2,
                     color='blue',num_list_in_minut=35, scan_to=['jpg, tif'], 
                     two_sided_scann=True))
list_equipment.append(Scanner(price=305, weight=5, length=2, height=2, width=2,
                     color='blue',num_list_in_minut=35, 
                     scan_to=['jpg, tif, png'], two_sided_scann=False))
list_equipment.append(Copier(price=305, weight=5, length=2, height=2, width=2,
                     color='blue',num_list_in_minut=35, copies_per_minute=100, 
                     up_to_letter_size=True))               

bookkeeping = {}


print(isinstance(list_equipment[0], Printer))

warehouse = OfficeEquipmentWarehouse()

warehouse.put_in_the_warehouse(*list_equipment)
warehouse.revision()

bookkeeping.update(warehouse.get('сКанер', number = 0))

print('='*50)
print('В бухгалтерию выдали следующее оборудование:')
for key in bookkeeping:
    print(f'   {key}{bookkeeping[key]}')
print('='*50)

warehouse.revision()




