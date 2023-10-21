#!/usr/bin/python3
"""
Exact same object- returns True if the same, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Checks if obj1 and obj2 are the exact same instances
    """
    return type(obj) == a_class
