class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

collection = EmployeesCollection()


collection.add_employee("Арина", 150000)
collection.add_employee("Ася", 300000)
collection.add_employee("Александр", 100000)


for employee in collection.employees:
    print(f"Имя: {employee.name} \t Зарплата: {employee.salary}")