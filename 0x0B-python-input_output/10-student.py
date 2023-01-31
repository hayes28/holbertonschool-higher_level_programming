#!/usr/bin/python3
""" Write a class Student that defines
a student by: (based on 9-student.py) """

import contextlib


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert a Student object to JSON"""
        if attrs is None:
            return vars(self)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = vars(self)[i]
            except Exception:
                pass
        return new_dict
