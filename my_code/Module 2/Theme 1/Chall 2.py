def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j +1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

numbers = [4, 2, 7, 1, 9]
bubble_sort(numbers)
print(numbers)  