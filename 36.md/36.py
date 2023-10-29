class User:
    def init(self):
        self.name = ''

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

class Employee(User):
    def setname(self, name):
        if len(name) > 0:
            super().setname(name)

employee = Employee()
employee.setname("Арина")
print("Name:", employee.getname())