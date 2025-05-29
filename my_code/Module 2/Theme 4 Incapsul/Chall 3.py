import math
class Circle:
    def __init__(self, __radius):
        self.__radius = __radius
    
    @property
    def area(self):
        pi = math.pi
        return pi * (self.__radius ** 2)
    

circle = Circle(5)
print(circle.area)