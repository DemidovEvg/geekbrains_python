# 3.	Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод ///make_order()///, принимающий экземпляр класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.

class Cell:

    def __init__(self, number_of_partitions):
        if number_of_partitions < 1:
            raise ValueError('number_of_partitions is too small')
        self.number_of_partitions = int(number_of_partitions)

    def __add__(self, other):
        new_cell = Cell(self.number_of_partitions + other.number_of_partitions)
        return new_cell
    
    def __sub__(self, other):
        new_cell = Cell(self.number_of_partitions - other.number_of_partitions)
        return new_cell

    def __mul__(self, other):
        new_cell = Cell(self.number_of_partitions * other.number_of_partitions)
        return new_cell
    
    def __floordiv__(self, other):
        new_cell = Cell(self.number_of_partitions // other.number_of_partitions)
        return new_cell

    def __truediv__(self, other):
        new_cell = Cell(self.number_of_partitions / other.number_of_partitions)
        return new_cell

    def make_order(self, nums_in_row=5):
        rows = self.number_of_partitions // nums_in_row
        mod_last_row = self.number_of_partitions % nums_in_row
        result_list = []

        for i in range(rows):
            result_list.append('*' * nums_in_row + '\n')
        result_list.append('*' * mod_last_row + '\n')
    
        return ''.join(result_list)
    
c1 = Cell(31)
c2 = Cell(3)
c = c1 * c2
print(c.make_order(10))




