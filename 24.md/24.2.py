class Employee :
  __name = None

  def __init__(self, name):
    self.__name = name

  def getName(self):
    return self.__name

Employees = [
	 Employee('Арина,150000'),
	 Employee('Ася,300000'),
	 Employee('Саша,100000'),
]

for user in Employees:
	print(user.getName())