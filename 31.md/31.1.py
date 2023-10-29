class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self._age = age


    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age



employee = Employee("Арина", 50000, 18)


print("Возраст:", employee.get_age())


employee.set_age(19)
print("Новый возраст:", employee.get_age())