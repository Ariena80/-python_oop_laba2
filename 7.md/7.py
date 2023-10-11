class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        print(self.name)

    def get_salary(self):
        print(self.salary)

employee = Employee("Арина", 8000)
employee.get_name()
employee.get_salary()