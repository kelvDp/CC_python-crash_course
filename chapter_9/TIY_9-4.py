class Restaurant:
    """A simple attempt to model a Restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, and their best dish is {self.cuisine}.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def served(self):
        print(f"We have served {self.number_served} customers today !")

    def set_nr_served(self, number_served):
        self.number_served = number_served

    def increment_nr(self, nr):
        self.number_served += nr


restaurant = Restaurant("Pizza e Vino", "pizza")

restaurant.served()  # this will print 0 customers.
print("\n")
restaurant.number_served = 24  # changing the number of customers
restaurant.served()
print("\n")

# updating with a method:
restaurant.set_nr_served(65)
restaurant.served()
print("\n")

# incrementing the number of customers served:
restaurant.increment_nr(15)  # increments nr by 15
restaurant.served()
