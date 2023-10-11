import re

class Validator:
    def __init__(self):
        pass

    def isEmail(self, string):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, string):
            return True
        else:
            return False

    def isDomain(self, string):
        pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, string):
            return True
        else:
            return False

    def isNumber(self, string):
        pattern = r'^\d+$'
        if re.match(pattern, string):
            return True
        else:
            return False

validator = Validator()

print(validator.isEmail('example@example.com'))
print(validator.isEmail('example.com'))

print(validator.isDomain('example.com'))
print(validator.isDomain('example'))

print(validator.isNumber('12345'))
print(validator.isNumber('abc123'))