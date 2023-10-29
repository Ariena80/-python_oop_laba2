class User:
    def __init__(self):
        self._name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)


class Employee(User):
    def set_name(self, name):
        if len(name) > 0:
            self._name = name

    name = property(User.get_name, set_name)


employee = Employee()
employee.name = "Арина"
print("Name:", employee.name)