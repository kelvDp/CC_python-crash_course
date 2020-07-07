favorite_places = {
    "jack": ["croatia", "russia", "australia"],
    "jill": ["canada", "brazil"],
    "kelly": ["south africa", "new zealand"]
}

for name,locations in favorite_places.items():
    print(f"{name}'s favorite locations are :")
    for location in locations:
        print(f"\t{location}")
