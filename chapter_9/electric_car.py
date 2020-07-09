# You don’t always have to start from scratch when writing a class. If the class
# you’re writing is a specialized version of another class you wrote, you can use
# inheritance. When one class inherits from another, it takes on the attributes
# and methods of the first class.
# The original class is called the parent class, and
# the new class is the child class :

# When you’re writing a new class based on an existing class, you’ll often want
# to call the __init__() method from the parent class. This will initialize any
# attributes that were defined in the parent __init__() method and make them
# available in the child class.

# This is the parent class:
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # this is a default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model}"
        return long_name.title()

    def read_odometer(self):  # function for default value
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


# -------------------------------------------------------------------------------

# Here we make the child class:

class ElectricCar(Car):  # you pass in the parent class name
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        # have to call super to get the parent attributes in child
        super().__init__(make, model, year)
        # The super() function at is a special function that allows you to call a
        # method from the parent class.


my_tesla = ElectricCar("tesla", "model s", 2019)

print(my_tesla.get_descriptive_name())  # so you can now use the functions/methods that were made in the parent class


# Once you have a child class that inherits from a parent class, you can add any
# new attributes and methods necessary to differentiate the child class from
# the parent class.
# --------------------------------------------------------
class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  # init after you init from parent

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# You can override any method from the parent class that doesn’t fit what
# you’re trying to model with the child class. To do this, you define a method
# in the child class with the same name as the method you want to override in
# the parent class. Python will disregard the parent class method and only pay
# attention to the method you define in the child class.

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # this is how you would add in another class if it isnt a parent , you use the
        # class name as a method??


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # you can then have access to all of the functions created in the battery class as well.



