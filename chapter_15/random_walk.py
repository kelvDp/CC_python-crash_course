# To create a random walk, we’ll create a RandomWalk class, which will make
# random decisions about which direction the walk should take. The class
# needs three attributes: one variable to store the number of points in the walk
# and two lists to store the x- and y-coordinate values of each point in the
# walk.

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self,num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

# We’ll use the fill_walk() method, as shown here, to fill our walk with points
# and determine the direction of each step.
    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

