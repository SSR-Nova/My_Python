#Конкатенация строк
#Создайте функцию concat_strings, которая принимает неограниченное количество именованных аргументов (**kwargs) 
# и объединяет все строковые значения в одну строку.

def concat_strings(**kwargs):
    my_list = []
    for value in kwargs.values():
        my_list.append(value)
    return ''.join(my_list)

print(concat_strings(a="Hello", b=" ", c="World"))

#Фильтр по типу данных
#Напишите функцию filter_by_type, которая принимает **kwargs и возвращает словарь, содержащий только элементы 
# с указанным типом (например, только int).
def filter_by_type(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, int):
            my_dict[key] = value
    print(my_dict)

filter_by_type(a=1, b="text", c=3.14, type_filter=int)


#Настройка персонажа
#Создайте функцию create_character, которая принимает **kwargs (например, name, health, weapon) 
#и возвращает словарь с параметрами персонажа. Если какие-то параметры не переданы, используйте значения по умолчанию.

def create_character(**kwargs):
    
    new_character = {'name':'Геркулес', 'health': '100', 'weapon' : 'меч'}
    for key, value in kwargs.items():
        new_character[key] = value
    
    return new_character

print(create_character(name="Артур", health=100))