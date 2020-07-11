filename = "alice.txt"

try:
    with open(filename,encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, but this file {filename} does not exist here:")

else:
    # Count the approx nr of words in the file:
    words = content.split()
    num_of_words = len(words)
    print(f"This file {filename} has about {num_of_words} words.")

