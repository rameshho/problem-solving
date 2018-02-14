'''
    This is the practical example of using decorators
    It will show how to writer logger and time took to execute function in log files.
'''

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

#display_info("ramesh", 30)

#display_info = my_timer(display_info)    #This is equivalent to @my_timer decorator
print display_info.__name__               #you will get wrapper as output. so to preserve the function name we should use functools

print display_info('ramesh', 'hossamani')
#display_info = my_logger(my_timer(display_info))   #This is equivalent to @my_logger after that @my_timer for display_info