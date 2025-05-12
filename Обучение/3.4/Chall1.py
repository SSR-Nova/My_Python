class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def __str__(self):
        avg = sum(self.grades) / len(self.grades)
        return f'Студент: {self.name} Средний балл: {avg}'

    def __repr__(self):
        return f'Student("{self.name}")'
    
    def __len__(self):
        return len(self.grades)

    def __add__(self, grade):
        
        self.grades.append(grade)
        
sergey = Student('Сергей')

sergey.__add__(5)
sergey.__add__(4)
sergey.__add__(3)
sergey + 5
sergey + 5
sergey + 2
print(len(sergey))
print(sergey.__str__())
print(repr(sergey))
