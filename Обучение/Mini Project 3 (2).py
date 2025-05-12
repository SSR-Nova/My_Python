#Создаем класс Задачи с аргументами (задача, статус), Статус изначально стоит "не выполнено" 
class Task:
    def __init__(self, description, status):
        self.description = description
        self.status = 'Не выполнено'

    #Функция информации
    def info(self):
        return f'Задача: {self.description}. Статус задачи: {self.status}'
    
    def __str__(self):
        return self.info()
    
#Создаем класс Лист Задач    
class ToDoList:
    #Функция с пустым аргументом под список(в который будут добавляться задачи и производится с ними действия)
    def __init__(self):
        self.tasks = []

        #Фунция для добавления задачи
    def add_tasks(self, description, status='Не выполнено'):
        # Проверяем, есть ли задача с таким описанием в списке
        for task in self.tasks:
            if task.description == description:
                task.status = 'Выполнено'  # Меняем статус задачи
                print(f'Статус задачи "{description}" изменён на "Выполнено"')
                return

        # Если задачи нет, добавляем её
        task = Task(description, status)
        self.tasks.append(task)
        print(f'Задача: "{description}" добавлена в список задач')

    #Функция для удаления задачи
    def remove_task(self, description): 
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f'Задача: "{description}" удалена из списка задач!')
                return
            
            print(f'Задача "{description}" отсутствует в списке задач')
                
    
    def show_tasks(self):
        for i in self.tasks:
            print(i)
    
    
    
    

TodayList = ToDoList()

TodayList.add_tasks('Покушать')
TodayList.add_tasks('Идти на работу')
TodayList.add_tasks('Сходить в душ')
TodayList.add_tasks('Покушать')
TodayList.remove_task('Сходить в душ')
TodayList.show_tasks()