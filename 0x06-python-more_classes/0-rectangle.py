#!/usr/bin/python3
"""
Defines two private instance attributes 'width' and 'height'.
TypeError will raise if width and height are not integers
ValueError will raise if width and height are less than zero
width and height are private attributes
"""


class Rectangle:
    def __init__(self, width=0, height=0):
            self.width = width
            self.height = height

    @property
    def width(self):
        '''
        Retrieves width of self.width
        '''
        return self.__width
    
    @property
    def height(self):
        '''
        Retrieves height of self.height
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''
        Sets width of self rectangle
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''
        Sets height of self rectangle
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value