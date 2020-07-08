# Positiobal arguments:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')  # the arguments have to be in the same position as its parameter


# you can call this function over and over again.
# order matters here because if you switch it around, the sentence that it prints will be wrong because the arguments were switched

# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion (you won’t end up
# with a harry named Hamster):

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')  # now the order does not matter.


# When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses
# the argument value. If not, it uses the parameter’s default value:

def describe_pet(pet_name, animal_type='dog'):  # dog will be the default value
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')  # so now if you don't add in an animal, it will automatically say its a dog.
# can simply also pass in the name of the pet without assigning it to a key.
# When you use default values, any parameter with a default value needs to be
# listed after all the parameters that don’t have default values. This allows
# Python to continue interpreting positional arguments correctly.

# the above functions can be called in many ways if there is a default value:
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster') #you can override the default value.
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

