class Car:

    brand = 'Unknown'

    def __init__(self, model):
        self.model = model

    @classmethod
    def set_brand(cls, new_brand):
        cls.brand = new_brand
    
    @classmethod
    def from_dict(cls, car_data):
        return cls(model = car_data['model'])
    

Car.set_brand("BMW")
car1 = Car("X5")
car2 = Car.from_dict({"model": "M3"})

print(car1.brand, car1.model) 
print(car2.brand, car2.model)