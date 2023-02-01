#!/usr/bin/python3
"""Creating a class called Base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
                return "[]"
        return json.dumps(list_dictionaries)
