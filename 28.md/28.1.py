class User:
    def __init__(self, name):
        self.name = name

class Employee(User):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_info(self):
        print(f"Имя: {self.name}, Зарплата: {self.salary}")

employee = Employee("Арина", 50000)


employee.display_info()