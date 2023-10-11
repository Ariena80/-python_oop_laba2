class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def capitalize_first_letter(self, string):
        return string[0].upper()

    def get_initials(self):
        first_letter_name = self.capitalize_first_letter(self.name)
        first_letter_surname = self.capitalize_first_letter(self.surname)
        return first_letter_name + first_letter_surname

student = Student("Арина", "Морозова")
print(student.get_initials())