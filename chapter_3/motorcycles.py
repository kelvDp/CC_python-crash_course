motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#this will change the first item in the list :
motorcycles[0] = 'ducati'
print(motorcycles)

#this appends an item to the end of the list :
motorcycles.append('ducati')
print(motorcycles)

#can actually start with an empty list and just add items in on the go :
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#instead of appending an item to the very end of a list you can place a new item into a specific position in the list:
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  #this will now place the item at the beginning of the list
print(motorcycles)

#can delete a specific item out of a list
# If you know the position of the item you want to remove from a list, you can
# use the del statement.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#can do the same as above with the .pop() method:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()  #this removes last item from list unless you pass in an index
print(motorcycles)
print(popped_motorcycle)  #you can assign the popped value to a var to use

first_owned = motorcycles.pop(0) #pops off first item
print(f"The first motorcycle I owned was a {first_owned.title()}.")

 #if you don't know at which index the item is that you want to remove , you can use the remove method and pass in the name :
motorcycles.remove('ducati')
print(motorcycles)







