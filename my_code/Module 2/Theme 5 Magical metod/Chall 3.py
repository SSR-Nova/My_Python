class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'Контакт: {self.name}, Телефон: {self.phone}'
    
contact = Contact('Сергей', '+79878137069')
print(contact)