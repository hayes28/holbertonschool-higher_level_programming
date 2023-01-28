#!/usr/bin/python3
"""
Checks if object is an instance of or inherited from a_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns: True of obj is an instance of a_class, False otherwise
    """
    return isinstance(obj, a_class)
