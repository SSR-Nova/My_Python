<<<<<<< HEAD
second = int(input('Введите количество секунд: '))
hour = second // 3600
min = (second - hour * 3600) // 60
sec = ((second - hour * 3600)- (min * 60))
=======
second = int(input('Введите количество секунд: '))
hour = second // 3600
min = (second - hour * 3600) // 60
sec = ((second - hour * 3600)- (min * 60))
>>>>>>> d6adf397ce76f5063ab9da53365e45c33c9cf186
print(f'{hour}:{min}:{sec}')