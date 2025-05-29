class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, new_name):
        if len(new_name) == 0:
            print('Ошибка: Пустое имя')

        else:
            self.__owner = new_name

    def deposit(self, deposits):
        if deposits < 0:
            print('Ошибка: Введеная сумма должна быть положительной!')
        else:
            self.__balance = self.__balance + deposits

    def withdraw(self, withdraws):
        if withdraws > self.__balance:
            print('Ошибка: Нельзя снять больше, чем есть на счету!')
        else:
            self.__balance = self.__balance - withdraws

acc = BankAccount('Иван', 1000)
print(acc.balance)
acc.deposit(500)
print(acc.balance)
acc.withdraw(2000)
acc.owner = ''