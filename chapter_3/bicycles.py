bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# to print only one specific item from the list
print(bicycles[0].title())  # can also use methods on the individual items from list
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print("\n")

# can print from last item :
print(bicycles[-1])  # works the same as string indexing and slicing

# can use these individual values from a list in other parts of your code :

message = f"My favorite bicycle was a {bicycles[1].title()}."

print(message)
