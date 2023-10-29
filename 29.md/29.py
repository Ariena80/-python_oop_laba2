class User:
    def __init__(self):
        ...
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Employee(User):
    ...

stuff = Employee()

stuff.setName('Арина')
print(stuff.getName())