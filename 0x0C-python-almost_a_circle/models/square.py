#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Rectangle"""
        return '[' + type(self).__name__ + '] (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - ' \
            + str(self.size)

    def update(self, *args, **kwargs):
        """Assigning an argument to each attribute"""
        key = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, key[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle"""
        self_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return self_dict

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
