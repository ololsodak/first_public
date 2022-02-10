# 16.9.1- 16.9.2
# Создадим конструктор, который будет описывать прямоугольник с имеющимися характеристиками: ширина и высота
class Rectangle:
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x # координаты по оси X
        self.y = y # координаты по оси Y
    
    # метод выводит ширину и длину
    def get_atribute(self):
        return f'Прямоугольник со сторонами a = {self.a}, b = {self.b}'
                
    # метод вывлодит координаты прямоугольника    
    def get_coordinate(self):
        return f'Кординваты: X = {self.x}, Y = {self.y}'
        
    # метод нахождения площади
    def get_area(self):
        return self.a*self.b
        
rect_1 = Rectangle(4,3,0,0)
print(rect_1.get_atribute())