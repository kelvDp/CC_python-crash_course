# After you’ve read a file into memory, you can do whatever you want with
# that data, so let’s briefly explore the digits of pi. First, we’ll attempt to build a
# single string containing all the digits in the file with no whitespace in it:

file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string = pi_string + line.rstrip()

print(pi_string)
print(len(pi_string))

# you can do this with much bigger files as well , like pi with a million digits etc:

with open("pi_million_digits.txt") as million:
    more_lines = million.readlines()

big_pi_string = ""
for line in more_lines:
    big_pi_string += line.strip()

print(f"{big_pi_string[:52]}...") #this will only print the string up until the 52nd nr
print(len(big_pi_string))

# you can actually check to see whether your birthday is in the pi string somewhere :

birthday = input("Enter your birthday in the form mmddyy:")
if birthday in big_pi_string:
    print("Your birthday appears in the first million digits of pi!!")
else:
    print("Oops, your birthday isn't in the first million digits of pi ..")
