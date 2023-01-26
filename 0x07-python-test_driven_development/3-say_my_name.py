#!/usr/bin/python3
"""
Prints "My name is First_name, Last_name" to the console.
"""


def say_my_name(first_name, last_name=""):
    """_summary_ Prints out given names

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    fullname = first_name + " " + last_name
    print("My name is " + fullname)
