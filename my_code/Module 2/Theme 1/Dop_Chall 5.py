#Проверка на палиндром
def is_palindrome(text, start=0, end=-1):
    #Убираем пробелы и приводим к нижнему регистру
    text = text.replace(' ', '').lower()
    #Запускаем отсчёт от последнего индекса
    if end == -1:
        end = len(text) - 1
    # Когда индексы встречаются выдаем ответ  
    if start >= end:
        return True
   
    # если первый и последний индекс одинаковые, запускаем рекурсию, увеличивая первый индекс и уменьшая последний
    elif text[start] == text[end]:
        return is_palindrome(text, start + 1,end - 1)
    # Иначе это не палиндром    
    else:
        return False

print(is_palindrome("А роза упала на лапу Азора")) 