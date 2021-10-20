# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.

class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNum(new_real, new_imag)
    
    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self
    
    def __mul__(self, other):
        new_real = self.real*other.real - self.imag*other.imag
        new_imag = self.real*other.imag + self.imag*other.real 
        return ComplexNum(new_real, new_imag)

    def __imul__(self, other):
        self.real = self.real*other.real - self.imag*other.imag
        self.imag = self.real*other.imag + self.imag*other.real
        return self

    def __str__(self):
        return f'{self.real}{self.imag:+d}i'

complex_num1 = ComplexNum(3,2)
complex_num2 = ComplexNum(3, 20)
complex_num1 += complex_num1
print(complex_num1)