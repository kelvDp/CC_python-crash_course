# Let’s look at a function that takes a first and last name, and returns a neatly
# formatted full name:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()  # since there is something that you return, you can assign it to a var


musician = get_formatted_name('jimi', 'hendrix')
print(musician) # then you can simply call the var name


# say we want to expand get_formatted_name() to handle middle
# names as well:
# this will work if you pass in a middle_name param
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
# this function as written
# would not work if you tried to call it with only a first name and a last name...
# so you can set a default value of an empty string
