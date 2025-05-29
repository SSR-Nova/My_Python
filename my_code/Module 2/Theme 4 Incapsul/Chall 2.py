class User:
    def __init__(self, name, __password):
        self.__password = __password
        self.name = name

    @property
    def password(self):
        return '******'

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            print('Ошибка: Пароль слишком короткий!')
        else:
            self.__password = new_password

user = User('admin', 'qwerty123')
print(user.password)
user.password = "123"