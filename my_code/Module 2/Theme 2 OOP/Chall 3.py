class Student:
    def __init__(self, name, grades = None):
        self.name = name
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade):
        self.grades.append(grade)   
        
    
    def average_grade(self):
        sum_grade = 0
        for i in self.grades:
            sum_grade += i

        return f'Средняя оценка: {sum_grade / len(self.grades)}'
    
    def __str__(self):
        return f'Студент: {self.name}, {self.average_grade()}'


student = Student(name = 'Алексей')
student.add_grade(5)
student.add_grade(4)
print(student.average_grade()) 
print(student)
        