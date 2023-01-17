#!/usr/bin/python3
" Square class "

class Square:
    "defines size with value of 0"
    def __init__(self, size=0):
        "user input needs to be a number and greater than or equal to 0"
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    " function to get the area of the square "
    def area(self):
        return self.__size * self.__size
