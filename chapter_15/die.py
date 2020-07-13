from random import randint

class Die:
    """A class representing a single dice"""

    def __init__(self,side=6):
        """Assume the dice has 6 sides"""
        self.num_sides =side

    def roll(self):
        """Return random value between 1 and num of sides"""
        return randint(1, self.num_sides)


