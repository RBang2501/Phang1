import math_2

# Circle class is a shape that represents a Circle in the 2D coordinate system.


class Circle:

    def __init__(self, position=[0, 0], velocity=[0, 0], mass=1, charge=0, radius=10):
        # initializing the Circle class with value.
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.charge = charge
