class User:
    def set_name(self, name):
        if self.__not_empty(name):
            self.__name = name

    def get_name(self):
        return self.__name

    def __not_empty(self, stri):
        return len(stri) > 0

class Employee(User):
    def set_surname(self, surname):
        if self._User__not_empty(surname):  # Use the proper method name with correct naming conventions
            self.__surname = surname

    def get_surname(self):
        return self.__surname

employee = Employee()
employee.set_name("Арина")
employee.set_surname("Морозова")

print("Name:", employee.get_name())
print("Surname:", employee.get_surname())