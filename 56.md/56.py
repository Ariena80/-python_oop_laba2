class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_seconds_difference(self):
        return (self.end - self.start).total_seconds()

    def get_minutes_difference(self):
        return self.get_seconds_difference() / 60

    def get_hours_difference(self):
        return self.get_minutes_difference() / 60

    def get_days_difference(self):
        return self.get_hours_difference() / 24


# Пример использования
import datetime

start_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
end_time = datetime.datetime(2021, 1, 2, 12, 0, 0)

period = Period(start_time, end_time)
print("Seconds difference:", period.get_seconds_difference())
print("Minutes difference:", period.get_minutes_difference())
print("Hours difference:", period.get_hours_difference())
print("Days difference:", period.get_days_difference())