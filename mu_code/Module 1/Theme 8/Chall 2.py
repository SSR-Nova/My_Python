from datetime import datetime

mood = input('Введите Ваше настроение: ')
current_time = datetime.now()
now_time = current_time.strftime("%d-%m-%Y")
with open('mood_diary.txt', 'a') as file:
    file.write(str(now_time)+ ':' + ' ' + mood + '\n')
