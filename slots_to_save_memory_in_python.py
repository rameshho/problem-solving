__author__ = 'rameshho'

class myclass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.set_up()

    def set_up(self):
        print("hosamani")

class myclass(object):
    __slot__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

without_slot = myclass("ramesh", 28)
print(without_slot.__dict__)