#!/usr/bin/python3
""" Create class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to contain attributes of 
    rectangle shape """
    
    def __init__(self, width, height):
        """ Validates values/types and initalizes the 
        rectangle """
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
