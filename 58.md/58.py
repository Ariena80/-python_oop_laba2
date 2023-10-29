class Zate:
    pass


class ZateExt(Zate):
    def add_years(self, years):
        self.year += years

    def subtract_years(self, years):
        self.year -= years

    def add_months(self, months):
        self.month += months
        if self.month > 12:
            self.year += self.month // 12
            self.month = self.month % 12

    def subtract_months(self, months):
        self.month -= months
        if self.month < 1:
            self.year -= abs(self.month) // 12 + 1
            self.month = self.month % 12 + 12

    def add_days(self, days):
        self.day += days
        while self.day > self.days_in_month(self.year, self.month):
            self.day -= self.days_in_month(self.year, self.month)
            self.month += 1
            if self.month > 12:
                self.year += 1
                self.month = 1

    def subtract_days(self, days):
        self.day -= days
        while self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            self.day += self.days_in_month(self.year, self.month)