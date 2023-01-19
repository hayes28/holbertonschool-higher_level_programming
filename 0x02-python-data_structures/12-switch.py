#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
# using tuple unpacking to swap
# the values of a and b in a single line of code
print("a={:d} - b={:d}".format(a, b))
# This is a common way to swap two variable values
# in python without needing a temporary variable.
