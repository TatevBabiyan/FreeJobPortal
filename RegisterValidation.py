from NameValidationDescriptor import *
from SurnameValidationDescriptor import *
from EmailValidationDescriptor import *
from PasswordValidationDescriptor import *

class Validation:
    name = NameValidation()
    surname = SurnameValidation()
    email = EmailValidation()
    password = PasswordValidation()

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

