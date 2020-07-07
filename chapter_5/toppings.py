requested_topping = 'mushrooms'

# checks inequality: so if the req_topping is NOT equal to anchovies, then it will print the message
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# you can check whether a certain value is in a list, if it is the output will be true, and if not --> false:

more_toppings = ['mushrooms', 'onions', 'pineapple']
# so you can ask :
# "mushrooms" in more_toppings     -->true because it is in the list
# "pepperoni" in more_toppings    --> false

# you can use multiple if statements to test multiple conditions :
more_requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in more_requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in more_requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in more_requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# this checks to see whether all checks passes whereas if you used elif etc it will stop running after one test passes.


# Checking for special items:
toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in toppings:
    print(f"Adding {topping}.")

print("\nFinished making your pizza!")

# But what if the pizzeria runs out of green peppers? An if statement inside
# the for loop can handle this situation appropriately:
for topping in toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}.")
print("\nFinished making your pizza!")

# Checking that a list is not empty :
just_more_toppings = []   #if empty --> false , if full --> true
if just_more_toppings:  #if there are items in list
    for requested_topping in just_more_toppings:
        print(f"Adding {requested_topping}.") #loop through and print toppings

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") #if list empty (it is) then it will ask if the person wants a plain pizza

# Using multiple lists:

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings_list = ['mushrooms', 'french fries', 'extra cheese']

# this will loop through both lists and check to see if items in the one are in the other
for requested_topping in requested_toppings_list:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

