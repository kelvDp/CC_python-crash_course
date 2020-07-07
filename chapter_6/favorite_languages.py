favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")  # this will print sarah's fav language.

# can make this better with a loop and a .items() method:
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# if you want to loop through in a particular order you can use sorted()

# can make this more complex by adding lists in as the values :
favorite_languages_2 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages_2.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
