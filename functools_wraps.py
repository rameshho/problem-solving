from functools import wraps
import inspect
def logged(func):
    func_info = inspect.getfullargspec(func)
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func_info.annotations['cls'])
        print (func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print (f.__name__)  # prints 'f'
print (f.__doc__)   # prints 'does some math'
