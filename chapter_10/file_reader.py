# if using a longggg file name you can save it in a var and use that in open()
with open('pi_digits.txt') as file_object: # the 'as ...' is an alias that you can assign
    contents = file_object.read() #method to open the txt file and read it

print(contents)

# You can use a for loop on the file object to examine each line from a file
# one at a time:

with open("pi_digits.txt") as f:
    for line in f:
        print(line)  # this will now print all the text line for line
# this might print everything with extra lines or whitespace, in which case just use the strip() method

# The following example stores the lines of pi_digits.txt in a list inside the
# with block and then prints the lines outside the with block:

with open("pi_digits.txt") as r:
    lines = r.readlines()  #this will store each line in the var lines

for line in lines: # now we have access to the lines outside of the with block
    print(line.strip()) # will print lines

