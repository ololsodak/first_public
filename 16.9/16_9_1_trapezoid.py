# 16.9.2
# создадим класс геометрической фигуры Трапеция с аргументами:
# основания - a и b, высота - h
from rectangle import Rectangle

class Trapezoid(Rectangle):
    def __init__(self, a = 0, b = 0, h = 1, x = 0, y = 0):
        super().__init__(a, b, x ,y) # переопределяем аргументы родительского класса
        self.h = h # высота
        
    
    # метод расчета площади трапеции
    def get_area(self):
        return f'Площадь трапеции равна {round(((self.a+self.b)/2*self.h), 2)}'
    
    # переопределим родительский метод get_atribute
    def get_atribute(self):
        return f'Нижнее основании трапеции - {self.a}\nВерхнее основание трапеции - {self.b}\nВысота трапеции - {self.h}.'
                
trap_1 = Trapezoid()
trap_1.a = float(input('Введите нижние основание трапеции: '))
trap_1.b = float(input('Введите верхнее основание трапеции: '))
trap_1.h = float(input('Введите высроту трапеции: '))
trap_1.x = float(input('Введите координаты трапеции по оси X: '))
trap_1.y = float(input('Введите координаты трапеции по оси Y: '))

print('-----')
print(trap_1.get_atribute())
print(trap_1.get_coordinate())
print(trap_1.get_area())

