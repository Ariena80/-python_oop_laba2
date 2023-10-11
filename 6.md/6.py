class Employee:
    def test_method(self, name, salary):
        return f"Работник {name} имеет зарплату {salary}."

employee = Employee()
print(employee.test_method("Арина", 8000))