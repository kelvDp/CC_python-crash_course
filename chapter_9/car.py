# Our class will store information
# about the kind of car we’re working with, and it will have a method that
# summarizes this information:

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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()  # method for default value

# You can change an attribute’s value in three ways: you can change the value
# directly through an instance(1), set the value through a method(2), or increment
# the value (add a certain amount to it) through a method(3) :

# 1 --> The simplest way to modify the value of an attribute is to access the attribute directly through an instance :

my_new_car.odometer_reading = 23  # so you change it on the go basically
my_new_car.read_odometer()

# 2 --> It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute
# directly, you pass the new value to a method that handles the updating internally:

# class Car:
# --snip--
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# we can update the code above to do additional work every
# time the odometer reading is modified by adding logical operators :
# ----snip ----
# if mileage >= self.odometer_reading:
#         self.odometer_reading = mileage
# else:
#     print("You can't roll back an odometer!")


# 3 --> Sometimes you’ll want to increment an attribute’s value by a certain amount
# rather than set an entirely new value:
# Here’s a
# method that allows us to pass this incremental amount and add that value to
# the odometer reading:

# class Car:
# --snip--
#     def update_odometer(self, mileage):
# --snip--
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)  --> will set value of odometer
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)  --> increments set value by 100
# my_used_car.read_odometer()
