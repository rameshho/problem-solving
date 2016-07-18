class Date(object):

    # day = 0
    # month = 0
    # year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod                                                        #you can create instance using this decorator
    def from_string(cls, date_as_string):
        print(cls)
        day, month, year = map(int, date_as_string.split('-'))
        #date2 = cls()
#        print(date2)
 #       print(isinstance(date2))
        date1 = cls(day, month, year)
        return date1

    def display(self):
        print(self.day)
        print(self.month)
        print(self.year)

#
d = Date()
d.display()

b = Date.from_string("11-3-2011")
print(isinstance(b, Date))
print(b)
b.display()