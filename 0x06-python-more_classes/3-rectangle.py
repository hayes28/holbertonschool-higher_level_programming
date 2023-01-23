#!/usr/bin/python3
"""
Defines two private instance attributes 'width' and 'height'.
TypeError will raise if width and height are not integers
ValueError will raise if width and height are less than zero
width and height are private attributes
"""


class Rectangle:
    """
    Rectangle definitions
    """
    def __init__(self, width=0, height=0):
        """
        Method to initialize a rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves width of self.width
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves height of self.height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets width of self rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets height of self rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle or 0
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle or 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return((self.__height + self.__width) * 2)

    def __str__(self):
        """
        Returns the string representation of a rectangle that is human readable
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        display = ''
        for i in range(self.__height):
            if i > 0:
                display += '\n'
            for _ in range(self.__width):
                display += '#'
        return display

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        is machine readable
        """
        return("Rectangle({}, {})".format(self.__width, self.__height))
