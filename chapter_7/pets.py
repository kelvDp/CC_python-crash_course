# Removing all instances of specific values from a list :

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# this will loop through the list, and remove all of the cats inside of it