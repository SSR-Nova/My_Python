class Vehicle:
    def __init__(self,brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, brand, max_speed, num_doors):
        super().__init__(brand, max_speed)
        self.num_doors = num_doors

car = Car('Toyota', 200, 4)
print(car.brand)
print(car.max_speed)
print(car.num_doors)