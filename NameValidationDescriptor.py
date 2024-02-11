class NameValidation:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if 4 <= len(value) <= 20 and value.isalpha() and ' ' not in value:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Enter a Valid Name")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]

