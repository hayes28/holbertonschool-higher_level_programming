#!/usr/bin/python3
""" Square class """


class Square:
    """defines size with value of 0"""
    def __init__(self, size=0):
        self.__size = size

    """function to get the area of the square"""
    def area(self):
        return self.__size * self.__size

    """getter and setter functions below"""
    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
