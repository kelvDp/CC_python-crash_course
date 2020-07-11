import json
# program that greets a user whose name has already
# been stored:

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}!")

