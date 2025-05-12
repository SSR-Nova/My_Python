import json

try:
    # Открываем файл для чтения
    with open('task.json', 'r') as file:
        list_task = json.load(file)
except FileNotFoundError:
    # Список всех задач
    list_task = []


 

# Добавление задачи
def add_task():
        
    new_task = input('Введите новую задачу: ')
    task = {'id':None, 'title': None, 'done': False}
    task['title'] = new_task
    task['id'] = len(list_task) + 1
    list_task.append(task)
    print(f'\nЗадача "{new_task}" добавлена!\n')
    return




# Изменение статуса задачи
def status_task():
    id_task = int(input('Введите индекс ID задачи для которой необходимо изменить статус: '))
    for task in list_task:
        if task['id'] == id_task:
            if task['done'] == True:
                task['done'] = False
                print(f'\nСтатус задачи ID: {id_task} изменен!')
                return
            else:
                task['done'] = True
                print(f'\nСтатус задачи ID: {id_task} изменен!')
                return
        
    print('\nЗадачи с таким ID не существует!')
            



# Удаление задачи
def delete_task():
    id_task = int(input('Введите ID задачи, которую необходимо удалить: '))
    for task in list_task:
        if task['id'] == id_task:
            while True:
                enter = input('Вы действительно хотите удалить задачу? Да/Нет: ')
                if enter == 'Да':
                    list_task.remove(task)
                    # Перерасчёт индексов
                    id = 0
                    for task_id in list_task:
                        id += 1
                        task_id['id'] = id
                    print('\nЗадача удалена!')
                    print('Обновленный список задач: ')
                    all_task()
                    break
                elif enter == 'Нет':
                    break
                else:
                    print('Введите Да/Нет')
                    continue
    



# Сохранение и выход из программы
def exit_save_task():
    with open('task.json', 'w') as file:
        json.dump(list_task, file)
        print('\nФайл сохранен!')
        return
                
                 


# Выводит список всех задач
def all_task():
    
    for task in list_task:
        if task['done'] == True:
            print(f'\n{task["id"]}. [✔] {task["title"]}')
        else:
            print(f'\n{task["id"]}. [X] {task["title"]}')



# Формируем основное меню со списком возможных команд и вводом команды

while True:
    print('\nСписок задач: \n 1. Добавить задачу \n 2. Показать все задачи \n 3. Отметить как выполненную \n 4. Удалить задачу \n 5. Выход и сохранение в файл')
    choice = input('Введите команду: ')
    if not choice.isdigit():
        print('Ошибка: Введеная команда должна быть числом')
        continue

    choice = int(choice)
    
        #Прописываем старт функции в зависимости от выбранной команды

    if choice == 1:
        add_task()
    
    elif choice == 2:
        all_task()
    
    elif choice == 3:
        status_task()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        exit_save_task()
        break