from math import floor
class TimeSpan:
    def __init__(self, weeks, days, hours):
        self.weeks = weeks
        self.days = days
        self.hours = hours

        if type(weeks) is not int:
            raise TypeError("This class only accepts integers.")
        if type(days) is not int:
            raise TypeError("This class only accepts integers.")
        if type(hours) is not int:
            raise TypeError("This class only accepts integers.")
        if not (weeks >= 0 and days >= 0 and hours >= 0):
            raise ValueError("Values cannot be negative")
        if (self.hours >= 24):
            self.days += floor(self.hours/24)
            self.hours = self.hours%24
        if (self.days >= 7):
            self.weeks += floor(self.days/7)
            self.days = self.days%7

    def __str__(self):
        output = ("{0:02d}").format(self.weeks)+"W "+("{0:01d}").format(self.days)+"D "+("{0:02d}").format(self.hours)+"H"
        return output

    def getTotalHours(self):
        return (self.weeks * (7 * 24) + self.days * 24 + self.hours)

    def __add__(self, other):
        if type(other) is not TimeSpan:
            raise TypeError("Other should be of type TimeSpan")
        weeks=self.weeks+other.weeks
        hours=self.hours+other.hours
        days = self.days+other.days
        New=TimeSpan(weeks,days,hours)
        return New

    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError("Other should be of type int")
        if other <= 0:
            raise ValueError("Other should be of greater than 0")
        weeks=self.weeks*other
        hours=self.hours*other
        days = self.days*other
        New=TimeSpan(weeks,days,hours)
        return New
    __rmul__ = __mul__

