from functools import wraps

def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[call] {func.__name__} args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[ret ] {func.__name__} -> {result}")
        return result
    return wrapper

@log_io
def add(a, b):
    """Add two numbers."""
    return a + b

print(add(1, 2))

"""
[call] add args=(1, 2), kwargs={}
[ret ] add -> 3
3
"""

from functools import wraps
import time

def retry(times=3, delay=0.1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return deco

@retry(times=5, delay=0.2)
def flaky():
    return 1 / 0

print(flaky())