__author__ = 'rameshho'

def fibonacci_numbers(maximum_number):
    a, b = 0, 1
    while b < maximum_number:
        a, b = b, a + b
        print(a)

if __name__ == "__main__":
    fibonacci_numbers(100)