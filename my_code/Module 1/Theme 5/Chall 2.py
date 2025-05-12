secret_number = 9
while True:
    num = int(input('Угадай число(1-10): '))
    if num == secret_number:
        print('Поздравляю! Вы угадали!')
        break