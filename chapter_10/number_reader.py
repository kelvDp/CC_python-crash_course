import json

filename = "numbers.json"

with open(filename) as f:
    numbers = json.load(f) # this loads the json data in the file

print(numbers)

# Saving data with json is useful when you’re working with user-generated
# data, because if you don’t store your user’s information somehow, you’ll lose
# it when the program stops running.

