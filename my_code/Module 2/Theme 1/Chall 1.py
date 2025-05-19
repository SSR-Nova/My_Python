def search_index(numbers, x):
    for number in range(len(numbers)):
            if numbers[number] == x:
                return number
    
    return -1
    
            
numbers = [3, 6, 2, 8, 4]

print(search_index(numbers, 25))
