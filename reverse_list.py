__author__ = 'rameshho'

class reverse_list:
    def __init__(self, b):
        self.b = b
        self.counter = len(self.b) - 1

    def __iter__(self):
        return self

    def __next__(self):
        item = self.b[self.counter]
        self.counter -= 1
        if self.counter < -1:
            self.counter = len(self.b) - 1
            raise StopIteration
        return item

my_list = range(10)

print(my_list)

obj = reverse_list(my_list)

for i in obj:
    print(i)