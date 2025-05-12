<<<<<<< HEAD
import string
import random

numbers = string.digits
letter = string.ascii_uppercase

alphanumeric = string.ascii_letters + string.digits

def generate_pass():
    

    while True:
        password = (random.choice(numbers)+random.choice(letter)+''.join(random.sample(alphanumeric, 6)))
        password = ''.join(password)    


        return password   
        

        
print(generate_pass())

=======
import string
import random

numbers = string.digits
letter = string.ascii_uppercase

alphanumeric = string.ascii_letters + string.digits

def generate_pass():
    

    while True:
        password = (random.choice(numbers)+random.choice(letter)+''.join(random.sample(alphanumeric, 6)))
        password = ''.join(password)    


        return password   
        

        
print(generate_pass())

>>>>>>> d6adf397ce76f5063ab9da53365e45c33c9cf186
