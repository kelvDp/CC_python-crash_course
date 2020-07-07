favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ["grant", "jen", "phil", "aliza", "craig"]

for person in people:
    if person in favorite_languages.keys():
        print(f"{person}, thank you for taking part in the poll !")
    else:
        print(f"{person},would you like to be a part of the poll?")