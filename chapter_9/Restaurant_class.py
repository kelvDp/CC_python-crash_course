"""Here is a module for the Restaurant class"""


class Restaurant:
    """A simple attempt to model a Restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, and their best dish is {self.cuisine}.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")
