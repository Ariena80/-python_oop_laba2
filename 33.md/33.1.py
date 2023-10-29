class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def getSurn(self):
        return self.surname

class Employee(User):

    ...