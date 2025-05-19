def find_min(arr, index=0):
    if len(arr) == 0:
        return None
    if index == len(arr) - 1:  # Достигли последнего элемента
        return arr[index]
    current = arr[index]
    rest_min = find_min(arr, index + 1)  # Минимум в оставшейся части
    return current if current < rest_min else rest_min

numbers = [5, 2, 9, 1, 7]
print(find_min(numbers))