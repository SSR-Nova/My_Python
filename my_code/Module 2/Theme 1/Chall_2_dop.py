def bubble_sort(numbers):
    n = len(numbers)  
    for i in range(n):
        if numbers[i - 1] < numbers[i]:
            print(numbers)
            break
        else:
            for j in range(0, n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    print(numbers)




numbers = [7, 2, 5, 1, 9]
bubble_sort(numbers)