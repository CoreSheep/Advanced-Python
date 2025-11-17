"""
How to use lambda functions in Python.
    1. Lambda function is a one-line function
    2. Lambda function is an anonymous function (without function name)
    3. How to define a lambda function: lambda arguments: expression (usually use in a mathmatical expression)
"""
from functools import wraps
# 1. Basic  -- anoynmous function
def divide_by_zero(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        y = args[1] if args else kwargs.get("y")
        # operation = args[2] if args else kwargs.get("operation")
        if y == 0:  # suppose the operation is division
            raise ZeroDivisionError("Cannot divide by zero.")
        return func(*args, **kwargs)
    return wrapper

@divide_by_zero
def apply_operations(x, y, operation):
    return operation(x, y)

res = apply_operations(1, 5, lambda a, b: a + b)
print(f"res: {res}")


# 2. map(lambda, iter) and sorted(iter, key)
def add_tax_for_salary(salary, tax_rate):
    return list(map(lambda s: s * (1 - tax_rate), salary))

salary = [100000, 90000, 80000]
tax_rate = 0.4

print(f"Salary after tax: {add_tax_for_salary(salary=salary, tax_rate=tax_rate)}")


products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 80}
]

# sort by price
sorted_price = sorted(products, key=lambda p: p['price'])
print(f"Sorted by price for products: {sorted_price}")

# sort by length of name, descending
sorted_name_len = sorted(products, key=lambda p: len(p['name']), reverse=True)
print(f"Sorted by name for products: {sorted_name_len}")
