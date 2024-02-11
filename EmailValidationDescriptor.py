import re

class EmailValidation:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if re.fullmatch(regex, value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Enter a Valid Email")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


