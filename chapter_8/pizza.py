# The function in the following example has one parameter,
# *toppings, but this parameter collects as many arguments as the calling line
# provides:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') #you can pass in as many arguments as you want to

# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed last
# in the function definition since python matcges positional and keyword arguments first and then collects any
# remaining arguments.

