class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def increase_salary(self):
        self.salary *= 1.1

employee = Employee("Арина Морозова", 8000)

print(employee.get_name())

print(employee.get_salary())

employee.increase_salary()

print(employee.get_salary())