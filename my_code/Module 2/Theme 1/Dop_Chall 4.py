#Рекусивный подсчёт элементов
'''def count_occurrences(arr, target):
    count = 0
    if not arr:
        return 0
    
    for i in arr:
        if i == target:
            count += 1
    return count'''

def count_occurrences(arr, target, start=None):
    start = len(arr) - 1
    count = 0
    if not arr:
        return 0
    elif arr[start] == target:
        count += 1
        count_occurrences(arr, target, start - 1)
        
    return count   
    


numbers = [1, 2, 2, 3, 2, 4]  
print(count_occurrences(numbers, 2))