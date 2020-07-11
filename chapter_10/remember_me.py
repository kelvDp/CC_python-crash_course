import json


# we
# prompt the user for their name the first time they run a program and then
# remember their name when they run the program again.

# username = input("What is your name?")
#
# filename = "username.json"
#
# with open(filename,"w") as f:
#     json.dump(username,f)
#     print(f"We'll remember you when you come back, {username}.")

# we can combine both the json.dump and load method in one program:
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it:

# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name ?")
#     with open(filename,"w") as f:
#         json.dump(username,f)
#         print(f"We'll remember you the next time {username}!")
# else:
#     print(f"Welcome back {username}!")

# we can move all of the code above into one function since it is all just about greeting the user.
# we can then simply call the function:

# def greet_user():
#     """Greet the user by name."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}!")


# greet_user()
# -------------------------------------------------
# We can refactor greet_user() so it’s not doing so many different tasks. We’ll
# start by moving the code for retrieving a stored username to a separate
# function:

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back {username}!")
#     else:
#         username = input("What is your name ?")
#         filename = "username.json"
#         with open(filename, "w") as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")
#
#
# greet_user()

# can refactor even more by adding the code to get a new user into a function :

def get_new_user():
    """Prompt for a new username"""

    username = input("What is your name ?")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
        return username

# now we can add them all together :

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_user()
        print(f"We'll remember you when you come back, {username}!")


greet_user()