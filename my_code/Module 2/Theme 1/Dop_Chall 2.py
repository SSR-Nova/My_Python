
def binary_search_recursive(arr, search, left = 0, right = None):
    if right == None:
        right = len(arr) - 1

    if left > right:
        return -1
    mid = (left + right)//2

    if arr[mid] == search:
        return mid
    elif arr[mid] < search:
        return binary_search_recursive(arr, search, mid + 1, right)
    else:
        binary_search_recursive(arr, search, left, mid - 1)
    

sorted_numbers = [1, 3, 5, 7, 9]  
print(binary_search_recursive(sorted_numbers, 7)) 