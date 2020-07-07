rivers = {"nile": "eqypt", "sepik river": "new guinea", "volga": "russia"}

# to print whole dict
for name,location in rivers.items():
    print(f"The {name} runs through {location}")
    print("\n")

# to print only keys
for name in rivers.keys():
    print(name)
    print("\n")

#to print only the values
for location in rivers.values():
    print(location)