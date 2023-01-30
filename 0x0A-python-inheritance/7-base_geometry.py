#!/usr/bin/python3
""" Public instances for class BaseGeometry """


class BaseGeometry:
    """ Empty class """

    def area(self):
        """ returns the area of a BaseGeometry
        But using an Exception. The area is not implemented """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ checks if the value is a valid integer """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
