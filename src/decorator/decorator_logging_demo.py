import logging
def logger(func): 
    def wrapper(*args, **kwargs): 
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}") 
        result = func(*args, **kwargs) 
        logging.info(f"{func.__name__} returned: {result}") 
        return result 
    return wrapper

"""A decorator that logs function calls."""
logging.basicConfig(filename="./my_app.log",level=logging.INFO) 

@logger 
def my_function(a, b): 
    """A simple function that adds two numbers.""" 
    return a + b

result = my_function(5, 3) 
print(f"Result: {result}")

"""
With this detailed logging information, you can:

- Track down bugs: Identify the exact point where an error occurred and the conditions that led to it.
- Monitor performance: See which parts of your code are taking the longest to execute.
- Understand user behavior: Analyze how users interact with your program.
- Audit security events: Keep a record of who accessed what and when.

"""