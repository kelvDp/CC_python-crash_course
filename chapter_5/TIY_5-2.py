#more conditional tests:

my_string = "ball"
print("Is my_string == 'Ball',I predict False")
print(my_string == "Ball")
print("But : my_string.title() == 'Ball', will be True.")
print(my_string.title() == "Ball")

another_string = "HOUSE"
print("\nIs another_string == 'house', I predict False.")
print(another_string == "house")
print("But : another_string.lower() == 'house',will be true")
print(another_string.lower() == "house")

numbers = 10
print("\nIs numbers == 10 ,I predict True.")
print(numbers == 10)
print("Is numbers != 10, I predict False.")
print(numbers != 10)
print("Is numbers < 20, I predict True")
print(numbers < 20)
print("Is numbers > 42, I predict False")
print(numbers > 42)
print("Is numbers <= 12 , I predict True")
print(numbers <= 12)
print("Is numbers >=9 , I predict True")
print(numbers >= 9 )

print("\nIs my_string == 'ball' and numbers == 10, I predict True")
print(my_string == 'ball' and numbers == 10)

print("\nIs another_string == 'HOUSE' or numbers >50, I predict True.")
print(another_string == 'HOUSE' or numbers >50)

my_list = ["red", "yellow", "blue"]
print("\nIs green in my_list, I predict False.")
print("green" in my_list)

print("\nIs red in my_list, I predict True")
print("red" in my_list)