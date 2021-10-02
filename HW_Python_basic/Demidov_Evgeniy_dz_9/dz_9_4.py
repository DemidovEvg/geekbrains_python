# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
 
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print("car go")

    def stop(self):
        print('car stop')

    def turn(self, direction):
        print(f'car turn to {direction}')
    
    def show_speed(self):
        print(f'current speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed, please slow down')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed, please slow down')            

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


towncar = TownCar(70, 'black', 'polo', False)
workcar = WorkCar(20, 'grey', 'niva', False)
sportcar = SportCar(250, 'red', 'urus', False)
policecar = PoliceCar(60, 'pink', 'smart', True)

towncar.show_speed()
workcar.show_speed()
sportcar.show_speed()
policecar.show_speed()