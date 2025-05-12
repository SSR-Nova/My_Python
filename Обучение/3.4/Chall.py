class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name_item, quantity = 1):
        if name_item in self.items:
            self.items[name_item] += quantity
        else:
            self.items[name_item] = quantity
        print(f'{quantity} {name_item} добален(о) в корзину')
    def __add__(self, other):
        if isinstance(other, dict):
            for name_item, quantity in other.items():
                self.add_item(name_item, quantity)
            
        elif isinstance(other, str):
            self.add_item(other)

        return self
    def __str__(self):
        print(f'Корзина: ')
        for name_item, quantity in self.items.items():
            
            print(f'- {name_item}: {quantity} шт.')

    def __len__(self):
        count = 0
        for value in self.items.values():
            count += value
        return f'В корзине всего {count} товара(ов)'
    
    def __contains__(self, name_item):
        if name_item in self.items:
            print(f'{name_item} есть в корзине')
        else:
            print(f'{name_item} нет в корзине')

    

my_cart = ShoppingCart()

my_cart.add_item('яблоко', 3)
my_cart + {'банан' : 21}
my_cart + 'пивко'
my_cart.__str__()
print(my_cart.__len__())
my_cart.__contains__('пивко')
