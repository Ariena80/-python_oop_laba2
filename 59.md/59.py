class Month:
    def __init__(self, month_number):
        self.month_number = month_number

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return month_names[self.month_number - 1]

    def get_last_day_number(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month_number == 2:
            # Check for leap year
            if self.is_leap_year():
                return 29
        return days_in_month[self.month_number - 1]

    def get_first_weekday_number(self):
        from datetime import date
        return date(2021, self.month_number, 1).weekday()  # Assuming the year is 2021

    def get_last_weekday_number(self):
        from datetime import date
        return date(2021, self.month_number, self.get_last_day_number()).weekday()  # Assuming the year is 2021

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
