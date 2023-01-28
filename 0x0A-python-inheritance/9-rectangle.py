#!/usr/bin/python3
""" Create class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to contain attributes of rectangle shape """

    def __init__(self, width, height):
        """ Validates values/types and init the rectangle """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of the rectangle """

        return(self.__width * self.__height)

    def __str__(self):
        """Returns the human readable
        string representation of self """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
