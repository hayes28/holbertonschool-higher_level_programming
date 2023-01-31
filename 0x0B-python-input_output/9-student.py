#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    def __init__(self, first_name, last_name, age):
        """ public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary with a student's
        information """
        return {"first_name": self.first_name, "last_name":
                self.last_name, "age": self.age}
