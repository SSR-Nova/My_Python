class UserValidator:
    
    @staticmethod
    def validate_email(email):
        return '@' in email
    
    @staticmethod
    def validate_phone(phone):
        return phone.isdigit()
    
print(UserValidator.validate_email("test@example.com")) 
print(UserValidator.validate_phone("123abc"))