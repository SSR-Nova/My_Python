class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка: (x={self.x}, y={self.y})'
    
point = Point(3,5)
print(point)