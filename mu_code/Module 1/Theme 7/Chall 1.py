#Создайте программу, которая:
#Запрашивает у пользователя список продуктов через запятую.
#Преобразует строку в список.
#Удаляет дубликаты (если есть).
#Сортирует список по алфавиту.
#Выводит итоговый список.

products = input('Введите продукты через запятую: ')
products_list = [p.strip() for p in products.split(',')]

products_set = set(products_list)
no_dubl_products_list = list(set(products_list))
no_dubl_products_list.sort()


print(no_dubl_products_list)