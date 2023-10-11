class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Salary: {self.salary}"
e = Employee("Морозова Арина", 8000)
print(e.show())