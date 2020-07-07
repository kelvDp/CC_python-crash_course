cars = ['bmw', 'audi', 'toyota', 'subaru']

#this will sort the list in alphabetical order but permanently, so you won't be able to sort it back:
cars.sort()

print(cars)

# You can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method. The following example sorts the
# list of cars in reverse alphabetical order:
cars.sort(reverse=True)
print(cars)
print("\n")

#you can sort the list values only for printing/output without changing the list permanently by using sorted instead of sort:
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\n")

#you can reverse a list with the reverse method:
print(cars)
cars.reverse() #this also changes list permanently , but can just apply reverse again if you want normal list
print(cars)
print("\n")





