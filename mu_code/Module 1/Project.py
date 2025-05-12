import json

# Список всех задач
list_task = [] 

# Формируем основное меню со списком возможных команд и вводом команды

while True:
    print('Список задач: \n 1. Добавить задачу \n 2. Показать все задачи \n 3. Отметить как выполненную \n 4. Удалить задачу \n 5. Выход и сохранение в файл')
    choice = int(input('Введите команду: '))

    


    # Добавление задачи
    def add_task():
        
        new_task = input('Введите новую задачу: ')
        task = {'id':None, 'title': None, 'done':'Не выполнена'}
        task['title'] = new_task
        task['id'] = len(list_task) + 1
        list_task.append(task)
        print(f'Задача "{new_task}" добавлена!')
        return




    # Изменение статуса задачи
    def status_task():
        id_task = int(input('Введите индекс ID задачи для которой необходимо изменить статус: '))
        for task in list_task:
            if task['id'] == id_task:
                task['done'] = 'Выполена'
                print(f'Статус задачи ID: {id_task} изменен!')
                return
            else:
                print('Задачи с таким ID не существует!')

    # Удаление задачи
    def delete_task():
        id_task = int(input('Введите ID задачи, которую необходимо удалить: '))
        for task in list_task:
            if task['id'] == id_task:
                while True:
                    enter = input('Вы действительно хотите удалить задачу? Да/Нет: ')
                    if enter == 'Да':
                        list_task.remove(task)
                        print('Задача удалена!')
                        break
                    elif enter == 'Нет':
                        break
                    else:
                        print('Введите Да/Нет')
    


    # Сохранение и выход из программы
    def exit_save_task():
        with open('task.json', 'w') as file:
            json.dump(list_task, file)
            print('Файл сохранен!')
            return
                
                 




    # Выводит список всех задач
    def all_task():
        print(list_task)

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