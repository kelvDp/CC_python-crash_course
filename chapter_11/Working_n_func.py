# To make middle names optional, we move the parameter middle to the end
# of the parameter list in the function definition and give it an empty default
# value. We also add an if test that builds the full name properly, depending
# on whether or not a middle name is provided:

def get_formatted_name(first,last,middle=""):

    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



