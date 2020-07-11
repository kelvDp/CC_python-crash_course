# Handling the FileNotFoundError Exception
# One common issue when working with files is handling missing files. The
# file you’re looking for might be in a different location, the filename may be
# misspelled, or the file may not exist at all. You can handle all of these
# situations in a straightforward way with a try-except block:

filename = 'alice.txt'
# the encoding arg is needed when your system’s default encoding doesn’t match the encoding of the file that’s being read.
#with open(filename, encoding='utf-8') as f:
    #contents = f.read()

# This will cause a file not found error since python cannot find the file you are trying to open.
# this is how we could handle this error:

try:
    with open(filename,encoding="utf-8") as f:
        f.read()
except FileNotFoundError:
    print(f"Sorry, but the file {filename} does not exist...")

