cats_file = "cats.txt"
dogs_file = "dogs.txt"

try:
    with open(cats_file,encoding="utf-8") as cats:
        cat_content = cats.read()
except FileNotFoundError:
    print(f"Sorry,but this file {cats_file} does not exist")
else:
    print(cat_content)

try:
    with open(dogs_file,encoding="utf-8") as dogs:
        dog_content = dogs.read()
except FileNotFoundError:
    print(f"Sorry,but the file {dogs_file} does not exist")
else:
    print(dog_content)

# another way of doing it:
# try:
#     with open(cats_file) as cats:
#         cat_c = cats.read()
#     with open(dogs_file) as dogs:
#         dog_c = dogs.read()
# except FileNotFoundError:
#     print("One of your files does not exist, please make sure they do and try again.")
# else:
#     print(cat_c)
#     print(dog_c)



