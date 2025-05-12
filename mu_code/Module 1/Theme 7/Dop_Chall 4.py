#Находит элементы, общие для всех трёх списков.
#Находит элементы, которые есть только в первом списке.
#Выводит результаты в формате:
#Общие элементы: [5]
#Уникальные для list1: [1, 2]


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
uniqum_list1 = []
common_list = []

for i in list1:
    if i not in list2 and i not in list3:
        uniqum_list1.append(i)

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

inter_set = set1 & set2 & set3

unique_to_list1 = set1 - (set2 | set3)


print(f'Общие элементы: {list(inter_set)}')
print(f'Уникальные для list1: {uniqum_list1}')