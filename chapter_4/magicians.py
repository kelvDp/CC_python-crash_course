magicians = ['alice', 'david', 'carolina']

#this will loop through the whole list of items and print every item seperately:
for magician in magicians:
    print(magician)

print("\n")

#can print same message for each item:
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician}") #everything that is indented is part of the loop

print("Thanks everyone,that was a great show !") #since this is not indented it will only be printed out once

print("\n")





