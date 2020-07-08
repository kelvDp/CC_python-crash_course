# Defining a function:

def greet_user():
    """
    Display a simple greeting.  --- this is a short description of what the function will do.
    """

    print("Hello!")


greet_user() #this is how you call a function.

# you can pass in parameters/info into a function to use as an argument when you call the function:
def greet_user(username):
    """
    Display a simple greeting.
    """
    print(f"Hello, {username.title()}!")


greet_user('jesse')

# can use functions with a while loop :
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!, unless you break out of it
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    if l_name == "quit":
        break
        