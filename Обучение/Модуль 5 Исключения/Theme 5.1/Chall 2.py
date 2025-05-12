
def dostup():
    list = ['яблоко', 'банан', 'киви', 'манго', 'апельсин']
    while True:
    
        try:
            index = int(input('Введите индекс:'))
            if index < 0:
                print('Введите положительный индекс')
                continue
        
            print(list[index])
            break

        
        except ValueError:
            print('Введите число!')
            
        except IndexError:
            print('Вы вышли за пределы индекса!')

dostup()
