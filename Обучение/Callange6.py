class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f'Площадь прямоугольника: {self.width * self.height}'
    
    def perimetr(self):
        return f'Периметр прямоугольника: {2 * (self.width + self.height)}'


recta = Rectangle(10, 12)
print(recta.area())
print(recta.perimetr())