class Vehicle:
    def __init__(self,brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def info(self):
        return f'{self.brand}, макс. скорость: {self.max_speed} км/ч'

class Car(Vehicle):
    def __init__(self, brand, max_speed, num_doors):
        super().__init__(brand, max_speed)
        self.num_doors = num_doors

    def info(self):
        parent_info = super().info()
        return f'{parent_info}, дверей: {self.num_doors}'

def print_vehicle_info(vehicle):
    return vehicle.info()


vehicle = Vehicle("BMW", 250)
car = Car("Audi", 240, 5)

print(print_vehicle_info(vehicle))  
print(print_vehicle_info(car))