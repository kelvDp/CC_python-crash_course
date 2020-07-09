# Creating a Class --> Dog Class :
# Each instance created from the Dog class will store a name and an age, and we’ll
# give each dog the ability to sit() and roll_over():
# a class is basically like an empty template that you use to create several objects that might have the same characteristics:

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# you can assign functions to the Dog class , so that you can access the specific function wherever you use this object.

# Making an Instance from a Class
# Think of a class as a set of instructions for how to make an instance. The
# class Dog is a set of instructions that tells Python how to make individual
# instances representing specific dogs.

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.") # to access the attributes of the instance/class for Dog, you use the '.' notation
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
# After we create an instance from the class Dog, we can use dot notation to call
# any method defined in Dog. Let’s make our dog sit and roll over:

my_dog.sit()  # this function comes from the class Dog we created
my_dog.roll_over()

# Creating Multiple Instances
# You can create as many instances from a class as you need :
your_dog = Dog("Fluffy",8)
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()




