class Store:
    def __init__(self, items = {}):
        self.items = items

    def add_item(self, name, price):
        self.name = name
        self.price = price
        
        self.items[self.name] = price
        print(f'Товар: {name} добавлен!')

    def remove_item(self, name):
         
        if self.items[self.name] in self.items:
            del self.items[name]
            print(f'Товар: {name} удален!')

        return f'Данного товара нет в списке'
    
    def get_total_price(self):
        total_price = 0
        for value in self.items.values():
            total_price += value

        return f'Общая стоимость товаров: {total_price}'
    


store = Store()
store.add_item('Яблоки', 150)
store.add_item('Хлеб', 50)
print(store.get_total_price())  # 200
store.remove_item("Хлеб")
print(store.get_total_price())  # 150