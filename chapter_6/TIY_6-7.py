persons_1 = {"first-name": "Alex", "Last-name": "Yu", "Age": 25, "City": "Joburg"}
persons_2 = {"first-name": "Max", "Last-name": "Black", "Age": 12, "City": "Cape Town"}
persons_3 = {"first-name": "Mika", "Last-name": "Breedt", "Age": 56, "City": "Joburg"}

people = [persons_1, persons_2, persons_3]

for person in people:
    print(f"My name is {person['first-name']} {person['Last-name']},I am {person['Age']} years old, and I live in {person['City']}")