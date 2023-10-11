class Student:
    name = "Арина"
    surname = "Морозова"

    def show(self):
        return f"Name: {self.name}, Surname: {self.surname}"

student = Student()
print(student.show())