#!/usr/bin/python3
def common_elements(set_1, set_2):
    # This function takes in two sets as parameters and returns
    # a list of common elements present in both sets
    # Using list comprehension to iterate through all elements
    # in set_1 and check if they are in set_2
    return [element for element in set_1 if element in set_2]
