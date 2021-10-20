# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
 
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.


import time

class TrafficLight:

    def validate_decor(func):

        def validate_sequense(self, color):  
            self.validate_color(color)  
            list_with_correct_sequence = [('red', 'yellow'), ('yellow', 'green'), ('green', 'red')]
            current_sequense = (self.color, color)
            if current_sequense not in list_with_correct_sequence:
                raise ValueError('Wrong sequense!')
            result = func(self, color)
            return result
        return validate_sequense
    
    def validate_color(self, color):
        if color not in ['red', 'yellow', 'green']:
            raise ValueError('Wrong color!')

    def __init__(self, color):
        print(color)
        self.validate_color(color)
        self.color = color
        self._delay_light(color)

    @validate_decor
    def running(self, color):
        print(color)
        self.color = color
        self._delay_light(color)
      
    def _delay_light(self, color):
        if color == 'red':
            time.sleep(1)
        elif color == 'yellow':
            time.sleep(1)
        else:
            time.sleep(1)

light = TrafficLight('red')

light.running('yellow2')
light.running('green')
light.running('red')

