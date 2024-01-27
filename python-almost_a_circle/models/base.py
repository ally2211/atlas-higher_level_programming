class Base:
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # Assign the provided id to the public instance attribute
        else:
            Base.__nb_objects += 1  # Increment the private class attribute
            self.id = Base.__nb_objects  # Assign the incremented value to the public instance attribute

# Example usage:
base1 = Base()
print(base1.id)  # Should print 1

base2 = Base(10)
print(base2.id)  # Should print 10

base3 = Base()
print(base3.id)  # Should print 2
