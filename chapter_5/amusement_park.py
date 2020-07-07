age = 12

# this will check multiple conditions and change the print message accordingly:
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# you can cut down on the code above by only printing the admission price at the end of the statements rather than inside
# the statement chain. :

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# you can use multiple lines of the elif statement to check conditions , and you can even leave out the else statement
# when you don't want a 'default' action to happen if nothing checks out.