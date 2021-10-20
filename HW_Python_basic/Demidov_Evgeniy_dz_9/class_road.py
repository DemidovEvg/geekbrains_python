# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
 
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self,*, length=1, width=1):
        self._length = length
        self._width = width
    
    def mass_of_asphalt(self,*, weight_square_meter=1, height=1):
        return (self._length * self._width * weight_square_meter * height/1000, 'тонны')


lenina_street = Road(length=5000, width=20)
print(lenina_street.mass_of_asphalt(weight_square_meter=25, height=5))
