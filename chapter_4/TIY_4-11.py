friend_pizzas = ["Meat lovers" , "Chicken" , "Vegeterian"]
my_pizzas = friend_pizzas[:] #to copy over list

friend_pizzas.append("Ham & Mushroom")
my_pizzas.append("Plain cheese")

print("My favorite pizzas are : ")
for pizza in my_pizzas:
    print(pizza)
print("\n")

print("My friends' favorite pizzas are :")
for pizza in friend_pizzas:
    print(pizza)
