import datetime


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_weekday_number(self):
        return self.date.weekday()

    def get_weekday_name(self):
        weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday_names[self.get_weekday_number()]

    def get_month_name(self):
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]
        return month_names[self.get_month() - 1]


# Пример использования
zate = Zate(2021, 5, 17)
print("Year:", zate.get_year())
print("Month:", zate.get_month())
print("Day:", zate.get_day())
print("Weekday Number:", zate.get_weekday_number())
print("Weekday Name:", zate.get_weekday_name())
print("Month Name:", zate.get_month_name())