# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки!')

class Pen(Stationery):
    def draw(self):
        print('I am signing the document')

class Pencil(Stationery):
    def draw(self):
        print('I am drawing a horse')


class Handle(Stationery):
    def draw(self):
        print('What I am doing here? I like open doors!')


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

for obj in (pen, pencil, handle):
    obj.draw()
