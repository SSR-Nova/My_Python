class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def total_cost(self):
        return self.price * self.quantity
        
         
    
    def __str__(self):
        return f'Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Итого: {self.total_cost()}'
    
product = Product('Телевизор', 50000, 2)
print(product)