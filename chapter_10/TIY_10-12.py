import json

filename = "fav_nr.json"

try:
    with open(filename) as f:
        file = json.load(f)
except FileNotFoundError:
    fav_nr = input("What is your favorite number?")
    with open(filename,"w") as f:
        json.dump(fav_nr,f)
else:
    print(f"I know your favorite number! It's {file}")