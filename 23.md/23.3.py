class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department

class Position:
    title = None

    def __init__(self, title):
        self.title = title

class Department:
    name = None

    def __init__(self, name):
        self.name = name


position = Position("Менеджер")
department = Department("Отдел продаж")

user = User("Иван", position, department)

print("Имя:", user.name)
print("Должность:", user.position.title)
print("Отдел:", user.department.name)