class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self):
        print("Logged in as", self.username)

    def __get_password(self):
        return self.__password

class Employee(User):
    def __init__(self, username, password, position):
        super().__init__(username, password)
        self.position = position

    def get_position(self):
        return self.position

    def get_password(self):
        return super()._User__get_password()

employee = Employee("arieshka", "ertfa1674", "Manager")
employee.login()
print("Position:", employee.get_position())
print("Password:", employee.get_password())