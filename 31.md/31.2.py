class Employee:
    name = None
    age = None

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Employee2(Employee):

    def setName(self, name):
        if len(name) > 0:
            self.name = name
        else:
            raise Exception("Вы ввели не верное имя!")

    def setAge(self, age):
        if age > 0:
            self.age = age
        else:
            raise Exception("Возраст не может быть меньше 0")

emp = Employee2()
emp.setName('Арина')
emp.setAge(18)

print(emp.getName())
print(emp.getAge())