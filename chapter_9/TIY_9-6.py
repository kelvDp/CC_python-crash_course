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


class IceCreamStand(Restaurant):


    def __init__(self,name,cuisine,*flavors):
        super().__init__(name,cuisine)
        self.flavors = list(flavors)

    def display_flavors(self):
        print(self.flavors)


iceCream_stand = IceCreamStand("Jollies","Ice cream","Chocolate","Peppermint","Vanilla")


iceCream_stand.display_flavors()