#Рекусивный подсчёт элементов


def count_occurrences(arr, target, start=0):
    #Проверка длины списка
    if start >= len(arr):
        return 0
    #Если значения совпадают +1 и продолжение рекурсии
    elif arr[start] == target:
        return 1 + count_occurrences(arr, target, start + 1)
    # Если не совпадают 0+ продолжение рекурсии    
    else:
        return 0 + count_occurrences(arr, target, start + 1)
        
      
    


numbers = [1, 2, 2, 3, 2, 4]  
print(count_occurrences(numbers, 2))