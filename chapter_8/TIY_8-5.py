def describe_city(city,country = "Iceland"):
    print(f"{city} is in {country}")

# with default country:
describe_city("Reykjavik")
print("\n")

describe_city("Selfoss")
print("\n")

# not in default country:
describe_city("New York","USA")