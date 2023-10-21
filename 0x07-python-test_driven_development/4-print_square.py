#!/usr/bin/python3
"""
Prints "Prints square"
"""


def print_square(size):
    """
    Checks to make sure the size is an int > 0,
    then prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an int > 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
