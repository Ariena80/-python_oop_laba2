class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def show_info(self):
        return f"Name: {self.__name}, Salary: {self.__salary}, Age: {self.__age}"

employee = Employee("Морозова Арина", 8000, 18)

print(employee.show_info())