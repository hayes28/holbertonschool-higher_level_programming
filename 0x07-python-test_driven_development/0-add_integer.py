#!/usr/bin/python3
"""
    add_integer:
    returns sum of two integers or floats
    returns only integer
"""
def add_integer(a, b=98):
    """
    Change float to integer, making sure variables are ints
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
