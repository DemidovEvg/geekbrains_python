
class Sale:
    def __init__(self, val, currency):
        self.__val = val
        self.__currency = currency

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, val):
        self.__val = val
        return self.__val

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    def __str__(self):
        return f'{self.__val} {self.__currency}'
    
min_sale = Sale(100000, 'rub')           

print(min_sale)