def get_formatted_name(first,middle,last):
    """Generates a neatly formatted full name."""

    full_name = f"{first} {middle} {last}"
    return full_name.title()

# This version should work for people with middle names, but when we test
# it, we see that we’ve broken the function for people with just a first and last
# name. This time, running the file test_name_function.py gives an error...

# Assuming you’re checking the right
# conditions, a passing test means the function is behaving correctly and a
# failing test means there’s an error in the new code you wrote. So when a test
# fails, don’t change the test. Instead, fix the code that caused the test to fail.
# Examine the changes you just made to the function, and figure out how
# those changes broke the desired behavior.