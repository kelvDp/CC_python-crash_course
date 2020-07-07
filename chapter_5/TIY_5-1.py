#conditional testing:

car = "subaru"
print("Is car == 'subaru', I predict True.")
print(car == "subaru")

print("\nIs car == 'bmw',I predict False.")
print(car == "bmw")

print("\nIs car == 'Subaru',I predict False.")
print(car == "Subaru")

print("\nIs car.title() == 'Subaru', I predict True.")
print(car.title() == "Subaru")

color = "blue"
print("\nIs color == 'blue', I predict True.")
print(color == "blue")

print("\nIs color == 'red',I predict False.")
print(color == "red")

print("\nIs the color != 'purple', I predict True.")
print(color != "purple")

print("\nIs color != 'red' or != 'green', I predict True.")
print(color != "red" or color != "green")

print("\nIs car == 'bmw' and color == 'blue' ,I predict False. ")
print(car == 'bmw' and color == 'blue')

print("\nIs car != 'subaru', I predict False.")
print(car != "subaru")

