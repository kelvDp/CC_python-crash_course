sarah = {"name": "sarah", "animal": "cat", "owner": "jack"}
spike = {"name": "spike", "animal": "dog", "owner": "dave"}
fluffy = {"name": "fluffy", "animal": "snake", "owner": "megan"}
tiny = {"name": "tiny", "animal": "dog", "owner": "donny"}

animals = [sarah, spike, fluffy, tiny]

for animal in animals:
    print(f"{animal['name']} is a {animal['animal']}, and it's owner is {animal['owner']}")
