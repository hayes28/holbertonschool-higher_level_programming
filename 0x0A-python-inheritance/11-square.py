#!/usr/bin/python3
""" Create class Square that inherits from Rectangle """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square specific class """

    def __init__(self, size):
        """ initializes Square """

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ Returns area of the Square """

        return(self.__size * self.__size)

    def __str__(self):
        """Returns the human readable
        string representation of self, says [Square] """

        return f"[Square] {self.__size}/{self.__size}"
