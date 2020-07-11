import json

numbers = [2,3,5,7,11,13]

filename = "numbers.json"

with open(filename,"w") as f:
    json.dump(numbers,f)  # so dump the list numbers into f (numbers.json file)
# function takes two arguments: a piece of data to store and a file object it can use to store the data.



