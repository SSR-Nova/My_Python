second = int(input('Введите количество секунд: '))
hour = second // 3600
min = (second - hour * 3600) // 60
sec = ((second - hour * 3600)- (min * 60))
print(f'{hour}:{min}:{sec}')