"""
How to use decorators to measure the execution time of functions.
    1. A decorator is a function you call every time when you specify a decorator @ before the fucntion
    2. Learn how to define a decorator: functool.wraps (@wraps is another decorator to wrap a function)
    3. The wrapper function will replace the original function at run time
    4. Think wrapper as a gift wrapper, the gift itself is original func
"""

import time
from functools import wraps

def timing_decorator_no_wrap_decorator(func):
    def wrapper(*args, **kwargs):
        """wrapper func for timing"""
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} s to complete.")
    return wrapper


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper func for timing"""
        start = time.time()
        func(*args, **kwargs)   # call the original func
        print(f"{func.__name__} took {time.time() - start:.4f} s to complete.")
    return wrapper  # Return the wrapper for the decorator


@timing_decorator
def slow_time():
    """slow time with sleeping for 1 sec"""
    time.sleep(1)
    print(f"Time sleeps for 1 sec.")


def main():
    slow_time()
    print(f"slow_time.__name__ is {slow_time.__name__}")    
    # if we don't use @wraps(func) for the warpper func, it will automatically replace the original func
    print(f"slow_time.__doc__ is {slow_time.__doc__}")



if __name__ == "__main__":
    main()