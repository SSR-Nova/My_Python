#Сортировка вставками
def insertion_sort(arr):
    if not arr:
        return
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break



numbers = [4, 2, 7, 1, 3]  
insertion_sort(numbers)  
print(numbers) 