class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        
        self.balance += amount
        return f'На Ваш счёт поступило: {amount}. Баланс на счёте составляет: {self.balance}'
    def withdraw(self):
        draw = float(input('Введити сумму для снятия со счёта: '))
        self.balance = self.balance - draw
        if self.balance >= 0:
            return f'С Вашего счёта списано: {draw}. Баланс на счёте составляет: {self.balance}'
        else:
            return f'На Вашем счёте недостаточно средств'
    def info(self):
        return f"Владелец счета: {self.owner}\nБаланс: {self.balance}"


my_bank = BankAccount('Полетаев Сергей', 100000)
print(f'{my_bank.deposit(3000)}')