class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    class EmployeesCollection:
        def __init__(self):
            self.employees = []