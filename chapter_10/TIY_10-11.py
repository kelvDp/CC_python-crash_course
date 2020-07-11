import json

fav_nr = input("What is your favorite number ?")
filename = "fav_nr.json"

with open(filename,"w") as f:
    json.dump(fav_nr,f)

with open(filename) as file:
    my_fav_nr = json.load(file)
    print(f"I know your favorite number!It's {my_fav_nr}.")

