class PlacementPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return (self.x, self.y, self.z)

# Create a placement point at the origin with x=0, y=0, z=0
origin = PlacementPoint(0, 0, 0)

# Get the coordinates of the origin
print(origin.get_coordinates())  # Output: (0, 0, 0)
