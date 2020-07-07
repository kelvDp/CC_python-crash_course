pizzas = ["Meat lovers" , "Chicken" , "Vegeterian"]

#very basic loop to just print all the names of the pizzas in the list:
for pizza in pizzas:
    print(pizza)

print("\n")

#more complex loop:
for pizza in pizzas:
    print(f"I like {pizza} pizza !!")

print(f"But I don't like {pizzas[2]} all that much...")
print(f"The {pizzas[1]} is ok i guess...")
print(f"But {pizzas[0]} is my favorite pizza!!")