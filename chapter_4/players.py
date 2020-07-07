players = ['charles', 'martina', 'michael', 'florence', 'eli']

#this will print the list but only up until the 3 person (the :3 means up until but not including)
print(players[0:3]) #if you leave starting value, automatically starts from 0
print("\n")

#you can choose which part of your list to use:
print(players[1:4])  #so only the second,third and fourth person in list
print("\n")

#can choose only to print names at end of list by adding a starting point but no end point:
print(players[2:])  #so will print list from third person[2] to last person
print("\n")

#can print names at end of list by "reversing through list" or going backwards :
print(players[-3:])
print("\n")
#can also add a step size in as third param


#can loop through a sliced list:
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    print("\n")

