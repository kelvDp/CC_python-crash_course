# To write text to a file, you need to call open() with a second argument telling
# Python that you want to write to the file.

filename = "programming.txt"

with open(filename,"w") as file_object:
    file_object.write("I love programming!")

# The second
# argument, 'w', tells Python that we want to open the file in write mode.
# You
# can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode
# that allows you to read and write to the file ('r+').
# It opens in read mode automatically if you don't pass in an argument.

# The open() function automatically creates the file you’re writing to if it
# doesn’t already exist.
# Be careful opening a file in write mode ('w')
# because if the file does exist, Python will erase the contents of the file before
# returning the file object.

# The write() function doesn’t add any newlines to the text you write. So if you
# write more than one line without including newline characters, your file may
# not look the way you want it to.

# ----------APPENDING TO A FILE------------

# If you want to add content to a file instead of writing over existing content,
# you can open the file in append mode. When you open a file in append mode,
# Python doesn’t erase the contents of the file before returning the file object.
# Any lines you write to the file will be added at the end of the file. If the file
# doesn’t exist yet, Python will create an empty file for you.

with open(filename,"a") as f:
    f.write("I also love finding meaning in large datasets. \n")
    f.write("I love creating apps that can run in a browser.\n")
