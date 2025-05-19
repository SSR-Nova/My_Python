def recursive_sum(arr, index = 0):
    if index >= len(arr):
        return 0
    
    return arr[index] + recursive_sum(arr, index + 1) 
    

numbers = [1, 2, 3, 4]
print(recursive_sum(numbers)) 