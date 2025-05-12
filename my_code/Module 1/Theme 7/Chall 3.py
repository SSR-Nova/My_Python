#Напишите код, который выводит:
#Общих друзей.
#Всех уникальных друзей.


friends1 = {"Анна", "Борис", "Владимир"}  
friends2 = {"Борис", "Дмитрий", "Анна"}  
all_friends = friends1.union(friends2)

print(f'Общие друзья: {friends1 & friends2}')
print(f'Все друзья: {all_friends}')