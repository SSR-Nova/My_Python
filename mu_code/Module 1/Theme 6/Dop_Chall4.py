#Квадраты чисел
#Напишите лямбда-функцию, которая принимает число и возвращает его квадрат.

numbers = [1, 2, 3, 4]
fun_lambda = list(map(lambda x:x*x, numbers))

print(fun_lambda)

#Фильтр чётных чисел
#Создайте лямбда-функцию для фильтрации чётных чисел из списка.

numbers = [5, 10, 15, 20]
fun_lambda = list(filter(lambda x:x % 2 == 0, numbers))

print(fun_lambda)


#Сортировка по последней букве
#Напишите лямбда-функцию, которая сортирует список слов по последней букве каждого слова.

fruit = ['яблоко', 'груша', 'апельсин']
sort_fruit = sorted(fruit, key=lambda x: x[::-1])

print(sort_fruit)