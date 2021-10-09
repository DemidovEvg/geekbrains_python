# 1.	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
# класса (метод __init__()), который должен принимать данные (список списков) 
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных 
# в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31	22
# 37	43
# 51	86
	
# 3	5	32
# 2	4	6
# -1	64	-8
	
# 3	5	8	3
# 8	3	7	1


# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы 
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов 
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент 
# первой строки первой матрицы складываем с первым элементом первой строки 
# второй матрицы и пр.


import copy


Matrix_type = list[list]

class Matrix:
    def __init__(self, matrix: Matrix_type):
        self.matrix = matrix

    def len_of_longest_element(self):
        len_of_l_e = 0
        for row in self.matrix:
            for el in row:
                current_len = len(str(el))
                if len_of_l_e < current_len:
                    len_of_l_e = current_len
        return len_of_l_e

    def __str__(self):
        _matrix_str = ''
        elements_container_size = self.len_of_longest_element() + 2
        for index, row in enumerate(self.matrix):
            line_break = '\n' if index < len(self.matrix)-1 else ''
            for el in row:
               _matrix_str += f'{el:<{elements_container_size}}'
            _matrix_str += line_break
        return _matrix_str

    def matrix_size(self):
        return [len(self.matrix[0]),len(self.matrix)]
        

    def __add__(self, other):
        if self.matrix_size() != other.matrix_size():
            raise Exception(f'Different sizes: {self.matrix_size()} and' 
                            f'{other.matrix_size()}')
        new_matrix = copy.deepcopy(self.matrix)
        for index_row, row in enumerate(new_matrix):
            for index_col, el in enumerate(row):
                new_matrix[index_row][index_col] += \
                                            other.matrix[index_row][index_col]
        return Matrix(new_matrix)
        

matrix_list1 = [
    [1000,2,3],
    [5,1,6]
]

matrix_list2 = [
    [1,2,-30],
    [5,1,60]
]


m1 = Matrix(matrix_list1)
m2 = Matrix(matrix_list2)

new_m = m1 + m2
print(new_m)

