# 2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

import abc

class Clothes(abc.ABC):
    @abc.abstractmethod
    def tissue_consumption(self):
        pass
    

class Coat(Clothes):

    def __init__(self, *, size = 10):
        self.size = size

    def __setattr__(self, name: str, value) -> None:
        if name == 'size':
            if value > 0:
                self.__dict__[name] = value
            else:
                raise ValueError('Wrong size')
        else:
            self.__dict__[name] = value

    @property
    def tissue_consumption(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):

    def __init__(self, *, height = 22):
        self.height = height

    def __setattr__(self, name: str, value) -> None:
        if name == 'height':
            if value > 0:
                self.__dict__[name] = value
            else:
                raise ValueError('Wrong height')
        else:
            self.__dict__[name] = value

    @property
    def tissue_consumption(self):
        return self.height + 0.3

coat = Coat(size = 14)
suit = Suit(height = 36)
print(coat.tissue_consumption)
print(suit.tissue_consumption)