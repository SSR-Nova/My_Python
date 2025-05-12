#Универсальный обработчик
#Напишите функцию processor, которая:
#Принимает обязательный аргумент operation (строка: "sum", "multiply", "concat").
#Принимает *args для чисел (если операция "sum" или "multiply").
#Принимает **kwargs для строк (если операция "concat").

def processor(operation, *args, **kwargs):
    if operation == 'sum':
        return sum(args)
    elif operation == 'concat':
        return ''.join(str(value) for value in kwargs.values())



print(processor("sum", 1, 2, 3)) 
print(processor("concat", a="Hello", b=" "))