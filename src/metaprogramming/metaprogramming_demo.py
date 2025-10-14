def create_user_class(class_name, attributes):
    """Dynamically creates a user class with given attributes."""
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in attributes:
                setattr(self, attr, value)
            else:
                raise AttributeError(f"Invalid attribute: {attr}")
    class_attrs = {"__init__": __init__}
    for attr in attributes:
        class_attrs[attr] = None
    return type(class_name, (object,), class_attrs)

BasicUser = create_user_class("BasicUser", ["username", "email"])
PremiumUser = create_user_class("PremiumUser", ["username", "email", "subscription_level"]) # Corrected line

basic_user = BasicUser(username="Alice", email="alice@example.com")
premium_user = PremiumUser(username="Bob", email="bob@example.com", subscription_level="gold")

print(basic_user.username)  # Output: Alice
print(premium_user.subscription_level)  # Output: gold


"""
Say you're building a program that needs to create different types of user accounts, each with specific properties. 
Instead of defining separate classes for each account type, you can use metaprogramming to create them dynamically.

In the example, the create_user_class function takes a class name and a list of attributes as input. It then uses 
the type() function to dynamically create a new class with those attributes. This allows you to generate classes 
dynamically, adapting your code to different needs without writing repetitive class definitions.

These examples showcase the power and flexibility of metaprogramming in Python. By understanding these concepts, 
you can write more adaptable, efficient, and expressive code.

Metaprogramming is a fascinating aspect of programming that allows you to write code that can manipulate other code. 
It's like giving your code a brain of its own, enabling it to adapt, evolve, and generate new code dynamically. 
While it might seem complex at first, the core idea is simple: write code that writes code. This powerful technique 
can be used to create DSLs, build flexible frameworks, and automate repetitive tasks.  

Metaprogramming is a powerful tool, but it's important to use it responsibly. Overusing metaprogramming can make 
your code harder to understand and debug. It's best to use it strategically to solve specific problems and improve
code clarity, not just for the sake of being clever.  Think of it like a superpower. It can be used for good or 
for evil. A responsible programmer uses metaprogramming to create elegant and efficient solutions, while an 
irresponsible one might use it to create confusing and unmaintainable code.
"""