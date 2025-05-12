seconds = int(input('Введите число секунд: '))
if seconds <= 60:
     print(f'{seconds} секунд')
elif seconds <= 3599:
     minuts = seconds // 60
     sec = seconds % 60
     print(f'{minuts} минут {sec} секунд')
elif seconds >= 3600:
     hours = seconds // 3600
     minuts = (seconds - hours * 3600) // 60
     sec = seconds % 60
     print(f'{hours} час {minuts} минута {sec} секунда')
