class BankAccount:
    def __init__(self, owner, balance = 0):
        self._balance = balance  
        self.owner = owner

    def deposit(self, amount):
        if amount <= 0:
            print('Ошибка: 0 или отрицательное число!')
        else:
            self._balance = self._balance + amount
            print(f'Счёт пополнен на {amount}')
            return self._balance

    def withdraw(self, amount):
        if self._balance < amount:
            print('На счёте недостаточно средств!')

        else:
            self._balance = self._balance - amount
            print(f'Со счёта снято {amount}')
            return self._balance
        

    def check_balance(self):
        return self._balance
    
account = BankAccount("Иван")
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())