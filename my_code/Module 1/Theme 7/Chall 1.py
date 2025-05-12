<<<<<<< HEAD
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


=======
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


>>>>>>> d6adf397ce76f5063ab9da53365e45c33c9cf186
print(no_dubl_products_list)