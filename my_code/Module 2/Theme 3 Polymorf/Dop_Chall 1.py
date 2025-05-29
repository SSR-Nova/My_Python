class Animal:
    def make_sound(self):
        return f'Some sound'
    
class Dog(Animal):
    def make_sound(self):
        return f'Woof!'
    
dog = Dog()
print(dog.make_sound())