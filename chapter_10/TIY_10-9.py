try:
    with open(cats_file) as cats:
        cat_c = cats.read()
    with open(dogs_file) as dogs:
        dog_c = dogs.read()
except FileNotFoundError:
    pass
else:
    print(cat_c)
    print(dog_c)