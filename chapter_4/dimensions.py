dimensions = (200, 50)

#tuples are basically same as lists but they are immutable which means you can't change them without re-assigning the whole thing
print(dimensions[0])
print(dimensions[1])
print("\n")

#!!! cant do this : dimensions[0] = 250  !!!

#you can loop through them just like a list

#this is how to change a tuple:
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print("\n")

#new tuple:
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)