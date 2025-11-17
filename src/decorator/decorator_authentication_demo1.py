from functools import wraps

def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):   # Pass all positional arguments or keyword arguments to the wrapper
        VALIDATED_USERS = ["John", "Feng", "Mike", "Jennie"]
        user = args[0] if args else kwargs.get("user")
        if user not in VALIDATED_USERS:
            raise PermissionError("Invalid user!")
        return func(*args, **kwargs)
    return wrapper


@auth
def view_database(user, database_name):
    print(f"{database_name} is open by {user}.")


# view_database(user="Feng", database_name="dev.bronze")
view_database(user="Hacker", database_name="prod.gold")