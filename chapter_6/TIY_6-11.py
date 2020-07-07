cities = {
    "New York":{"country": "America", "population": 5000000, "fact": "Bill de Blasio is the mayor"},
    "Amsterdam": {"country": "Netherland", "population": 850000, "fact": "Houses the Van Gogh Museum"},
    "Johannesburg": {"country": "South Africa", "population": 957000, "fact": "Was home to Nelson Mandela"}
}

for city,information in cities.items():
    print(f"Here are some facts about {city} :")
    country = f"{information['country']}"
    population = f"{information['population']}"
    fact = f"{information['fact']}"
    print(f"This city is found in {country}, it has a population of {population} and a fact about it : {fact}")