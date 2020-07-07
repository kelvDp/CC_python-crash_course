#make a list of squared numbers:

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print("\n")

#can cut down on code above by leaving out the var and just appending directly:
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print("\n")

#you can cut down on code more by turning the for loop into a list comprehension (on line for loop basically):
#this allows you to do the above in one line of code:

square = [value **2 for value in range(11)]
print(square)
print("\n")

