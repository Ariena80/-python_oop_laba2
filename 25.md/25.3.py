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

    def print_employees(self):
        if len(self.employees) == 0:
            print("Нет доступных работников.")
        else:
            print("Список работников:")
            for employee in self.employees:
                print(f"Имя: {employee.name} \t Зарплата: {employee.salary}")

collection = EmployeesCollection()


collection.add_employee("Арина", 150000)
collection.add_employee("Ася", 300000)
collection.add_employee("Александр", 100000)

collection.print_employees()