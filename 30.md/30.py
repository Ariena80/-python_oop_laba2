class User:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Имя: {self.name}")


class Employee(User):
    def __init__(self, name, salary, surname):
        super().__init__(name)
        self._salary = salary
        self._surname = surname


    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname



employee = Employee("Ася", 50000, "Сакичева")


employee.display_info()


print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())
print("Фамилия:", employee.get_surname())


employee.set_name("Арина")
employee.set_salary(60000)
employee.set_surname("Морозова")


print("Новое имя:", employee.get_name())
print("Новая зарплата:", employee.get_salary())
print("Новая фамилия:", employee.get_surname())