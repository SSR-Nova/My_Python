def calc():
    while True:
        try:
            a = float(input('Введите первое число:'))
    
            b = float(input('Введите второе число:'))
        
        
            operation = input('Введите действие:')
        
           
            if operation == '*':
                print(f'Результат: {a * b}')

            elif operation == '/':
                try:
                    print(f'Результат: {a / b}')
                except ZeroDivisionError:
                    print('Делить на 0 нельзя!')
        
            elif operation == '+':
                print(f'Результат: {a + b}')
    
            elif operation == '-':
                print(f'Результат: {a - b}')
            else:
                print('Неподдерживаемая операция!')
                continue
            break

        except ValueError:
            print('Введите число!')
        
        

calc()

    