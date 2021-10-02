# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

Income = dict[tuple[str,int],tuple[str,int]]

class Worker:

    def __init__(self, name, surname, position, income: Income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
    
class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        sum = 0
        for _, val in self._income.items():
            sum += val
        return f'{sum}'

p = Position('Ivan', 'Petrov', 'Ingeneer', {'wage':10000, 'bonus': 5000})
print(p.get_full_name())
print(p.get_total_income())