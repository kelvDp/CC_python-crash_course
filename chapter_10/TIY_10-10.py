filename = "alice.txt"

try:
    with open(filename,encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    pass
else:
    phrases = content.lower().count("the ")
    print(f"The phrase 'the' appears about {phrases} times in the file.")