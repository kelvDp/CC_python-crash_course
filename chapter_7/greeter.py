# you always have to write a prompt that is clear enough for users to understand, so that they know what to type in :

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Sometimes you’ll want to write a prompt that’s longer than one line. For
# example, you might want to tell the user why you’re asking for certain input.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "  #you just end up concatenating a string together to build a multi-line string
name = input(prompt)
print(f"\nHello, {name}!")

