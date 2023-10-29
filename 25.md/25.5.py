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

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

    def calculate_average_salary(self):
        total_salary = self.calculate_total_salary()
        if len(self.employees) > 0:
            average_salary = total_salary / len(self.employees)
            return average_salary
        else:
            return 0

collection = EmployeesCollection()


collection.add_employee("Арина", 150000)
collection.add_employee("Ася", 300000)
collection.add_employee("Александр", 100000)

collection.print_employees()


average_salary = collection.calculate_average_salary()
print(f"Средняя зарплата всех работников: {average_salary}")