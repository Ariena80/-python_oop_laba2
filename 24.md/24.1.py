class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee("Арина", 150000),
    Employee("Ася", 300000),
    Employee("Александр", 100000)
]


for employee in employees:
    print(f"Имя: {employee.name} \t Зарплата: {employee.salary}")