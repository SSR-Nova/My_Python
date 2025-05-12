#Сумма произвольных чисел
#Напишите функцию sum_all, которая принимает любое количество чисел через *args и возвращает их сумму.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))

#Среднее значение
#Создайте функцию average, которая вычисляет среднее значение переданных чисел

def average(*args):
    mid_sum = sum(args) / len(args)
    return mid_sum

print(average(1, 2, 3))

#Максимальное и минимальное
#Напишите функцию min_max, которая возвращает кортеж (минимум, максимум) из всех переданных чисел.

def min_max(*args):
    return min(args), max(args)

print(min_max(10, 5, -3, 42))
