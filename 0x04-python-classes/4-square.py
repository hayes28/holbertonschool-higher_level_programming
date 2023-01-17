#!/usr/bin/python3
"""
Defines a square class with a single attribute, 'size', which is
set during instantiation.
"""


class Square:
    """
    Initializes the square object with a size attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    Function to calculate the area of the square using the size
    attribute.
    """
    def area(self):
        return self.__size * self.__size

    """
    Getter and setter functions for the size attribute
    """
    @property
    def size(self):
        """
        Getter function to retrieve the value of a size attribute
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """
        Setter function to set the value of a size attribute
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints a square using '#' character
        """
        if self.size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
