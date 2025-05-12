import math
class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError('Знаменатель не может быть 0')

        sab = math.gcd(a, b)
        self.a = a // sab
        self.b = b // sab
        
    
    def __str__(self):
        if self.b == 1:
            return f'{self.a}'
        
        return f'{self.a}/{self.b}'
        
    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_a = self.a * other.b + self.b * other.a      
        new_b = self.b * other.b
        #szv = math.gcd(z, v)
        #z = z // szv
        #v = v // szv

        #if v == 1:
           # return f'{z}'
        
        #return f'{z}/{v}'
        return Fraction(new_a, new_b)
    
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.a == other.a and self.b == other.b


number1 = Fraction(2, 4)
number2 = Fraction(1, 5)

#print(number.__str__())
sum_number = number1 + number2
print(sum_number)
#print(number.__eq__())
