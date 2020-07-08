# The following example sends a list of names to a function called greet_users(),
# which greets each person in the list individually:

def greet_users(names):
    """Print a simple greeting to each user in the list."""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)