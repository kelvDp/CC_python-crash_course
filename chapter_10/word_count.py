def count_words(file):
    """Counts the approx number of words in a file"""

    try:
        with open(file,encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, but this file {file} does not exist here...")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file} has about {num_words} words.")


file_name = "alice.txt"

count_words(file_name)

# In the previous example, we informed our users that one of the files was
# unavailable. But you don’t need to report every exception you catch.
# Sometimes you’ll want the program to fail silently when an exception occurs
# and continue on as if nothing happened. To make a program fail silently,
# you write a try block as usual, but you explicitly tell Python to do nothing in
# the except block. Python has a pass statement that tells it to do nothing in a
# block.

