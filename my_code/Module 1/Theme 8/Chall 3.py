import json
product = input('Введите список покупок: ').split(',')
dict_product = {}
dict_product['items'] = product
with open('shopping_list.json', 'w') as file:
    json.dump(dict_product, file, indent=4, ensure_ascii=False)

with open('shopping_list.json', 'r') as file:
    shopping = json.load(file)
    print(shopping)

