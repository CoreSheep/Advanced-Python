import time
import numpy as np

def timer(func):
    """A decorator that prints the time taken by the decorated function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f}s to execute.")
        return result
    return wrapper

@timer
def add(a, b):
    return a + b

@timer
def matrix_multiply(a, b):
    # Convert lists to numpy arrays for matrix multiplication
    a = np.array(a)
    b = np.array(b)
    return a @ b

result1 = add(1999, 2999)
print(f'result1: {result1}')

result2 = matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(f'result2: {result2}')